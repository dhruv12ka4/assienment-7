class student:
    
    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def setrollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getrollNumber(self):
        return self.__rollNumber

std = student()

std.setname("Harsh")
print(std.getname())
std.setrollNumber(107)
print(std.getrollNumber())


