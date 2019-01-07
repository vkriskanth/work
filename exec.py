"""
This folder shall contains the calls and will be modified on a day to day basis
"""
import work_os
import work_files
import work_bigdata
# mypath="Z:\\ITPO InfoSvcs Team\\12 Data Ops"
# res = work_os.list_files_recursively(mypath)
# file="files_data_ops.dat"
# work_files.write_list_to_file(res,file)

work_bigdata.convert_parquet_to_csv('C:\\Users\\kanthkr\\Documents\\tmp\\cuve\\cuve_parq','Z:\\Temporary\\Krishna\\cuve\\cuve_download.dat')
