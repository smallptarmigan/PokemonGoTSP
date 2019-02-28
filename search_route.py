###
### route search function
###

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
    return table

############################################################

def search_route(now_route, dist_table, play_time):
    ### search_last_node
    last_node = None
    last_time = 0
    if now_route[-1] != None:
        last_node = now_route[-1][0]
        last_time = now_route[-1][1]

    ### exit function
    if last_time >= play_time:
        return now_route

    ### init_function
    root_route = copy.copy(now_route)
    res_route  = copy.copy(now_route)

    ###
    reverse_route = list(reversed(root_route))
    node_list = [a[0] for a in reverse_route]

    ### next_route
    for i in range(len(dist_table)):
        sum_walk_time = root_route[-1][1] + dist_table[i][last_node]

        ### visited the spot again
        if i in node_list:
            again_node = node_list.index(last_node)
            if (sum_walk_time - reverse_route[again_node][1]) < 5:
                sum_walk_time = reverse_route[again_node][1] + 5

        ### append next route
        now_route.append([i, sum_walk_time])
        tmp_route = search_route(now_route, dist_table, play_time)

        ### update route
        if len(res_route) < len(tmp_route):
            res_route = copy.copy(tmp_route)

        now_route.pop()

    return res_route

############################################################

# DFS
def calculation(data, initposition, speed=66.6, playtime=30):
    ### calculation each pokestop distance
    dist_table = calc_dist_table(data, speed)

    ### search route
    mainroute = search_route([initposition], dist_table, playtime)

    ### return route
    return mainroute
