from flet import *

def main(page: Page):
    page.add(Text("Hello"))
    page.update()

    page.add(TextField(label = "Login"))

app(main, view = WEB_BROWSER)
