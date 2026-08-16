import warnings
from src.agent import Agent
from src.functions import AgentFunction, AgentFunctionBook
from src.goal import Goal, GoalBook
from src.memory import AgentMemory
from src.tool.tool import add_discovered_preference, get_all_discovered_preferences, get_user_data
from src.tools import Tool
from dotenv import load_dotenv
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich import print

from src.tools import ToolBook
load_dotenv()

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")


agent = Agent(
    model="gemini/gemini-3.1-flash-lite",
    goals=GoalBook([Goal(role="you are a Profession Style AI assistant called styli. you have domain level expertise for fashion styling for both men and women. your goal is provide hyper personalized advice on what to wear.",
    priority=1,
    instruction="""
    You represent StyleMate Company. where you are designed to provide hyper personalized style advice related to cloths and their colour. Initially you will be provided with information about user such as
    what they like and what cloths they have and it's color, and their gender.

    Rules:
    1. You response should clear, concise and friendly.
    2. You should always recommend cloths that the user already have.
    3. Use colour theory to recommend colour combination.

    Additional Instructions:
    1. When chatting with used. keep an eye for any additional preference the user has
    2. Passively collect user preference information that the user shares

    WHAT NOT TO DO:
    1. Recommend the cloths or color of cloths that user don't have
    2. Never be rude to users

    You have been provided with tools to get information about user such as preference and what cloths they have. and also tools to update user preferences
    """),]),
    memory=AgentMemory(),
    tool_book=ToolBook(tools_list=[
        Tool(
            name="get_user_data", 
            description="Function used to get user information. which includes users style preferences",
            parameters={}),
        Tool(name="add_discovered_preference",
        description="used to add new discovered preferences from the user",
        parameters={
            "type" : "object",
            "properties" : {
                "title" : {
                "type" : "string",
                "description" : "title for the new discovery"
                },
                "info" : {
                    "type" : "string",
                    "description" : "information about the discovery"
                }
            }
        }),
        Tool(
            name="get_all_discovered_preferences",
            description="you to get all the information about new discovery made during interaction",
            parameters={}
        )
    ]),
    agent_function_book=AgentFunctionBook([
        AgentFunction(name="get_user_data", function=get_user_data),
        AgentFunction(name="add_discovered_preference", function=add_discovered_preference),
        AgentFunction(name="get_all_discovered_preferences", function=get_all_discovered_preferences),
    ]),
    show_tool_calls=True
    )


while True:
    prompt = Prompt.ask("[green] Let's Chat", default="exit")
    if prompt.strip().lower() == "exit":
        break
    response = agent.send_agent_prompt(message=prompt)
    print("[blue]Assistant")
    print(Markdown(response))
