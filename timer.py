import PySimpleGUI as sg
import subprocess

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# first layout
		default_layout = [
			[sg.Radio('Restart','Time', key='restart'), sg.Radio('Turn off','Time', key='turnoff')],
			[sg.Text('Time', size=(5, 0)), sg.Input(size=(10, 0), key='time')],
			[sg.Ok(size=(7, 0)), sg.Cancel(size=(7, 0))],
		]
		
		# Window
		window = sg.Window('Sleepy').layout(default_layout)

		# Take time from the screen:
		self.button, self.values = window.Read()

	def Start(self):
		restart = self.values['restart']
		turnoff = self.values['turnoff']
		time = self.values['time']
		comm_string = 'dir'
		if restart:
			# comm_string = f'shutdown -r -t {time}'
			subprocess.run(f'{comm_string}', shell = True)
			pass
		if turnoff:
			# comm_string = f'shutdown -s -t {time}'
			subprocess.run(f'{comm_string}', shell = True)
			
		print(self.values)

screen = PyScreen()
screen.Start()

