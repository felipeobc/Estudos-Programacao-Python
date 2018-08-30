import os

def rename_photo():
    file_list = os.listdir(r"C:\Users\felipe.oliveira\PycharmProjects\Aulas Udacity\prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"C:\Users\felipe.oliveira\PycharmProjects\Aulas Udacity\prank")


    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)

rename_photo()
