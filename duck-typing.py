class pyCharm:
    
    def execute(self):
        print("compiling")
        print("running")


class Laptop:
    
    def code(self, ide):
        ide.execute()


class Myeditor:
    def execute(self):
        print("spell check")
        print("multiple theme")
        print("compiling")
        print("running")


#ide =pyCharm()
ide=Myeditor()
lap1=Laptop()
lap1.code(ide)