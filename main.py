from flet import *

def main(page: Page):
    page.title("Hello")

    page.add(TextField(label = "Login"))
    page.add(TextButton("Loginn"))

    page.update()

app(main, view = WEB_BROWSER)
