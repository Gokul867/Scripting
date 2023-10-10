import sys as s
from PIL import Image
from pathlib import Path
import re
import os


def convertor(files, new_path):
    for i in range(len(files)):
        img = Image.open(f'{str(files[i])}')

        pattern = re.compile(r"\\[a-z]+\.")
        pattern_obj = pattern.search(str(files[i]))
        pic_name = pattern_obj.group()
        last = len(pic_name) - 1
        pic_name = pic_name[1:last]

        img.save(f"{new_path}/{pic_name}.png", "png")


old_file = s.argv[1]
new_file = s.argv[2]


p = Path(old_file)

list_of_files = list(p.glob('**/*.jpg'))

q = Path(new_file)
print(q.exists())

if (q.exists() == False):
    parent_directory = "D:/Python_Andrei/Projects_udemy/1_scripting"
    path = os.path.join(parent_directory, q)
    os.mkdir(path)

convertor(list_of_files, q)


# Andrei Code:
# import sys
# import os
# from PIL import Image

# path = sys.argv[1]
# directory = sys.argv[2]

# if not os.path.exists(directory):
#     os.makedirs(directory)


# for filename in os.listdir(path):
#   clean_name = os.path.splitext(filename)[0]
#   img = Image.open(f'{path}{filename}')
#   #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
#   img.save(f'{directory}/{clean_name}.png', 'png')
#   print('all done!')
