file = open("matter.txt", "rt")
data = file.read()
for letter in data:
    print(letter, end="#")
file.close()
/Users/ronshergill/VSCODE_PROJECTS/file_stuff.py