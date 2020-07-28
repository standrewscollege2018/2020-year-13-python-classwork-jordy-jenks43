from guizero import App, Box, Text, TextBox

app = App()
title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="Title")
buttons_box = Box(app, width="fill", align="bottom", border=True)
Text(buttons_box, text="Buttons")
options_box = Box(app, height="fill", align="right", border=True)
Text(options_box, text="Options")
content_box = Box(app, width="fill", align="top", border=True)
Text(content_box, text="Content")
form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
Text(form_box, grid=[0,0], text="Form", align="right")
Text(form_box, grid=[0,1], text="Form", align="left")
TextBox(form_box, grid=[1,1], text="Data", width="fill")

app.display()