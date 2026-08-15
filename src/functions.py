from typing import Any, Callable


class AgentFunction:
    def __init__(self, name : str , function : Callable[..., Any]) -> None:
        self.name = name
        self.function = function


class AgentFunctionBook:
    def __init__(self, functions_list : list[AgentFunction]) -> None:
        self.functions_list = functions_list


    def execute_function(self, function_name : str, arguments : dict[str, Any]):
        function_call : Callable[..., Any] | None = None
        for function in self.functions_list:
            if function.name == function_name:
                function_call = function.function
        if function_call is None:
            raise Exception("Function doesn't exists, use already existing tools.")
        return function_call(**arguments)

    
