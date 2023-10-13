from flet import *

def main(page: Page):
    page.add(Text("Hello"))
    page.update()

    page.add(TextField(label = "Logiaan"))

app(main, view = WEB_BROWSER)
