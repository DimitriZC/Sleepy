import PySimpleGUI as sg
import subprocess

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# first layout
		default_layout = [
			[sg.Radio('Restart','Time', key='restart'), sg.Radio('Turn off','Time', key='turnoff'), sg.Radio('Timer','Time', key='timer')],
			[sg.Ok(size=(7, 0)), sg.Cancel(size=(7, 0))],
			[sg.Output(size=(30, 20))]
		]
		timer_layout = [
			[sg.Text('Time', size=(5, 0)), sg.Input(size=(16, 0), key='shutdowntime')],
			[sg.Slider(range=(0, 1000), default_value=0, orientation='h', size=(15, 20), key='slider')]
		]
		
		# Window
		self.window = sg.Window('Sleepy').layout(default_layout)

		# Take time from the screen:

	def Start(self):
		while True:
			self.button, self.values = self.window.Read()
			timer = self.values['timer']
			if timer:
				pass
			print(self.values, timer)

screen = PyScreen()
screen.Start()

