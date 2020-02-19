import PySimpleGUI as sg
import subprocess

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# layout
		layout = [
			[sg.Radio('Restart','Time', key='restart'), sg.Radio('Turn off','Time', key='turnoff'), sg.Radio('Timer','Time', key='timer')],
			[sg.Text('Time', size=(5, 0)), sg.Input(size=(16, 0), key='shutdowntime')],
			[sg.Slider(range=(0, 1000), default_value=0, orientation='h', size=(15, 20), key='slider')],
			[sg.Button('Ok', size=(7, 0)), sg.Button('Cancel', size=(7, 0))],
			[sg.Output(size=(20, 2))]
		]
		
		# Window
		self.window = sg.Window('Sleepy').layout(layout)

		# Take time from the screen:

	def Start(self):
		while True:
			self.button, self.values = self.window.Read()
			print(self.values)

screen = PyScreen()
screen.Start()

