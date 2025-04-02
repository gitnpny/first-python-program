#loop is used to repeat a block of code multiple times

#Types of loops:
# for loop
# while loops
# Nested loops


#For Loops with  range

#for loop is used to iterate over sequence(list,str or range,dictionary,tuples)
#for n in range(5):
#    print(n)

#list of characters
#fruit=["banana\napple\norange"]
#for fruit in fruit :
#    print(fruit)
#fruit=["banana","apple","orange"]
#for fruit in fruit :
#    print(fruit)

#STRING
#text = "python"
#for char in text:
#    print(char)

##on dictionary
#person = {"name": "John", "age": 30, "city": "New York"}
#for key, value in person.items():
#    print(f"{key}: {value}")

##nested for loops
#nesting is putting a block of code in another block of code
#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
##]
#
##for row in matrix:
##    for element in row:
##        print(element, end=" ")
##    print()
#


#while loop

#while guess != answer: 
#    if guess < 7 :
#      print("wrong number less than correct")
#      guess =int(input("Guess again: "))
#    elif guess > 7 :
#      print("wrong number greater than correct")
#    guess =int(input("Guess again: "))
#else:
#   guess == 7
#print("guessed right")
#guess =int(input("Guess again: "))



#answer = 7
#guess = int(input("Guess a number : "))
#



#first game using while loops and if statement and elif
#while True: 
#    if guess < 7 :
#      print("wrong number less than correct")
#      guess =int(input("Guess again: "))
#    else: guess > 7 
#    print("wrong number greater than correct")
#    guess =int(input("Guess again: "))
#    if guess == 7:
#     print("guessed right\n",end = "")
#     guess =int(input(" "))
#command= ["start, stop , quit"]
#command.sort()
#start = ("Car Started🚗")
#stop =("Car Stopped🛑🛑")
#quit= ("Exiting the game😥")
#text=("help")
#text=str(input("Enter Command: "))
#
#
#print("start - to start a car\nStop - to stop a car\nQuit - to exit")
#command=str(input("Enter command : "))
#print(f"{start}")
#command=str(input("Enter command : "))
#print(f"{quit}")
#command=str(input("Enter command : "))
#print(F"{stop}")

#command =""# missing module docsring
#
#while True:
#    command = input("Enter a command : ").lower()
#
#    if command == 'quit':
#        print('exiting game')
#        break
#    elif command == 'start':
#        print('car started')
#    elif command == 'stop':
#        print('car stopped')
#    elif command == 'help':
#         #print('start - to start car\n''stop- to stop car\n' 'quit - exit game')
#         print('''
#            start - to start car
#            stop- to stop car
#            quit - exit game
#
#''')
#
#  
#   else:
#    print("invalid")
# 
#n = 10
#while n >=0:
#    print(n)
#    n -= 1