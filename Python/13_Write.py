# Write the line and store all the lines in list.
# Reverse the list.
# Write the list back to the file.
with open('ReadWrite.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('ReadWrite.txt', 'w') as writter:
        for line in reversed(content):
            writter.write(line)