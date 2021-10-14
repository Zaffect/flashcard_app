
from tkinter import *
from random import randint
import math 

root = Tk()
root.title("Flashcard App!")
root.geometry("400x400")
# root.iconbitmap("C:/GUIs/maths.png/")

# Create State Capitals Dictionary
state_capitals = {
	"Alabama": "Montgomery",
	"Alaska": "Juneau",
	"Arizona": "Phoenix	",
	"Arkansas": "Little Rock",
	"California": "Sacramento",
	"Colorado": "Denver",
	"Connecticut": "Hartford",
	"Delaware": "Dover",
	"Florida": "Tallahassee",
	"Georgia": "Atlanta",
	"Hawaii": "Honolulu",
	"Idaho": "Boise",
	"Illinois": "Springfield",
	"Indiana": "Indianapolis",
	"Iowa": "Des Moines",
	"Kansas": "Topeka",
	"Kentucky": "Frankfort",
	"Louisiana": "Baton Rouge",
	"Maine": "Augusta",
	"Maryland": "Annapolis",
	"Massachusetts": "Boston",
	"Michigan": "Lansing",
	"Minnesota": "Saint Paul",
	"Mississippi": "Jackson",
	"Missouri": "Jefferson City",
	"Montana": "Helena",
	"Nebraska": "Lincoln",
	"Nevada": "Carson City",
	"New Hampshire": "Concord",
	"New Jersey": "Trenton",
	"New Mexico": "Santa Fe",
	"New York": "Albany",
	"North Carolina": "Raleigh",
	"North Dakota": "Bismarck",
	"Ohio": "Columbus",
	"Oklahoma": "Oklahoma City",
	"Oregon": "Salem",
	"Pennsylvania": "Harrisburg",
	"Rhode Island": "Providence",
	"South Carolina": "Columbia",
	"South Dakota": "Pierre",
	"Tennessee": "Nashville",
	"Texas": "Austin",
	"Utah": "Salt Lake City",
	"Vermont": "Montpelier",
	"Virginia": "Richmond",
	"Washington": "Olympia",
	"West Virginia": "Charleston",
	"Wisconsin": "Madison",
	"Wyoming": "Cheyenne"
}

# Create Functions
def add_correct(num1, num2):
	# Calculate correct answer
	correct = num1 + num2

	# Correct or incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct!")
	output_answer_incorrect.set("Incorrect: " + str(num1) + " + " + str(num2) + " = " + str(correct))

	if int(add_answer.get()) == correct:
		add_correct_label.config(text=output_answer_correct.get())
	else:
		add_correct_label.config(text=output_answer_incorrect.get())

	# Clear Answer Box
	add_answer.delete(0, "end")

	# Generate Two New Random Numbers
	num_1.set(randint(0, 10))
	num_2.set(randint(0, 10))	
	add_flash.config(text=str(num_1.get()) + " + " + str(num_2.get()), font=("Helvetica", 50))

def add():
	hide_menu_frames()
	add_frame.pack(fill="both", expand=1)

	# Create two random numbers
	global num_1
	global num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0, 10))
	num_2.set(randint(0, 10))

	# Display Numbers
	global add_flash
	add_flash = Label(add_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Helvetica", 50))
	add_flash.pack(pady=10)

	# Create Answer Box
	global add_answer
	add_answer = Entry(add_frame)
	add_answer.pack(pady=5)

	# Create Answer Button
	global add_button
	add_button = Button(add_frame, text="Answer", command=lambda: add_correct(num_1.get(), num_2.get()))
	add_button.pack(pady=5)

	# Correct or Incorrect Message
	global add_correct_label
	add_correct_label = Label(add_frame, text="Enter Your Answer Above")
	add_correct_label.pack(pady=5)

def subtract_correct(num1, num2):
	# Calculate correct answer
	correct = num1 - num2

	# Correct or incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct!")
	output_answer_incorrect.set("Incorrect: " + str(num1) + " - " + str(num2) + " = " + str(correct))

	if int(subtract_answer.get()) == correct:
		subtract_correct_label.config(text=output_answer_correct.get())
	else:
		subtract_correct_label.config(text=output_answer_incorrect.get())

	# Clear Answer Box
	subtract_answer.delete(0, "end")

	# Generate Two New Random Numbers
	num_1.set(randint(0, 10))
	num_2.set(randint(0, 10))	
	subtract_flash.config(text=str(num_1.get()) + " - " + str(num_2.get()), font=("Helvetica", 50))

def subtract():
	hide_menu_frames()
	subtract_frame.pack(fill="both", expand=1)

	# Create two random numbers
	global num_1
	global num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0, 10))
	num_2.set(randint(0, 10))

	# Display Numbers
	global subtract_flash
	subtract_flash = Label(subtract_frame, text=str(num_1.get()) + " - " + str(num_2.get()), font=("Helvetica", 50))
	subtract_flash.pack(pady=10)

	# Create Answer Box
	global subtract_answer
	subtract_answer = Entry(subtract_frame)
	subtract_answer.pack(pady=5)

	# Create Answer Button
	global subtract_button
	subtract_button = Button(subtract_frame, text="Answer", command=lambda: subtract_correct(num_1.get(), num_2.get()))
	subtract_button.pack(pady=5)

	# Correct or Incorrect Message
	global subtract_correct_label
	subtract_correct_label = Label(subtract_frame, text="Enter Your Answer Above")
	subtract_correct_label.pack(pady=5)

