#  Написать функцию, которая используя модуль requests скачивает файл и сохраняет его на файловой системе.
#  Функция имеет два параметра: ссылка на файл и имя на файловой системе.
#  В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория.


# Importing
import requests
import pathlib
import os
from time import sleep


# Creating file for writing
def license_download(url):
    while True:  # If the path is wrong, start anew
        file_is_ready = False  # Flag to check if the file is correct
        path_to_file = f"{pathlib.Path.home()}/LICENSE/"  # Defining default path var
        path_to_file = input(f"""Default path is: {path_to_file}LICENSE.md
Input path for LICENSE.md or leave empty for default: """)  # Asking if the path should be changed
        if path_to_file != "":
            if path_to_file[1] != '/':
                path_to_file += '/'
            yes_or_no = input(f"Your path is: {path_to_file}LICENSE.md. Is it correct? [Y/N]: ")  # Path confirmation
            if yes_or_no == 'n' or yes_or_no == 'N':  # User decided to change the path. Aborting and starting anew
                continue
            elif yes_or_no == 'y' or yes_or_no == 'Y':  # User confirmed the path
                if not os.path.exists(path_to_file):  # Wrong path. Aborting and starting anew
                    print(f"Path does not exists!")
                    sleep(1)  # 1 sec pause
                    continue  # Can be replaced with "break". If so, uncomment "UNCOMMENT THIS" section.
                else:  # The path is correct. Continuing operation
                    print(f"""Path exists!
Creating file...""")
                    sleep(1)  # 1 sec pause
                    pathlib.Path(f"{path_to_file}LICENSE.md").touch()  # Creating empty "LICENSE.md" for further writing
                    print(f"File created!")
                    break
            else:
                print(f"""You answered neither Y or N.
Aborting.""")  # The path was not confirmed correctly. Aborting and starting anew
                continue
        elif path_to_file == "":  # If the path input is empty
            print(f"""Default path chosen!
Creating file...""")
            sleep(1)  # 1 sec pause
            if os.path.exists(path_to_file):  # If all the folders in default path are pre-created
                path_to_file = f"{pathlib.Path.home()}/LICENSE/"
                pathlib.Path(f"{path_to_file}LICENSE.md").touch()
                print(f"File created!")
                break
            elif not os.path.exists(path_to_file):  # If "LICENSE" folder does not exist
                pathlib.Path(f"{pathlib.Path.home()}/LICENSE/").mkdir(parents=True, exist_ok=True)  # Creating "LICENSE" folder
                path_to_file = f"{pathlib.Path.home()}/LICENSE/"  # Defining newly created path
                pathlib.Path(f"{path_to_file}LICENSE.md").touch()  # Creating empty "LICENSE.md" for further writing
                print(f"File created!")
                break

    license_file = open(f"{path_to_file}LICENSE.md", "w")
    r = requests.get(f"{url}")  # Pinging targeted url
    license_file.write(f"{r.text}")  # Scrapping text from targeted url if one is available
    license_file.close()
    file_is_ready = True  # File is being written
    # UNCOMMENT THIS [BEGIN]
    # if not file_is_ready:
    #     print(f"Error: could not write file.")
    # else:
    # UNCOMMENT THIS [END]
    print(f"Text from \"{url}\" was written in file {path_to_file}LICENSE.md succesfully!")  # Confirming operation


url = "https://raw.githubusercontent.com/NickMarkovicz/lessons/main/LICENSE.md"  # Defining "url" var
license_download(url)  # Calling out function for print
