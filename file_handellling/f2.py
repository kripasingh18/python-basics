import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "input.txt")
print(file_path)
file=open(file_path,"r")
content=file.read()
print(content)
file.close()
