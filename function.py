# basic function #

def print_text(text):
    print(text+" :text from print_text function")
# print_text("hello there")

def add_two_numbers(a,b):
    return a+b
# print(add_two_numbers(2,3))

def add_numbers(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
# print(add_numbers(1,2,3,4))

def showing_info(**details):
    for key,value in details.items():
        print(f"{key}: {value}")
showing_info(Name="Joy Chandra Uday",Age=22,HomeTown="Patuakhali")