with open("input.txt", "r") as file:
    content = file.read()
modified_content = content.upper()
with open("output.txt", "w") as new_file:
    new_file.write(modified_content)
print("File has been read, modified, and written to output.txt ✅")
