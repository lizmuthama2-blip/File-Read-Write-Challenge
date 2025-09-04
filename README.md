File Read & Write Challenge + Error Handling Lab
This project demonstrates basic file handling in Python, including reading, writing, and error handling.  
It is divided into two parts:
File Read & Write Challenge
This part of the program:
1. Reads the contents of an input file.
2. Modifies the content (in this example, converts all text to uppercase).
3. Writes the modified content into a new output file.

Example flow:
- Input file: input.txt
- Modified output: output.txt
Error Handling Lab
This part of the program:
1. Asks the user to enter a filename.
2. Attempts to read the file.
3. Handles errors gracefully if the file does not exist, cannot be read, or permission is denied.
Errors handled:
FileNotFoundError → The file doesn’t exist.
PermissionError → User doesn’t have access to the file.
Other Exceptions → Any unexpected errors.
How to Run
1. Create a file called input.txt in the same directory as the script.
2. Add some sample text to it.
3. Run the script in Python:

bash
python file_challenge.py
