import json
from typing import Literal


class AgentMemory:
    def __init__(self) -> None:
        """Class responsible for managing agent memory"""
        self.memory : list[dict[Literal["role", "content", "tool_call_id"], str]] = []


    def add_memory(self, role : str, content : str):
        self.memory.append({"role" : role, "content" : content})

    
    def add_tool_call_memory(self, response):
        self.memory.append(response)

    def add_tool_call_result(self, id : str, result_content : str):
        self.memory.append({"role" : "tool", "tool_call_id" : id, "content" : result_content})

    def get_all_memory(self):
        return self.memory

    def overwrite_whole_memory(self, new_memory : list[dict[Literal["role", "content", "tool_call_id"], str]]):
        self.memory = new_memory
    