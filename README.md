GUI Calculator

 This is just a basic calculator I threw together using Python and the built-in tkinter library. It was a fun little project to practice handling events and basic layout management.

What It Does (Features)

Honestly, it's pretty straightforward:
Four-Function Math: It handles the basics: addition, subtraction, multiplication, and division.
A Clean Slate: There's a big red "CLEAR" button that wipes the screen instantly (super satisfying, by the way).
Error Proofing (Kind of): If you try to do something weird like dividing by zero or typing in garbage, it just throws up a clear "Error" message instead of crashing the whole program.

Fixed Size: I locked the window size (300x400) because, let's be real, calculators usually look best at one specific dimension.

How to Get It Running

If you have Python installed (which you probably do!), this is super simple.
Save the code: Grab the Python script and save it as something like calculator.py.
Run it: Open your terminal or command prompt, navigate to where you saved the file, and run this command:
python calculator.py


That's it! The little GUI window should pop right up.
A Quick Walkthrough of the Code

The whole thing is built around three main functions that handle all the action:

1. button_click(value)

This is the workhorse for most of the buttons.
Whenever you click a number, a decimal point, or an operator (+, -, etc.), this function takes that character (value) and just pastes it onto the end of whatever is already showing in the display.
I used a tk.StringVar() called entry_var to manage the text dynamically—it's the only way to link the Python logic to the graphical input field.

2. clear()

The Big Red Button: This function is super simple. It just sets entry_var back to an empty string (""), clearing the display instantly.

3. calculate()

This is where the magic (and the potential chaos) happens, bound to the = button.

The Magic: I'm using Python's built-in eval() function. I know, I know—it's risky if you were building something exposed to the web, but for a simple desktop calculator, it saves us a ton of time writing a custom expression parser. It just takes the string (e.g., "5+2*3") and spits out the answer.
The Safety Net: Crucially, I wrapped the eval() call in a try...except block. If the user messes up the input or tries to divide by zero, the except block catches the error and tells the user: "Error".

Layout Notes

The buttons are built using a nested loop (for row in buttons: ... for btn_text in row: ...). This keeps the code clean and easily scalable if I ever wanted to add more rows or columns.