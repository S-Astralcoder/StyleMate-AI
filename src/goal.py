class Goal:
    def __init__(self, role : str, priority : int, instruction : str) -> None:
        self.role = role
        self.priority = priority
        self.instruction = instruction

    def get_goal(self):
        return f"""Priority : {self.priority}\n{self.role}\n\n{self.instruction}\n----------\n"""


class GoalBook:
    def __init__(self, goal_list : list[Goal]) -> None:
        self.goal_list = goal_list

    def get_goals(self):
        content = ""

        for goal in self.goal_list:
            content += goal.get_goal()
        return content
        