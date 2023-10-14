from flet import *

def main(page: Page):
    page.add(Text("Hello World"))
    page.update()

    page.add(TextField(label = "Login"))
    page.add(TextButton("Login"))

app(main, view = WEB_BROWSER)
