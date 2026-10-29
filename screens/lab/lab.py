from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import Screen


class LabScreen(Screen):
    status_text = StringProperty("")
    created_clues = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        path = App.get_running_app().base_path
        Builder.load_file(path + "\\screens\\lab\\lab.kv")

    def save_clue(self):
        riddle = self.ids.riddle_input.text.strip()
        cipher_text = self.ids.cipher_input.text.strip()
        answer = self.ids.answer_input.text.strip()

        if not riddle or not cipher_text or not answer:
            self.status_text = "Please fill in the riddle, cipher text, and answer."
            return

        clue = {
            "riddle": riddle,
            "cipher_text": cipher_text,
            "answer": answer,
        }
        self.created_clues = [*self.created_clues, clue]
        self.status_text = f"Clue saved! You have created {len(self.created_clues)}."

    def clear_form(self):
        self.ids.riddle_input.text = ""
        self.ids.cipher_input.text = ""
        self.ids.answer_input.text = ""
        self.status_text = ""

