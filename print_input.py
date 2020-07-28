'''This program will print out the entered value in the text box'''

# import the neccessary classes from guizero
from guizero import App, TextBox, PushButton, Text

def print_text():
    # the code for printing text goes here
    text.value = text_entry.value

# setup the app
app = App(title="Print Entered Value")

# give the user a place to enter text
text_entry = TextBox(app)

# create the button and give it a command
print_button = PushButton(app, text="Print", command=print_text)

# give the function some place to print the input text
text = Text(app)

# finally display the app
app.display()