print("Creating a text file with the write<> method.\n")
print("Reading the newly created file.")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line2\n")
text_file.close()
text_file = open("write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing, end = '')
print("And that would make this third line.")
text_file.close()
print("\n\nCreating a text file with the writelines<> method.\n")
print("Reading the newly created file.")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "this is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()
text_file = open("write_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\n\nPress the enter key to exit.")
