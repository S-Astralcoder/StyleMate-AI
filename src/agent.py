import json
from litellm import ChatCompletionMessageToolCall, completion #pyright: ignore
from rich.console import Console

from src.functions import AgentFunctionBook
from src.goal import GoalBook
from src.memory import AgentMemory
from src.tools import ToolBook


class Agent:
    def __init__(self, model : str, goals : GoalBook, memory : AgentMemory, tool_book : ToolBook | None = None, agent_function_book : AgentFunctionBook | None = None, show_tool_calls : bool = True) -> None:
        self.model = model
        self.goals = goals
        self.memory = memory
        self.tool_book = tool_book
        self.agent_function_book = agent_function_book

        self.console = Console()
        self.show_tool_calls = show_tool_calls


        self.memory.add_memory("system", goals.get_goals())
    
    def _get_agent_response(self, message : str, tool_call_omit_message : bool = False):
        if not tool_call_omit_message:
            self.memory.add_memory("user", message)
        try:
            response = completion(model=self.model, messages=self.memory.get_all_memory(), tools=self.tool_book.get_tools() if self.tool_book else None)
            assistant_message : str | None = response.choices[0].message.content #pyright: ignore
            if  assistant_message is not None:
                self.memory.add_memory("assistant", assistant_message) #pyright: ignore
            return response
        except Exception:
            self.console.print_exception()
            raise SystemExit("Exiting Operation Due to Error..")

    def execute_tool_calls_list(self, tool_calls : list[ChatCompletionMessageToolCall]):
        if self.agent_function_book is None:
            raise Exception("Function call was triggered when function book doesn't exists")

        for tool_call in tool_calls:
            tool_call_id = tool_call.id
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            if self.show_tool_calls:
                self.console.print(f"\n[yellow]Tool {function_name} was called with arguments {json.dumps(arguments)}\n")
            try:
                result = self.agent_function_book.execute_function(function_name=function_name, arguments=arguments) #pyright: ignore
            except Exception as e:
                self.console.print(f"[red]Error Occurred while calling tool : {e}")
                self.memory.add_tool_call_result(id=tool_call_id, result_content=f"{e}")
                continue
            if self.show_tool_calls:
                self.console.print(f"\n[yellow]Tool {function_name} call resulted with response :\n{result}\n")
            self.memory.add_tool_call_result(id=tool_call_id, result_content=result)


    def send_agent_prompt(self, message : str, max_iteration : int = 10):
        tool_called : bool = False
        cycle : int = 0
        while cycle <= max_iteration:
            response = self._get_agent_response(message=message, tool_call_omit_message=tool_called)
            assistant_message : str = response.choices[0].message.content #pyright: ignore
            tool_calls = response.choices[0].message.tool_calls #pyright: ignore
            if tool_calls:
                self.memory.add_tool_call_memory(response=response.choices[0].message) #pyright: ignore 
                self.execute_tool_calls_list(tool_calls=tool_calls) #pyright: ignore
                cycle += 1
                tool_called = True
                continue
            return assistant_message
        return "The Agent has passed the iteration limit"