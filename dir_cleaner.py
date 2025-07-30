import os 
import shutil 

# file cleaner and sorter for a directory

print("Sort and Clean Directories")
print("==============================")
target_dir = input("Press Enter for current directory, or enter a different path:  ")
if target_dir == "":
  target_dir = os.getcwd()

os.chdir(target_dir)

files = [file for file in os.listdir() if os.path.isfile(file)] # list files and ignore dirs.
extensions = set()  # a set to collect unique extensions

# extract extension
for file in files:
  if "." in file and not file.startswith("."):
    ext = file.rsplit('.', 1)[1]
    extensions.add(ext)


for ext in extensions:
  os.makedirs(ext, exist_ok=True)

for file in files:
  if "." in file and not file.startswith("."):
    ext = file.rsplit('.', 1)[1]
    if ext in file:
      shutil.move(file, ext)
      print(f"{file} moved to {ext} directory.")

print("===============================================")
print("Done Sorting and Cleannnig Files.")
print("===============================================")
  




