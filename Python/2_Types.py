# Python data types:
# 1) Numeric
# 2) String
# 3) List -  Mutable or can do any changes.
# 4) Touple -  Same as list data type but immutable.
# 5) Dictionary -  Similar like Hash Map in Java, Denoted by flower braces "{}".


# Datatype: List

# Note - List denoted by square braces "[]".
values = [1, 5, "Rajat", 15]

print (values [0])
print (values[2])
print (values[-1]) # Last index of the list.
print (values[1:4]) # to print continuation index from and to.
values.insert(3, "Rane")
print (values)
values.append(100) # add the value to the end of a array index.
print(values)
values [2] = "RAJAT" # Update perticular index of an array.
print(values)
del values[5]
print(values)