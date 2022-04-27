# This file existed for testing a certain feature out of the main code
amnts = [1, 20, 20, 20, 20, 1, 20, 20, 20, 20, 20, 1, 20, 20, 20, 20]

for idx, val in enumerate(amnts):
    if val <= 2:
        print 'item num: ' + str(idx) + ', ' + str(val)
