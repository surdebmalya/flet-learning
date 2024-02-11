import flet as ft
from flet import UserControl, Text, Row, Page, ControlEvent, MainAxisAlignment, ElevatedButton

class Increment(UserControl):
    def __init__(self, text, start_number=0):
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number = Text(value=str(start_number), size=40)

    def increment(self, e):
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self)->Row:
        return Row(
            controls=[
                ElevatedButton(self.text, on_click=self.increment),
                self.text_number
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            width=300
        )

def main(page):
    page.title = "Reuseable App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    
    page.add(Increment("Study"))
    page.add(Increment("Coding"))


if __name__ == "__main__":
    # ft.app(target=main)
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)