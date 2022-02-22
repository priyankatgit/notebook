f = open("./context_manager.py")
data = f.read()
f.close()
print(data)

with open("./context_manager.py") as f:
    data = f.read()
    print(data)


class FileManager():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()

# loading a file
with FileManager('test.txt', 'w+') as f:
    data = f.read()
    f.write('Test adad')

