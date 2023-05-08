import os , glob
# remove all .exe files from the current folder
for i in glob.glob('*.exe'):
    os.remove(i)


# remove all .exe files from the current repository
# import os
# for root, dirs, files in os.walk("."):
#     for file in files:
#         if (file.endswith(".exe")):
#             os.remove(os.path.join(root, file)) 

print('Done')

