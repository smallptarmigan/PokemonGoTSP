#
# route search function
#

import math

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

def calculation(data, initposition, speed=66.6, playtime=30):
    ### init ffunction
    usetime = 0
    spotnum = len(data)

    ### calculation each pokestop distance 
    dist_table = calc_dist_table(data, speed)
    
    ### search route
    
            
        
