import os
import glob
import shutil
import PyPDF2


#                 TO CHECK IF ENTERED DIRECTORY IS VALID OR NOT
def check_dir():
    direc = input("Enter a valid directory :")

    if os.path.exists(direc):
        return direc
    else:
        check_dir()  # for wrong directory recall to input direcory


# To change working directory according to user input

def select_dir(Dir):
    try:
        os.chdir(Dir)
    except  Exception as e:
        print(e)

# Search for a particular format files

def search_file(file_format):
    l=['rar','jpg','pdf','csv','txt','docx','xlsx']           # we can add more format depend upon us
    search_res = []
    if file_format in l:
        search = os.listdir()

        for i in search:
            if i.endswith(file_format):
                search_res.append(i)
        if len(search_res)==0:
            print("No files with such format available")
        else:
            return search_res
    else:
        print("No such format is in our database")

    return search_res



# User command to Sort,Merge and Move particular Format files

def command(search, file_format, dirc):
    print("Enter Command :\n S for sort \n M for merge \n MV for move \n For exit E")
    comm = input("Enter :")
    l = ['S', 'M', 'MV', 'E']  # list to match command input
    if comm in l:

        if comm == 'S':
            search.sort()  # sort the search result
            print("your files have been sorted: \n", search)

        elif comm == 'M':
            merged_file = merge(file_format, dirc)  # to merge a particular file format
            print("Merged file:", merged_file)

        elif comm == 'MV':
            new_direct = move(file_format, dirc)  # to move a particular file format to new folder
            print("files moved in Directory:", new_direct)

    else:
        print("Enter a valid command")
        command()


# TO merge particular file format into a new one

def merge(file_format, old_dir):
    file_format_list = ['txt', 'csv', 'xlsx']  # to merge txt,csv,xlsx same algorithm can be used
    files_list = glob.glob("*." + file_format)

    if file_format in file_format_list:
        new_file = open("merged." + file_format, 'wb')  # for txt,xlsx,csv
        try:
            for i in files_list:
                data = open(i, 'rb')
                new_file.write(data.read())
            return "merged." + file_format
        except Exception as e:
            print("Exception Error:", e)

    elif file_format.endswith("pdf"):  # to merge pdf files
        merger = PyPDF2.PdfFileMerger()

        try:
            for pdf in files_list:
                merger.append(pdf)

            merger.write("result.pdf")
            merger.close()
        except Exception as e:
            print(e)

        return "result.pdf"


#  to move a particular file format file into another location/directory


def move(file_format, direc):
    file_formats = "\*." + file_format
    files = glob.glob(direc + file_formats)  # list of same kind of format
    new_directory = os.path.join(direc, file_format)  # new directory to move files
    if os.path.isdir(new_directory):  # to check if new directory available or not
        pass
    else:
        os.mkdir(new_directory)  # create a new directory
    for file in files:
        # extract file name form file path
        shutil.move(file, new_directory)  # to move into new directory
        print('Moved:', file)

    return new_directory


####main body###############

print("Kindly enter directory you want to search files")
dirc = check_dir()
select_dir(dirc)
file_format = input("Enter a file format without (.) : for example rar , txt etc :")
search = search_file(file_format)
print(search)
if len(search)>0:
    command(search, file_format, dirc)
print("PROGRAM END:")

