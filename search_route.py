#
# route search function
#

import math
import time

def calc_dist_table(data, speed):
    size  = len(data)
    table = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                dx = (data.iloc[i, 1] - data.iloc[j, 1]) * 110949
                dy = (data.iloc[i, 2] - data.iloc[j, 2]) * 90163
                table[i][j] = math.sqrt(dx * dx + dy * dy) / speed
            if i == j:
                table[i][j] = 5

    return table

############################################################

def search_route(nowroute, dist_table):
    # init function
    mainroute = nowroute
    sunroute  = []
    resroute  = []

    # debug output
    print(mainroute)
    time.sleep(1)

    # last_node
    last = None
    lasttime = 0
    if nowroute[-1] != None:
        last = nowroute[-1][0]
        lasttime = nowroute[-1][1]
    print(lasttime)

    # kokode nukeru
    if lasttime > 10:
        return nowroute

    # next_route
    for i in range(len(dist_table)):
        nowroute = mainroute
        nowroute.append([i, mainroute[-1][1]+dist_table[i][last]])
        temproute = search_route(nowroute, dist_table)

        # update
        if len(resroute) < len(temproute):
            resroute = temproute

        print(resroute)

    return rseroute

############################################################

# DFS
def calculation(data, initposition, speed=66.6, playtime=30):
    ### init ffunction
    usetime = 0
    spotnum = len(data)

    ### calculation each pokestop distance 
    dist_table = calc_dist_table(data, speed)
    
    ### search route
    mainroute = search_route([[0,0]], dist_table)
    
    ### output route
    print("max route len : {0}".format(len(mainroute)))
    print(mainroute)

    ### return route
    return mainroute
