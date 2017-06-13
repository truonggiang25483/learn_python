###Alphabet Game##
#DESC
#Imports
import time

#Control Variable
start = "true"

#Instruction
print("\nINSTRUCTION\n1. When the countdown get to zero type the alphabet\n2. That is the only rule!")
input("Press Enter when ready.")
#While Loop
while start == "true":
    #Input name
    name = input("What is your name?:\n")
    name = name.split(' ')

    #Countdown#
    print("Game Will Start in:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    #StartTime#
    startTime = time.time()

    #Alphabet input#
    alphabet = input("Go! Go! Go! Type in the Alphabet: \n")
    alphabet = alphabet.lower()

    print (alphabet)

    #Validation
    if alphabet == "abcdefghijklmnopqrstuvwxyz":
        #End Time#
        endTime = time.time()
        
        #Score#
        score = endTime - startTime
        score = round(score,1)

        #Output Score#
        print("Congratulation - " + name[0] + "\nYour time was - " + str(score) + "s")
    else:
        print("You made a mistake!")

    #Restart#
    restart = input("Input 'YES' to restart:\n")
    if restart == "YES":
        start = "true"
    else:
        start = "false"
                 
    
