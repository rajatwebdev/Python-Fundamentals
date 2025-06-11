# Read all content from text file.
file = open('ReadWrite.txt')
# print(file.read())

#line = file.readline()
#while line !="":
    #print(line)
   # line = file.readline()


# 2nd Method to read lines, type of List method.
for line in file.readlines():
    print(line)




