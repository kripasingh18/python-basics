import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "output.txt")
print(file_path)
file=open(file_path,"w")
file.write("hello Kripa!!!")
file.close()
