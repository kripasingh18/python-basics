import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "example.txt")

file = open(file_path, "r")
file.close()
