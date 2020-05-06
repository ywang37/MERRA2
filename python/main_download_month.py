"""
Created on May 05, 2020

@author: Yi Wang
"""

import sys

from mylib.merra2.download import get_tavg1_month

#######################
# Start user parameters
#

# usage:
# python main_download_month.py user password
#
# user password are for MERRA-2 website
#

month_list = ['200506']
#month_list = ['201407', '201408', '201409']
#month_list = ['201605', '201606', '201607']
#month_list = ['201506', '201507', '201508', '201509']

root_data_dir = '/Dedicated/jwang-data/shared_satData/MERRA2/ori'

user      = sys.argv[1]
password  = sys.argv[2]

#
# End user parameters
#####################


for month in month_list:
    get_tavg1_month(month, root_data_dir,
            user=user, password=password)
