import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page):
    page.title = "Signup Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    text_username = TextField(
        label="Username", 
        text_align=ft.TextAlign.LEFT,
        width=200
    )

    text_password = TextField(
        label="Password", 
        text_align=ft.TextAlign.LEFT,
        width=200,
        password=True
    )

    checkbox = Checkbox(
        label="I agree to the stuff",
        value=False
    )

    submit = ElevatedButton(
        text="Sign up",
        width=200,
        disabled=True
    )

    def validate(e):
        if all([text_username.value, text_password.value, checkbox.value]):
            submit.disabled=False
        else:
            submit.disabled=True
        page.update()

    def after_submit(e):
        print(f"Username: {text_username.value}")
        print(f"Password: {text_password.value}")
        page.clean()

        page.add(
            Row(
                [
                    Text(value=f"Welcome: {text_username.value}", size=20)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkbox.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate

    submit.on_click = after_submit

    page.add(
        Row(
            [
                Column(
                    [
                        text_username,
                        text_password,
                        checkbox,
                        submit
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)