def multiply_correct(num1, num2):
	# Calculate correct answer
	correct = num1 * num2

	# Correct or incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct!")
	output_answer_incorrect.set("Incorrect: " + str(num1) + " x " + str(num2) + " = " + str(correct))

	if int(multiply_answer.get()) == correct:
		multiply_correct_label.config(text=output_answer_correct.get())
	else:
		multiply_correct_label.config(text=output_answer_incorrect.get())

	# Clear Answer Box
	multiply_answer.delete(0, "end")

	# Generate Two New Random Numbers
	num_1.set(randint(0, 10))
	num_2.set(randint(0, 10))	
	multiply_flash.config(text=str(num_1.get()) + " x " + str(num_2.get()), font=("Helvetica", 50))

def multiply():
	hide_menu_frames()
	multiply_frame.pack(fill="both", expand=1)

	# Create two random numbers
	global num_1
	global num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0, 10))
	num_2.set(randint(0, 10))

	# Display Numbers
	global multiply_flash
	multiply_flash = Label(multiply_frame, text=str(num_1.get()) + " x " + str(num_2.get()), font=("Helvetica", 50))
	multiply_flash.pack(pady=10)

	# Create Answer Box
	global multiply_answer
	multiply_answer = Entry(multiply_frame)
	multiply_answer.pack(pady=5)

	# Create Answer Button
	global multiply_button
	multiply_button = Button(multiply_frame, text="Answer", command=lambda: multiply_correct(num_1.get(), num_2.get()))
	multiply_button.pack(pady=5)

	# Correct or Incorrect Message
	global multiply_correct_label
	multiply_correct_label = Label(multiply_frame, text="Enter Your Answer Above")
	multiply_correct_label.pack(pady=5)

def divide_correct(num1, num2):
	# Calculate correct answer
	correct = num1 / num2
	rounded_correct = math.ceil(correct * 100) / 100

	# Correct or incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct!")
	output_answer_incorrect.set("Incorrect: " + str(num1) + " / " + str(num2) + " = " + str(rounded_correct))

	if float(divide_answer.get()) == rounded_correct:
		divide_correct_label.config(text=output_answer_correct.get())
	else:
		divide_correct_label.config(text=output_answer_incorrect.get())

	# Clear Answer Box
	divide_answer.delete(0, "end")

	# Generate Two New Random Numbers
	num_1.set(randint(0, 10))
	num_2.set(randint(1, 10))	
	divide_flash.config(text=str(num_1.get()) + " / " + str(num_2.get()), font=("Helvetica", 50))

def divide():
	hide_menu_frames()
	divide_frame.pack(fill="both", expand=1)

	# Create two random numbers
	global num_1
	global num_2
	num_1 = IntVar()
	num_2 = IntVar()
	num_1.set(randint(0, 10))
	num_2.set(randint(1, 10))

	# Display Numbers
	global divide_flash
	divide_flash = Label(divide_frame, text=str(num_1.get()) + " / " + str(num_2.get()), font=("Helvetica", 50))
	divide_flash.pack(pady=10)

	# Create Answer Box
	global divide_answer
	divide_answer = Entry(divide_frame)
	divide_answer.pack(pady=5)

	# Create Answer Button
	global divide_button
	divide_button = Button(divide_frame, text="Answer", command=lambda: divide_correct(num_1.get(), num_2.get()))
	divide_button.pack(pady=5)
	# master.bind('Enter', lambda: add_correct(num_1.get(), num_2.get()))

	# Correct or Incorrect Message
	global divide_correct_label
	divide_correct_label = Label(divide_frame, text="Enter Your Answer Above to the Nearest Hundreth")
	divide_correct_label.pack(pady=5)

