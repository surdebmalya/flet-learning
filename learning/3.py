import flet as ft
from flet import Row, Text, KeyboardEvent

def main(page):
    page.title = "Keyboard Event Listener"
    page.spacing = 30
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = 600
    page.window_height = 600

    key = Text('Key', size=30)
    shift = Text('Shift', size=30, color='red')
    ctrl = Text('Control', size=30, color='blue')
    alt = Text('Alt', size=30, color='green')

    def on_keyboard(e):
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt

        print(e.data)
        page.update()

    page.on_keyboard_event = on_keyboard

    page.add(
        Text("Press any combination of keys..."),
        Row(
            [
                key, shift, ctrl, alt
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
