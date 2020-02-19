import PySimpleGUI as sg

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# layout
		layout = [
			[sg.Text('Time', size=(5, 0)), sg.Input(size=(16, 0))],
			[sg.Button('Ok', size=(7, 0))]
		]
		
		# Window
		window = sg.Window('Sleepy').layout(layout)

		# Take time from the screen:
		self.button, self.values = window.Read()

	def Start(self):
		print(self.values)

screen = PyScreen()
screen.Start()