def capital_correct(state, cap_correct):
	# Correct or incorrect message
	output_answer_correct = StringVar()
	output_answer_incorrect = StringVar()
	output_answer_correct.set("Correct!")
	output_answer_incorrect.set("Incorrect: You answered " + capital_answer.get() + ",\nbut the capital of " + state + "\n is " + cap_correct)

	if capital_answer.get() == cap_correct:
		capital_correct_label.config(text=output_answer_correct.get())
	else:
		capital_correct_label.config(text=output_answer_incorrect.get())

	# Clear Answer Box
	capital_answer.delete(0, "end")

	# Generate A New Random Capital
	num_1.set(randint(0, 50))
	state = list(state_capitals)[num_1.get()]
	cap = list(state_capitals.values())[num_1.get()]
	capital_flash.config(text="What is the\n capital of\n" + state + "?", font=("Helvetica", 35))
	capital_button.config(text="Answer", command=lambda: capital_correct(state, cap))

def capitals():
	hide_menu_frames()
	capital_frame.pack(fill="both", expand=1)

	# Create one random number to reference dictionary
	global num_1
	num_1 = IntVar()
	num_1.set(randint(0, 50))
	state = list(state_capitals)[num_1.get()]
	cap = list(state_capitals.values())[num_1.get()]

	# Display State
	global capital_flash
	capital_flash = Label(capital_frame, text="What is the\n capital of\n" + state + "?", font=("Helvetica", 35))
	capital_flash.pack(pady=10)

	# Create Answer Box
	global capital_answer
	capital_answer = Entry(capital_frame)
	capital_answer.pack(pady=5)

	# Create Answer Button
	global capital_button
	capital_button = Button(capital_frame, text="Answer", command=lambda: capital_correct(state, cap))
	capital_button.pack(pady=5)

	# Correct or Incorrect Message
	global capital_correct_label
	capital_correct_label = Label(capital_frame, text="Enter Your Answer Above")
	capital_correct_label.pack(pady=5)
	
def hide_menu_frames():
	# Destroy children widgets left over
	for widget in add_frame.winfo_children():
		widget.destroy()
	for widget in subtract_frame.winfo_children():
		widget.destroy()
	for widget in multiply_frame.winfo_children():
		widget.destroy()
	for widget in divide_frame.winfo_children():
		widget.destroy()
	for widget in capital_frame.winfo_children():
		widget.destroy()
	for widget in start_frame.winfo_children():
		widget.destroy()

	# Hide All Frames
	add_frame.pack_forget()
	subtract_frame.pack_forget()
	multiply_frame.pack_forget()
	divide_frame.pack_forget()
	capital_frame.pack_forget()
	start_frame.pack_forget()

# Welcome Screen
def home():
	hide_menu_frames()
	start_frame.pack(fill="both", expand=1)
	start_label = Label(start_frame, text="Welcome to the Flash Card App!", font=("Helvetica", 20)).pack(pady=40)

	# Button Shortcuts
	a_button = Button(start_frame, text="Addition Flash Cards", command=add).pack(pady=5)
	s_button = Button(start_frame, text="Subtraction Flash Cards", command=subtract).pack(pady=5)
	m_button = Button(start_frame, text="Multiplication Flash Cards", command=multiply).pack(pady=5)
	d_button = Button(start_frame, text="Division Flash Cards", command=divide).pack(pady=5)
	c_button = Button(start_frame, text="Capital Flash Cards", command=capitals).pack(pady=5)

# Define Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
main_menu = Menu(my_menu)
my_menu.add_cascade(label="Main Menu", menu=main_menu)
main_menu.add_command(label="Home", command=home)
main_menu.add_command(label="Exit", command=root.quit)
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math Cards", menu=math_menu)
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_command(label="Divide", command=divide)
capital_menu = Menu(my_menu)
my_menu.add_cascade(label="Capital Cards", menu=capital_menu)
capital_menu.add_command(label="U.S. Capitals", command=capitals)

# Create Math Frames
add_frame = Frame(root, width=400, height=400)
subtract_frame = Frame(root, width=400, height=400)
multiply_frame = Frame(root, width=400, height=400)
divide_frame = Frame(root, width=400, height=400)
capital_frame = Frame(root, width=400, height=400)
start_frame = Frame(root, width=400, height=400)

# Show Start Screen
home()


root.mainloop()