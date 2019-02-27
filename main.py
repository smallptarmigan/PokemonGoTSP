#
# PokemonGO_TSP main function
#

import os
import sys
import time
import pprint
import pandas as pd

import search_route as sr
import generate_map as gm

if __name__ == '__main__':
    ### init program and library
    print("[log] Run PokemonGO_TSP")
    start_time = time.time()

    args = sys.argv
    data = None
    disttable = None

    ### args check
    if len(args) < 2:
        print("[log] argument is missing")
        sys.exit()

    ### import data
    if os.path.isfile(args[1]):
        data = pd.read_csv(args[1], sep=',')
    else:
        print("[log] cannot open file : "+str(args[1]))
        sys.exit()

    ### calc route
    route = sr.calculation(data, (0,0), 66, int(args[2]))

    ### output result
    pprint.pprint(route)
    print("[log] Traveling spot num : {0}".format(len(route)))
    gm.gen_map(data, route)

    ### output run time
    end_time = time.time()
    print("[log] Start     Time : {0}".format(start_time))
    print("[log] End       Time : {0}".format(end_time))
    print("[log] Execution Time : {0}".format(end_time-start_time))
