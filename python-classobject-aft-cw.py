def main():
    Problem1()
     #Problem2()
     #Problem3()
    # Problem4()

#Create a function that will print all attributes of the class.
def Problem1():
    class Dog:  # create a class called Dog
        def __init__(self, name = "", breed = "", color = "", gender = ""):
            self.name = self
            self.breed = breed
            self.color = color
            self.gender = gender

    myDog = Dog("Cali", "Shepard", "White", "Female")
    myDog.printAll()
    def printAll(self):
        print(self.name, self.breed, self.color, self.gender)

#Create a function that has a loop that quits with the equal sign.
# If the user doesn't enter the equal sign, ask them to input another string.

def Problem2():
    userInput = input("Enter string")
    while (userInput != "="):
        if type(userInput) == str:
            print("Error. Try again")
        else:
            userInput = int(input("Enter another"))

Problem3():
#In your main file create three Person objects. Change the weight and height of each one.
# Afterwards, print the BMI (body mass index) of each Person. If you don’t know how to
# calculate BMI, look at the code I provided for you.
#Hint: BMI is (weight / (height * height)) x 703.
# Weight is in pounds and height is in inches.
#Extra:Put the three person objects in an array and use a loop to print out their BMIs.
class Person123:
    def __init__(self, weight="", height=""):
        self.weight = weight
        self.height = height


    def __str__(self):
        return(f"The person's  {self.weight}, {self.height}")
    person1 = person1(150,60)
    person2 = person2(175,65)
    person3 = person3(160,55)


print(person1)
print(person2)
print(person3)




    weight = int(input("Enter weight"))
    height = int(input("Enter height"))
    BMI = ((weight / (height * height)) x 703



    def addStringToList(self):
        self.Person1.append(BMI)
        self.Person2.append(BMI)
        self.Person3.append(BMI)








if __name__ == '__main__':
    main()
