"""
This folder shall contains the calls and will be modified on a day to day basis
"""
import work_os
import work_files
mypath="Z:\\ITPO InfoSvcs Team\\13 Active Projects"
res = work_os.list_files_recursively(mypath)
file="files.dat"
work_files.write_list_to_file(res,file)
