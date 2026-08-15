from __future__ import annotations

from litellm import ChatCompletionMessageToolCall


class ToolBook:
    def __init__(self, tools_list : list[Tool]) -> None:
        self.tools_list = tools_list

    def get_tools(self):
        tools : list[ChatCompletionMessageToolCall] = []
        for tool in self.tools_list:
            tools.append(tool.get_tool_data())
        return tools


class Tool:
    def __init__(self, name : str, description : str, parameters : dict[str, str | dict[str, str | dict[str, str | dict[str, str]]]]) -> None:
        self.name = name
        self.description = description
        self.parameters = parameters

    def get_tool_data(self) -> ChatCompletionMessageToolCall:
        tool = {
            "type" : "function",
            "function" : {
                "name" : self.name,
                "description" : self.description,
                "parameters" : self.parameters
            }
        }
        return tool #pyright: ignore

    