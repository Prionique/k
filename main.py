from flet import *
from sqlite3 import *

def main(page: Page):


    page.add(TextField(label = "Login"))
    page.add(TextButton("Login"))

    page.update

app(main, view = WEB_BROWSER)
