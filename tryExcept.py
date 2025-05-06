try:
    file=open('test.txt')
    print(file.read())
    if file.name=="test.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("error found!")
else:
    print(file.read())
    file.close()
finally:
    print('Final stage of the block!')