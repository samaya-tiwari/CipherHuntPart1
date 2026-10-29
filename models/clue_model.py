class ClueModel:
    def __init__(self, clue_id=None, user_id=None, clue_text="", key="", is_solved=False):
        self.clue_id = clue_id
        self.user_id = user_id
        self.clue_text = clue_text
        self.key = key
        self.is_solved = is_solved

    def check_answer(self, user_answer: str) -> bool:
        """Comprueba si la respuesta del usuario coincide con la clave de la pista."""
        if user_answer and user_answer.strip().lower() == self.key.strip().lower():
            self.is_solved = True
            return True
        return False

    def set_clue(self, clue_text: str, key: str):
        self.clue_text = clue_text.strip()
        self.key = key.strip()
        self.is_solved = False