# import module
import subprocess

# traverse the software list
Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Data)
# try block
# arrange the string
try:
	for i in range(len(a)):
		print(a.split("\\r\\r\\n")[i])
except IndexError as e:
	print("All Done")
