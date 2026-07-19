from playwright.sync_api import Page

class Actor:
    def __init__(self, name: str, page: Page):
        self.name = name
        self.page = page
        self._memory = {}

    def remember(self, key: str, value):
        self._memory[key] = value

    def recall(self, key: str):
        return self._memory.get(key)

    def attempts_to(self, *tasks):
        for task in tasks:
            task.perform_as(self)

    def asks_for(self, question):
        return question.answered_by(self)