"""
This module contains all the file related methods

"""

def write_list_to_file(file_list,file):
    with open(file,'w',encoding="utf-8") as f:
        for item in file_list:
            f.write("%s \n" %item)
        f.close()
    return 0
