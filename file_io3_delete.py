import os

with open("sample.txt" , "w") as f:
     data = f.write("I am going to office regularly")

os.remove("sample.txt")
