from flet import *

def main(page: Page):

   page.add(Text("Hello"))
   page.add(TextButton("Login"))


app(main, view = WEB_BROWSER)
