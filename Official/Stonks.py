# This is a modlue file being used to craete the stonks functions
# Stonks: take the amnts array and profits variable as input and outputs
# a text file that itemizes the remaining ingredients for the day and 
# the amount of gross profit
import time

amnts = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

profit = 110

timestr = time.strftime("%Y%m%d-%H%M%S")
stonks = open(timestr + '.txt', 'w')
stonks.write("Vodka: " + str(amnts[0]) + '\n')
stonks.write("Gin: " + str(amnts[1]) + '\n')
stonks.write("Rum: " + str(amnts[2]) + '\n')
stonks.write("Tequila: " + str(amnts[3]) + '\n')
stonks.write("Cranberry Juice: " + str(amnts[4]) + '\n')
stonks.write("Lime Juice: " + str(amnts[5]) + '\n')
stonks.write("Lemon Juice: " + str(amnts[6]) + '\n')
stonks.write("Coca Cola: " + str(amnts[7]) + '\n')
stonks.write("Campari: " + str(amnts[8]) + '\n')
stonks.write("Cointreau: " + str(amnts[9]) + '\n')
stonks.write("Grenadine: " + str(amnts[10]) + '\n')
stonks.write("Simple Syrup: " + str(amnts[11]) + '\n')
stonks.write("Tonic Water: " + str(amnts[12]) + '\n')
stonks.write("Dry Vermouth: " + str(amnts[13]) + '\n')
stonks.write("Kahlua: " + str(amnts[14]) + '\n')
stonks.write("Ice: " + str(amnts[15]) + '\n')
stonks.write("\nGross Profit: $" + str(profit))
stonks.close()
