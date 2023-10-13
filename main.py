from flet import *

def main(page: Page):
    page.add(Text("Hello"))
    page.update()

app(main, view = WEB_BROWSER)