from flet import *

def main(page: Page):


    page.add(TextField(label = "Login"))
    page.add(TextButton("Logingj"))

    page.update

app(main, view = WEB_BROWSER)
