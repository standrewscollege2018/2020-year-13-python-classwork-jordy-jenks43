from guizero import App, PushButton, Text

def hello():
    return print("Hello!")

app = App()
text = Text(app)
button = PushButton(app, command=hello)
app.display()
