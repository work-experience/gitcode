dis = int(input("How far are you travelling to the nearest mile")
passengers = int(input("How many passengers are with you"))
cost = 3
addcost = (passengers*1.5)
while cost == 0:
	if dis <1 AND passengers == 1:
		print("Your cost is £",cost,)
	elif dis>1:
		cost = ((cost + (2*dis))+addcost)
		print ("Your cost is £",cost,)
	else:
		print("Error please try again")
		
	