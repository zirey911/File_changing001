file = open("matter.txt", "rt") # change matter.txt to file name or whatever idc. Sigma
data = file.read() # if you want to read full lines and not like one by one, use file.readline(), it stores all the readded thingies into varible called data
for letter in data:#for loop for cool people
    print(letter) #prints all leters
file.close() # just the close the file yk
