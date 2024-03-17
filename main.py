# Jaunel Deans
#September 19, 2023

#Task 1: A program that asks for the user’s name and their favorite animal. The output should be: Hello [name]. Your favorite animal is the [favAni].
name = input("Hello user, what is your name? ")
print("Nice to meet you " + name + ".")
favAni = input(name + ", what is your favorite animal? ")
print("Hello " + name + ". Your favorite animal is the " + favAni +".")

#Task 2: Ask the user to enter a number, then print that number again 3 times.
print()
num = int(input("Hello " + name + ". Please enter a number: "))
print("The number you chose was " , num ,", ", num ,", ", num , ".")

#Task 3: Asks the user to enter 3 test scores as integers. Then print out the average of the numbers.
print()
test1 = int(input('Enter the first test score: '))
test2 = int(input("Enter the second test score: "))
test3 = int(input("Enter the final test score: "))

sumResult = sum([test1 , test2 , test3])

quotientResult = sumResult//3

print("The answer is rounded to the nearest whole number therefore, the average of your test scores " + name , "is" , quotientResult , ".")

#Task 4: Asks the user to enter in 3 words, then prints the words in reverse order.
print()
word1 = input(name + ", can you please enter the first random word? ")
word2 = input("Can you please enter the second random word? ")
word3 = input(name + ", can you please enter the final random word? ")

print("Thank you for your cooperation " + name + ". The words in reverse order is " + word3+", " + word2 +", " + word1+".")

#Task 5: Ask the user to enter two integers. Draw a rectangle on the screen using ASCII art and label the length and width that the user enters. Find the area of the rectangle.
print()
length = int(input("Please enter the length of the rectangle: "))
width = int(input("Please enter the width of the rectangle: "))
area = length * width
print("     ", width)
print(">  _________")
print("> |         |")
print("> |         | " , length)
print("> |_________|")
print(">  Area = " , area)
 
 
