class School:
    def __init__(self, name, city, state):
        self.name = name
        self.state = state
        self.__city = city

    def _privatekey(self):
        s = __city
        print('{}'.format(self.__city))

class Student(School):
    def data(self, sname, std):
        self.sname = sname
        self.std = std
        print('{} {} {} {}'.format(self.name, self.state, self.sname, self.std))    
s = Student('world school', 'pune', 'maharashtra')
s.data('shubham', 8)
s._privatekey()
print(s._School__city)