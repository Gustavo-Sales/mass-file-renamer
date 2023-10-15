import os


def rename_files(path: str, name: str, extension: str):
    i = 0

    for filename in os.listdir(path):
        my_dest = name + str(i) + extension
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


def main():
    path = str(input("File Path: "))
    name = str(input("File name: "))
    file_extension = str(input("File extension (with '.'): "))

    rename_files(path, name, file_extension)


if __name__ == "__main__":
    main()