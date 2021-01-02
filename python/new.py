import os
from fnmatch import fnmatch

root = 'C:\\Users\\ekaterina.morozova\\Desktop\\deeplom\\diploma\\lemmatized_with_stops'
pattern = "*.txt"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print (os.path.join(path, name))
            f = open(os.path.join(path, name), 'r', encoding='utf-8')
            lines = f.read()
            f.close()
            lines=lines.replace("\'", 'i')
            lines=lines.replace("`", 'y')
            f = open(os.path.join(path, name), 'w', encoding='utf-8')
            f.write(lines)
            f.close()