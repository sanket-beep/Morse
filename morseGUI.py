from tkinter import *
import time
from morse_code_advance import decodeBitsAdvanced, decodeMorse, encodeMorse, encode_to_bits

global string
global job

class Operation:
	def __init__(self, instruction, fun):
		self.instruction = instruction
		self.fun = fun
		self.string = ''
		self.job = None

	def generate_morse(self):
		for widget in frame1.winfo_children():
			widget.destroy()
		for widget in frame2.winfo_children():
			widget.destroy()

		self.string = self.string + '0'
		tap_button = Button(frame1, text = "tap", command = lambda: self.tap_one())
		tap_button.grid(row = 3, column = 0, columnspan = 1, pady = 5)
		end_button = Button(frame2, text = "End", command = lambda: self.result())
		end_button.grid(row = 4, column = 1, columnspan = 1, pady = 5)
		self.job = frame1.after(1000, self.generate_morse)

	def result(self):
		if self.job:
			frame1.after_cancel(self.job)
			job = None

		for widget in frame2.winfo_children():
			widget.destroy()
		for widget in frame1.winfo_children():
			widget.destroy()

		result_lbl = Label(frame1, text = self.fun(self.string))
		result_lbl.grid(row = 1, column = 1, columnspan = 2, pady = 5)
		result_lbl1 = Label(frame1, text = self.string)
		result_lbl1.grid(row = 2, column = 1, columnspan = 2, pady = 5)

	def tap_one(self):
		self.string = self.string + '1'

	def entering_input(self):
		for widget in frame1.winfo_children():
			widget.destroy()

		inst_lbl = Label(frame1, text = self.instruction)
		inst_lbl.grid(row = 0, column = 1, columnspan = 2, pady = 5)

		entered_text = StringVar()
		user_entry = Entry(frame1, textvariable = entered_text)
		user_entry.grid(row = 1, column = 1, columnspan = 2, pady = 5)

		convert_button = Button(frame1, text = "Convert", command = lambda: self.translate(entered_text.get()))
		convert_button.grid(row = 2, column = 1, columnspan = 2, pady = 5)

	def translate(self, a):
		for widget in frame2.winfo_children():
			widget.destroy()
		result_lbl = Label(frame2, text = self.fun(a))
		result_lbl.grid(row = 3, column = 1, columnspan = 2, pady = 5)

app = Tk()
app.title("Morse Code Translator")
app.geometry("360x350")

frame1 = Frame(app)
frame1.grid(row = 4, column = 1, columnspan = 2, pady = 5, padx = 4)
frame2 = Frame(app)
frame2.grid(row = 5, column = 1, columnspan = 2, pady = 5, padx = 4)

welcome_lbl = Label(app, text = "Welcome")
welcome_lbl.grid(row = 0, column = 1, columnspan = 2, pady = 5)
inst_lbl = Label(app, text = "Click on any one:")
inst_lbl.grid(row = 1, column = 1, columnspan = 2, pady = 5)

operation1 = Operation("Enter bits to be decoded", decodeBitsAdvanced)
operation2 = Operation("Enter morse to be decoded", decodeMorse)
operation3 = Operation("Enter text to be encoded", encodeMorse)
operation4 = Operation("Enter sequence of dots and dashes", encode_to_bits)
operation5 = Operation("Enter bits to be decoded", decodeBitsAdvanced)

decodebits_btn = Button(app, text = "Decode Bits", command = operation1.entering_input)
decodebits_btn.grid(row = 2, column = 0, pady = 5, padx = 4)
decodemorse_btn = Button(app, text = "Decode Morse", command = operation2.entering_input)
decodemorse_btn.grid(row = 2, column = 1, pady = 5, padx = 4)
encodemorse_btn = Button(app, text = "Encode Text", command = operation3.entering_input)
encodemorse_btn.grid(row = 2, column = 2, pady = 5, padx = 4)
encodebits_btn = Button(app, text = "Encode Morse", command = operation4.entering_input)
encodebits_btn.grid(row = 2, column = 3, pady = 5, padx = 4)
generatebit_btn = Button(app, text = "Generate bits", command = operation5.generate_morse)
generatebit_btn.grid(row = 3, column = 1, columnspan = 2, pady = 5)

app.mainloop()
