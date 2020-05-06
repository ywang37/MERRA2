"""
Created on March 19, 2020

@author: Yi Wang
"""

from mylib.merra2.gc_process import process_merra2_month

#######################
# Start user parameters
#

#month_list = ['201405', '201406', '201407', '201408', '201409']
#month_list = ['201805', '201806', '201807']
#month_list = ['201809']
month_list =['200505']

root_run_dir = '/Dedicated/jwang-data/ywang/soil_NOx/MERRA2_process\
/MERRA2/python/runs'

root_merra2_dir = '/Dedicated/jwang-data/shared_satData/MERRA2/ori'

root_output_dict = {}
root_output_dict['==> 2 x 2.5 output'] = \
        '/Dedicated/jwang-data/GCDATA/GEOS_2x2.5/MERRA2_soil_T'

#
# End user parameters
#####################


for month in month_list:
    process_merra2_month(month, root_run_dir, root_merra2_dir,
            root_output_dict)
