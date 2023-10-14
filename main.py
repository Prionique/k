from flet import *

def main(page: Page):

    page.title("Hello")


    page.add(TextField(label = "Login"))
    page.add(TextButton("Login"))

    page.update

app(main, view = WEB_BROWSER)
