class Suspect:
    def __init__(self, name, responses):
        self.name = name
        self.responses = responses  # dict of question: answer


class Clue:
    def __init__(self, description):
        self.description = description


class Case:
    def __init__(self, title, story, suspects, clues, contradictions, solution):
        self.title = title
        self.story = story
        self.suspects = suspects
        self.clues = clues
        self.contradictions = contradictions
        self.solution = solution