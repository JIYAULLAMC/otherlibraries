import os 

list_files = []    
input_folder = os.getcwd()

for root, dirs, files in os.walk(input_folder):
    for file in files:
        *name, extension = str(file).split(".")
        if extension == "pyc":
            try :
                file_path = root + f"\{file}"
                path = os.remove(file_path)
            
            except Exception as e:
                pass        