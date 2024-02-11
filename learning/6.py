# navigation
import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page):
    page.title="Navigation changing"
    
    def route_changing(e: RouteChangeEvent):
        page.views.clear()
        # Home
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(title=Text("Home"), bgcolor='blue'),
                    Text(value='Home', size=40),
                    ElevatedButton(text='Go to store', on_click=lambda _:page.go('/store'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )
        #store
        if page.route=='/store':
            page.views.append(
                View(
                    route="/store",
                    controls=[
                        AppBar(title=Text("Store"), bgcolor='blue'),
                        Text(value='Store', size=40),
                        ElevatedButton(text='Go back', on_click=lambda _:page.go('/'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )

        page.update()

    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_changing
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)