with open("example.text",'r') as file:
    data= file.read()
    print(data)

with open("example.text",'w') as file:
    file.write("I love learning Python")
    
try:
    with open("example.text",'r') as file:
        data= file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")


finally:
    file.close()
    print("File operation done.")
