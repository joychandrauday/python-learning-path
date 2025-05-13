# text=open('test.txt')
# print(text.readlines(4))
# with open("test.txt", "w") as file:
#     file.write("Hello, File!")
# print(text.read())

# 1.open(filename, mode)
file = open("example.txt", "w")  # Opens file for writing
# file.write("Hello, World!")
# file.close()

# 2.read
file = open("test.txt", "r")
content = file.read()
print(content)
file.close()

