import PySimpleGUI as sg
import subprocess

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# first layout
		default_layout = [
			[sg.Radio('Restart','Time', key='restart'), sg.Radio('Turn off','Time', key='turnoff'), sg.Radio('Timer','Time', key='timer')],
			[sg.Text('Time', size=(5, 0)), sg.Input(size=(10, 0), key='time')],
			[sg.Ok(size=(7, 0)), sg.Cancel(size=(7, 0))],
		]
		
		# Window
		window = sg.Window('Sleepy').layout(default_layout)

		# Take time from the screen:
		self.button, self.values = window.Read()

	def Start(self):
		timer = self.values['timer']
		time = self.values['time']
		# comm_string = f'shutdown -s -t {time}'
		comm_string = 'dir'
		if timer:
			subprocess.run(f'{comm_string}', shell = True)
		print(self.values, timer)

screen = PyScreen()
screen.Start()

