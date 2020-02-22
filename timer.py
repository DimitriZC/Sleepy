import PySimpleGUI as sg
import PyInstaller
import subprocess

class PyScreen():

	sg.theme('LightBrown5')

	def __init__(self):
		# first layout
		default_layout = [
			[sg.Radio('Restart','Time', key='restart'), sg.Radio('Turn off','Time', key='turnoff')],
			# [sg.Text('Time', size=(5, 0)), sg.In(size=(15, 0), key='time')],
			[sg.Slider(range=(0, 3600), key='time', default_value=1800, orientation='h')],
			[sg.Ok(size=(7, 0)), sg.Cancel(size=(7, 0))],
		]
		
		# Window
		window = sg.Window('Sleepy', grab_anywhere=False, no_titlebar=False, finalize=True).layout(default_layout)

		# Take time from the screen:
		self.button, self.values = window.Read()

	def start_windows(self):
		restart = self.values['restart']
		turnoff = self.values['turnoff']
		time = int(self.values['time'])
		comm_string = ' '
		if restart:
			comm_string = f'shutdown -r -t {time}'
			subprocess.run(f'{comm_string}', shell = True)
		if turnoff:
			comm_string = f'shutdown /s /t {time}'
			print(comm_string)
			subprocess.run(f'{comm_string}', shell = True)
			
		print(self.values)


screen = PyScreen() # This will be here to make test easyer
screen.start_windows()
