#
# route search function
#

import math
import copy
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

def search_route(now_route, dist_table, play_time):
    ### init_function
    root_route = copy.copy(now_route)
    res_route  = copy.copy(now_route)

    ### search_last_node
    last_node = None
    last_time = 0
    if root_route[-1] != None:
        last_node = root_route[-1][0]
        last_time = root_route[-1][1]
    
    ### debug_output
    # print(root_route)
    # print(last_node,last_time)
    # time.sleep(1)

    ### exit function
    if last_time > play_time:
        # print("[log] over time")
        return res_route

    ### next_route
    for i in range(len(dist_table)):
        now_route = copy.copy(root_route)
        now_route.append([i, root_route[-1][1]+dist_table[i][last_node]])
        now_route = search_route(now_route, dist_table, play_time)

        ### update route
        if len(res_route) < len(now_route):
            res_route = copy.copy(now_route)

    ### 

    return res_route

############################################################

# DFS
def calculation(data, initposition, speed=66.6, playtime=30):
    ### init ffunction
    usetime = 0
    spotnum = len(data)

    ### calculation each pokestop distance 
    dist_table = calc_dist_table(data, speed)
    
    ### search route
    mainroute = search_route([[0,0]], dist_table, playtime)
    
    ### output route
    print("max route len : {0}".format(len(mainroute)))
    print(mainroute)

    ### return route
    return mainroute
