# import glob , os

# print(os.getcwd())

# l = glob.glob('*.py', recursive=True)

# for i, f in enumerate(l):
#     print(f'{i+1}. {f}')

import os

# for root, dirs, files in os.walk("."):
#     for file in files:
#         if (file.endswith(".py")):
#             print(file)
#             # print(os.path.join(root, file))   # print the full path

# root give the subdirectory name
# dirs give the subdirectory name
for root , dirs , files in os.walk("."):
    print(files)