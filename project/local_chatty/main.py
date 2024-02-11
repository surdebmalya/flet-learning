from flet import UserControl, TextField, InputBorder, Page, ControlEvent, app, Row, Column, MainAxisAlignment, IconButton
import flet as ft
import time

class ChatApplication(UserControl):
    def __init__(self):
        super().__init__()
        self.windowfield = TextField(
            multiline=True,
            border=InputBorder.OUTLINE,
            min_lines=11,
            max_lines=11,
            content_padding=30,
            read_only=True,
            width=450
        )
        self.chatfield = TextField(
            multiline=True,
            autofocus=True,
            border=InputBorder.OUTLINE,
            min_lines=1,
            max_lines=2,
            content_padding=30,
            hint_text="Enter your message",
            width=400,
            shift_enter=True,
            on_submit=self.send_message
        )
        self.sendbutton = IconButton(ft.icons.SEND, on_click=self.send_message)

    def send_message(self, e):
        text = self.chatfield.value.strip()
        self.chatfield.value = ""
        if text!="":
            existing_text = self.read_database()
            existing_text += '— ' + text + '\n'
            self.windowfield.read_only = False
            self.windowfield.value = existing_text
            with open('database.txt', 'w') as f:
                f.write(self.windowfield.value)
            self.windowfield.read_only = True
        self.update()

    def broadcasting(self):
        existing_text = self.read_database()
        self.windowfield.read_only = False
        self.windowfield.value = existing_text
        self.windowfield.read_only = True
        self.update()

    def read_database(self):
        try:
            with open('database.txt', 'r') as f:
                return f.read()
        except:
            return ""

    def build(self):
        self.windowfield.read_only = False
        self.windowfield.value = self.read_database()
        self.windowfield.read_only = True
        return Column(
            [
                Row([self.windowfield], alignment=MainAxisAlignment.CENTER),
                Row([self.chatfield, self.sendbutton], alignment=MainAxisAlignment.CENTER)
            ]
        )

def main(page: Page):
    page.title = "Chatty"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = 500
    page.window_height = 480
    
    elements = ChatApplication()
    page.add(elements)

    f = open('database.txt', 'r')

    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
        else:
            print ('New message: ', line)
            elements.broadcasting()
            print ('Broadcasting Done')

if __name__ == "__main__":
    app(target=main)
    # app(target=main, view=ft.AppView.WEB_BROWSER)