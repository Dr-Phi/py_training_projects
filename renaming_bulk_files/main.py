# This can go into a folder and rename all the files to whatever we give it
import os

def main():
    i = 0
    path = "/home/el_as/Pictures/icons_webdev/"
    for filename in os.listdir(path):
        my_dest = "icon" + str(i) + ".png"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()
