import os 


#give the path of the folder from which you want remove all the cache

input_folder = os.getcwd()

# os.walk will travers all the files and folder of the given directory

#root -> means is path of the folder file
#dir -> means all the folders present in the root
#files -> means all the files present in the root path

for root, dirs, files in os.walk(input_folder):
    for file in files:

        *name, extension = str(file).split(".")

        # pickeing the pyc file and removeing the file from the particular folder root path
        if extension == "pyc":
            try :
                file_path = root + f"\{file}"
                path = os.remove(file_path)
            
            except Exception as e:
                pass        