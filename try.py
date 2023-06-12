import glob , os

for path in glob.glob(f'{os.getcwd()}/Assets/*.mkv', recursive=True):
    print("File Name: ", path.split('\\')[-1])
    print("Path: ", path)