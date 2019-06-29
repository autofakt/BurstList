'''
Programmer:
Description: A program to determine the length of bursts of zero’s in a list of N numbers stored in an List. The program should record the length of the bursts of 
zero’s in another List. The program should then print the lengths of the bursts.
Date: 06/28/2019
'''
setMax = 30            # Set the maximum size of burstList
burstList = []
burstLength = []
size = int(input("Enter size of list (N), max is " + str(setMax) + ": ")) 
while(size>setMax or size<1):  #Error checking for bounds
        print("Size is out of bounds, try again.")
        size = int(input("Enter size of list (N), max is 15: "))
for i in range(size):  #Input data loop to burstList
    temp = int(input("Store number in list " + str(i+1) + ": "))
    burstList.append(temp)
print("\nBurstList: ", burstList)

counter = 0            # This loop parses burstList and figures out how many consecutive 0's are present
repeat = False         # then it sends the amounts to the burstLength list
for x in burstList:
    if x ==0 & repeat == True:
        counter +=1
    elif x ==0:
        repeat = True
        counter +=1
    elif repeat == True and x !=0:
        burstLength.append(counter)
        counter = 0
        repeat = False
if counter !=0:  # Needed to appended 0 incase its the last item on the list
    burstLength.append(counter)
print("BurstLength: ",burstLength)

print("\n   RESULTS" + "\nBurst   Length")
counter2 = 1
totalSum = 0
totalZero = 0
'''
for x in burstLength:              # For loop to print results (example)
    print(counter2,"\t",x,"\t")
    totalSum += x
    counter2 += 1
'''
while counter2<=len(burstLength):  # While loop to print results (required for project)
    print(counter2,"\t",burstLength[counter2-1],"\t")
    totalSum += burstLength[counter2-1]
    counter2 += 1
    
average = totalSum/len(burstLength)
print("Average burst length: ", round(average,2))
print("Minimum burst length: ", min(burstLength))
print("Maximum burst length: ", max(burstLength))
print("Total number of zeros: ", sum(burstLength))
