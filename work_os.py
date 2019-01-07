"""
This python script will contain the following modules to help on a day to day basis

"""
from os import listdir
from os.path import isfile,join
from os import walk
import os

"""
input: path of the directory
output: files are returned in a list

"""
def list_files_in_dir(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
    return onlyfiles

"""
This method prints out all the files recursively in a directory

"""

def list_files_recursively(mypath):
    result=[os.path.join(dp,f) for dp,dn,filenames in os.walk(mypath) for f in filenames]
    return result
