from flet import *

def main(page: Page):

   def lo(_):
      page.add(Text(f"{a.value}"))
   a = TextField(label = "Login")
   page.add(a)
   page.add(TextButton("Login to the syste
   ", on_click = lambda : _ lo(_)))


app(main, view = WEB_BROWSER)
