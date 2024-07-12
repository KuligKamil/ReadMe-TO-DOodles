# # for each file in directory get todos
from enum import Enum
from os import listdir, walk, getcwd, path
from typing import Optional

from pydantic import BaseModel
# # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# a = fileno()
# print(a, type(a))

# #!/usr/bin/env python
walk_generator = walk(getcwd())
root_dir_entry = next(walk_generator)  # First entry corresponds to the root dir (passed as an argument)
print(root_dir_entry)

print(root_dir_entry[0])
print(root_dir_entry[1])
print(root_dir_entry[2])


# import pathlib
# print(getcwd())
# a = list(pathlib.Path(getcwd()).glob('*.py'))

# print(a)


for root, dirs, files in walk(getcwd()):
    for file in files:
        if file.endswith('.py'):
            print(dirs)
            # print(dirs)
            fullpath = path.join(root, file)
            print(fullpath)

class Priority(Enum):
   LOW = 'LOW'
   MID = 'MID'
   HIGH = 'HIGH'

class Directory(BaseModel):
  line: int
  file_name: str
  file_fullpath: str

class Task(Directory):
   title: str
   subtitle: Optional[str] = None
   desc: Optional[str] = ''
   priority: Priority = Priority.LOW

fullpath = "models.py"
file_name = "models.py"


with open(fullpath, "r") as file:
  # TODO: run file with black
  lines = file.readlines()
result = []
is_todo, todo_index = False, -1


for index, line in enumerate(lines):
  # print(line)
  # print(result)
  # print(index)

  line = line.lstrip()
  if line != '':
    if "TODO" in line: 
      result.append(Task(title=line, line=index + 1, file_fullpath=fullpath, file_name=file_name))
      # result.append([line]) 
      is_todo = True
      todo_index + 1
    elif is_todo and line[0] == '#':
        # result[todo_index + 1].append(line)
        result[todo_index + 1].desc += line
        
    elif is_todo:
      is_todo, todo_index = False, todo_index + 1
   
print(result)
