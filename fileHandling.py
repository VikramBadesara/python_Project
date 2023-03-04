# File handling in python

print(f'''file permissions:-
r	It opens the file to read-only mode. The file pointer exists at the beginning. The file is by default open in this mode if no access mode is passed.
rb	It opens the file to read-only in binary format. The file pointer exists at the beginning of the file.
r+	It opens the file to read and write both. The file pointer exists at the beginning of the file.
rb+	It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.
w	It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name. The file pointer exists at the beginning of the file.
wb	It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists. The file pointer exists at the beginning of the file.
w+	It opens the file to write and read both. It is different from r+ in the sense that it overwrites the previous file if one exists whereas r+ doesn't overwrite the previously written file. It creates a new file if no file exists. The file pointer exists at the beginning of the file.
wb+	It opens the file to write and read both in binary format. The file pointer exists at the beginning of the file.
a	It opens the file in the append mode. The file pointer exists at the end of the previously written file if exists any. It creates a new file if no file exists with the same name.
ab	It opens the file in the append mode in binary format. The pointer exists at the end of the previously written file. It creates a new file in binary format if no file exists with the same name.
a+	It opens a file to append and read both. The file pointer remains at the end of the file if a file exists. It creates a new file if no file exists with the same name.
ab+	It opens a file to append and read both in binary format. The file pointer remains at the end of the file.
x	Open a file only for exclusive creation. If the file already exists, this operation fails.
b	Create a binary file
t	Create and open a file in a text mode\n''')

print(f'Creating a text file - file1.txt')
file1 = open("file1.txt", "w")
file1.write('''This file is written for testing purpose---
This is first line
This is second line
This is third line''')
file1.close()
print(f'file <{file1.name}> created successfully\n')

file1 = open("file1.txt", "r")
print(f'''Reading the file --->
{file1.read()}''')
file1.close()

file1 = open("file1.txt", "rb")
print(f'''Reading the file in binary --->
{file1.read()}''')
file1.close()

file1 = open("file1.txt", "r+")
print(f'Initially the file-pointer is at {file1.tell()}')
print(f'Seeking the pointer at {file1.seek(10)}...')
print(f'Now the file pointer is at {file1.tell()}')
file1.close()




