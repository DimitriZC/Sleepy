import PySimpleGUI as sg
import subprocess

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# first layout
		default_layout = [
			[sg.Radio('Restart','Time', key='restart'), sg.Radio('Turn off','Time', key='turnoff'), sg.Radio('Timer','Time', key='timer')],
			[sg.Ok(size=(7, 0)), sg.Cancel(size=(7, 0))],
		]
		timer_layout = [
			[sg.Text('Time', size=(5, 0)), sg.Input(size=(16, 0), key='shutdowntime')],
			[sg.Slider(range=(0, 1000), default_value=0, orientation='h', size=(15, 20), key='slider')]
		]
		
		# Window
		window = sg.Window('Sleepy').layout(default_layout)

		# Take time from the screen:
		self.button, self.values = window.Read()

	def Start(self):
		timer = self.values['timer']
		print(self.values, timer)

screen = PyScreen()
screen.Start()

