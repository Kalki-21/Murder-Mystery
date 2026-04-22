class GameEngine:
    def __init__(self, case):
        self.case = case
        self.clue_index = 0
        self.clues_found = []
        self.statements = []

    # =========================
    # CLUE SYSTEM (UNLIMITED SAFE)
    # =========================
    def get_clue(self):
        # If all clues are shown
        if self.clue_index >= len(self.case.clues):
            return "No new clues. Review what you have."

        clue = self.case.clues[self.clue_index].description
        self.clue_index += 1
        self.clues_found.append(clue)

        return clue

    # =========================
    # INTERROGATION
    # =========================
    def ask_question(self, suspect, question):
        answer = suspect.responses.get(question, "No response.")

        self.statements.append({
            "suspect": suspect.name,
            "question": question,
            "answer": answer
        })

        return answer

    # =========================
    # CONTRADICTIONS
    # =========================
    def get_contradictions(self):
        return self.case.contradictions

    # =========================
    # FINAL CHECK
    # =========================
    def check_answer(self, suspect):
        return suspect == self.case.solution