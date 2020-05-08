import datetime
import time

#1 Print the time
print("*"*20,"Exercise 1","*"*20)
print(datetime.datetime.now())

print("*"*20)
print("*"*20,"Exercise 2","*"*20)
#2 - Simple stop watch
timeStart = datetime.datetime.now()
print(f"Start Time {timeStart}")
time.sleep(5)
timeEnd = datetime.datetime.now()
print(f"End Time: {timeEnd}")
print(f"Time difference: {timeEnd - timeStart}")

print("*"*20,"Exercise 3","*"*20)
#3 Print the word from the user
value = input("Please type your name: ")
print(f"Hi {value}")


print("*"*20,"Exercise 5","*"*20)
# Exercise 5: Record and Print a List
inputList = []
for i in range(3):
    val = input("Type a number:")
    inputList.append(val)

print(inputList)



# #welcome message
# print("welcome to the nifty stopwatch build on Python")
# #show to user the options to start, stop and reset
# stopWatchRunning = False
# userInput = input("Press 'S' to Start, 'T' to Stop and R to Reset: ")

# if(userInput =="S"):
#     print("Stop watch started")
#     stopWatchRunning = True
# elif(userInput =="T"):
#     print("Stop watch stopped")
# elif(userInput =="R"):
#     print("Stop watch reset")
# else:
#     print ("Not a valid input")
#     userInput = input("Press 'S' to Start, 'T' to Stop and R to Reset: ")    

# if(stopWatchRunning == True):
#     secondInput = "'T' to Stop and R to Reset: "

# while stopWatchRunning == True:
#     print(datetime.datetime.now())
   

# #display counter


# #start
# # now = datetime.datetime.now()
# # print(f"Current time is: {datetime.datetime.now()}")


# #stop


# #reset