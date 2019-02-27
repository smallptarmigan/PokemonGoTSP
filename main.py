#
# PokemonGO_TSP main function
#

import os
import sys
import time
import pandas as pd

import search_route as sr

if __name__ == '__main__':
    ### init program and library
    print("[log] Run PokemonGO_TSP")
    start_time = time.time()

    args = sys.argv
    data = None
    disttable = None

    ### import data 
    if os.path.isfile(args[1]):
        data = pd.read_csv(args[1], sep=',')
    else:
        print("[log] cannot open file : "+str(args[1]))
        sys.exit()

    ### calc route
    route = sr.calculation(data, (0,0), 66, 10)

    ### output result
    pass
    
    ### output run time
    end_time = time.time()
    print("[log] Start     Time : {0}".format(start_time))
    print("[log] End       Time : {0}".format(end_time))
    print("[log] Execution Time : {0}".format(end_time-start_time))

