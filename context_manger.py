'''
 Class based Context manager
'''

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


with FileManager('demo.txt', '+w') as f:
    f.write('Hello this done by class based')

print(f.closed)



'''
    Function Based Context Manager Using contextlib Library

'''

from contextlib import contextmanager

@contextmanager

def open_file(f):
    resource = open(f,  '+w')
    print('file_open')
    try:
        print("file processed")
        yield resource
    finally:
        print("file closed")
        resource.close()


with open_file('demo.txt') as resource:
        resource.write("Helloo, this is done by function based context managers")
        print("file updated")

