import os
# Remove the all .exe files from the current repository
# add the staged files to the commit and commit the changes with a message
# push the changes to the remote repository

# / message for the commit
commit_message = "Used Virtual Environment for the project \
    and used Jupiter Notebook for the project Documentation"

# add the staged files to the commit
os.system("git add .")
# commit the changes with a message
os.system(f"git commit -m \"{commit_message}\"")
# push the changes to the remote repository
os.system("git push origin master")

print("All changes are commit and pushed to the remote repository\n\n")
