print("Input your string...")

with open("output_file.txt", "w") as file:
    while True:
        user_input = input("\n>> ")
       
        if user_input.upper() == 'Q':
            break
          
        file.write(user_input + '\n')

print("Write process has been finished")

print("Your inputs are below...")

with open("output_file.txt", "r") as file:
    file_contents = file.read()
    print(file_contents)

