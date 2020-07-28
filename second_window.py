from guizero import App, Window, Text, PushButton

def open_window():
    window.show()

def close_window():
    window.hide()

app = App(title="Main Window")

window = Window(app, title="Second Window")
window.hide()

open_button = PushButton(app, text="open", command=open_window)
close_button = PushButton(window, text="close", command=close_window)

app.display()