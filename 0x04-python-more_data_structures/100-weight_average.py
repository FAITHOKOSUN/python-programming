#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product = 0
    freq = 0
    for score,weight in my_list:
        product += (score * weight)
        freq += weight
    return product/freq    


    #scores = [score * weight for score,weight in my_list]
    #return (sum(scores)/sum([weight for score,weight in my_list]))
