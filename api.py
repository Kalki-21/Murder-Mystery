from cases import load_cases
from game_engine import GameEngine

class API:
    def __init__(self):
        self.cases = load_cases()
        self.current_case = None
        self.engine = None

    def get_cases(self):
        return [c.title for c in self.cases]

    def select_case(self, index):
        self.current_case = self.cases[index]
        self.engine = GameEngine(self.current_case)
        return self.current_case.story

    def get_suspects(self):
        return [s.name for s in self.current_case.suspects]

    def get_clue(self):
        return self.engine.get_clue()

    def ask(self, suspect, question):
        for s in self.current_case.suspects:
            if s.name == suspect:
                return self.engine.ask_question(s, question)
        return "No response"

    def accuse(self, name):
        return self.engine.check_answer(name)
    
    def reset(self):
        self.current_case = None
        self.engine = None

    def get_questions(self, suspect_name):
        for s in self.current_case.suspects:
            if s.name == suspect_name:
                return list(s.responses.keys())
        return []
    