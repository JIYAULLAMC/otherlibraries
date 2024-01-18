
print("Hello World!")


import os


# curent working directory
present_dir = os.getcwd()

print("present_dir ->: ",present_dir)
import os

directory = os.getcwd()

print(directory)
all_files = os.listdir(directory)
def remove_cache(folder):  
    all_files = os.listdir(directory)      
    for file in all_files:
        print(file)
        fileandfolders = file.split(".")
        print("fileandfolders", fileandfolders)
        if len(fileandfolders)>1 and fileandfolders[-1] == "pyc":
            os.remove(file)

        else:
            remove_cache(file)

remove_cache(directory)
print(all_files)




import os
import shutil


# curent working directory

present_dir = os.getcwd()

present_dir = present_dir + "\__pycache__\\"
print("present_dir ->: ",present_dir, )

files_folders_present_dir = os.listdir(present_dir)
print("files_folders_present_dir", files_folders_present_dir)

for file_folder in files_folders_present_dir:
    print("---------------", file_folder)
    file_with_extension = file_folder.split(".")

    if len(file_with_extension) == 1:
        print("it is a folder", file_folder)
        folder = file_folder

        if folder == "__pycache__":
            try:
                shutil.rmtree(present_dir)
            except FileNotFoundError:
                print("folder is not found !")
    else:
        print("it is a file", file_folder, file_with_extension)
        file = file_folder
        # finding whether the file is cache or not
        if file_with_extension[-1] == "pyc":
            print("cache file", file)
            # removing the cache file
            try:
                os.remove(file)
            except FileNotFoundError as f:
                print("file is not found !")

        else :
            print("non cache file :",file)

