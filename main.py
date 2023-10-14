from flet import *

def main(page: Page):

   def lo(_):
      page.add(Text(f"{a.value}"))
   a = TextField(label = "Login")
   page.add(a)
   page.add(TextButton("Login", on_click = lo))


app(main, view = WEB_BROWSER)
