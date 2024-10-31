f = open("demo.txt", "r")
data = f.read() #if u put read(5), then "I am" will be printed.

print(data)
print(type(data))
f.close()


# line1 = f.readline()
# print(line1)# 1st line will be printed


