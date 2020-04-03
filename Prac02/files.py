#1st Part
outFile = open("name.txt", "w")
name = input("Please Enter Your Name: ")
print(name, file= outFile)
outFile.close()

#2nd Part
inFile = open("name.txt", "r")
name = inFile.read()
inFile.close()
print("Your name is", name)

#3rd Part
inFile = open("numbers.txt", "r")
num1 = int(inFile.readline())
num2 = int(inFile.readline())
inFile.close()
print(num1 + num2)


#4th Part
inFile = open("numbers.txt", "r")
num = 0
total = 0
for line in inFile:
    num = int(line)
    total = total + num
inFile.close()
print("Total of all the numbers in every line is", total)
