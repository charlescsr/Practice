from statistics import mean
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName,lastName,idNum,scores):
        self.scores=scores

        Person.__init__(self,firstName,lastName,idNum)
    
    def calculate(self):
        if(mean(scores)>=90):
            return 'O'
        elif(mean(scores)>=80 and mean(scores)<90):
            return 'E'
        elif(mean(scores)>=70 and mean(scores)<80):
            return 'A'
        elif(mean(scores)>=55 and mean(scores)<70):
            return 'P'
        elif(mean(scores)>=40 and mean(scores)<55):
            return 'D'
        else:
            return 'T'
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())