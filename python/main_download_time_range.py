"""
Created on May 05, 2020

@author: Yi Wang
"""

import sys

from mylib.merra2.download import get_tavg1_time_range

#######################
# Start user parameters
#

# usage:
# python main_download_time_range.py startDate endDate
#         user password
#
# startDate format: YYYYMMDD
# user password are for MERRA-2 website
#

startDate = sys.argv[1]
endDate   = sys.argv[2]
user      = sys.argv[3]
password  = sys.argv[4]

root_data_dir = '/Dedicated/jwang-data/shared_satData/MERRA2/ori'

#
# End user parameters
#####################




get_tavg1_time_range(startDate, endDate, root_data_dir,
        user=user, password=password)
