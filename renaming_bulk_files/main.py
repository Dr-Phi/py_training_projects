# This can go into a folder and rename all the files to whatever we give it
import os # this allow us to access to our Operating System

def main():
    i = 0
    path = "/home/el_as/Pictures/icons_webdev/" # Our target dir
    for filename in os.listdir(path):
        new_name = "icon" + str(i) + ".png"
        my_source = path + filename
        new_name = path + new_name
        os.rename(my_source, new_name)
        i += 1

if __name__ == "__main__":
    main()
