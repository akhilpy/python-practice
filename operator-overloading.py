class student:
    """Operator Over loading Example"""
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b

    def __add__(self, oth):
        """ This is example of Operator overloading in python,
         Here we overloading the (+) opeator using Dunder method __add__()"""
        self.r1=self.a+oth.a
        self.r2=self.b+oth.b
        return self.r1+self.r2

    def __str__(self):
        return '{} {}'.format(self.a, self.b)

    def __repr__(self):
        return '{} {}'.format(self.a, self.b)

s1=student(2,3)
s2=student(4,5)
s3 =s1+s2
print(str(s1))
print(repr(s1))
print(s3)