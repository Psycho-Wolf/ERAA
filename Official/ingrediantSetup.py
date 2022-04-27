import pickle

#amnts = {'Vodka':20, 'Gin':20, 'Rum':20, 'Tequila':20, 'Cran':20, 'Lime':20, 'Lemon':20, 'Campari':20, 'Coin':20, 'Gren':20, 'Syrup':20, 'Tonic':20, 'Dry':20, 'Kahlua':20, 'Coke':20}
amnts = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

f = open('ingrAmnt.p', 'wb')
pickle.dump(amnts, f, -1)
f.close()

fAmnts = open('ingrAmnt.p', 'rb')
amnts = pickle.load(fAmnts)
fAmnts.close()
print amnts
