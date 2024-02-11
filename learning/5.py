# building text editor
from flet import UserControl, TextField, InputBorder, Page, ControlEvent, app

class TextEditor(UserControl):
    def __init__(self):
        super().__init__()
        self.textfield = TextField(
            multiline=True,
            autofocus=True,
            border=InputBorder.NONE,
            min_lines=40,
            on_change=self.save_text,
            content_padding=30
        )

    def save_text(self, e):
        with open('5.txt', 'w') as f:
            f.write(self.textfield.value)

    def read_text(self):
        try:
            with open('5.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text="Welcome to the text editor"

    def build(self):
        self.textfield.value = self.read_text()
        return self.textfield

def main(page: Page):
    page.title = "Text Editor"
    page.scroll = True

    page.add(TextEditor())

if __name__ == "__main__":
    app(target=main)