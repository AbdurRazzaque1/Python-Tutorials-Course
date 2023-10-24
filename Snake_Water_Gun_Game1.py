import random
# Gun(g) , Water(w) , Snake(s)"
print("S means Snake\nW means Water\nG means Gun\n")
while (True):
	def gameWin(Comp , You):
		# If two values are equal, declare a tie
		if Comp == You:
			return None
		# Check all possibilities when computer chose g
		elif Comp == 'g':
			if You == 'w':
				return True
			elif You == 's':
				return False
		# Check all possibilities when computer chose w
		elif Comp == 'w':
			if You == 's':
				return True
			elif You == 'g':
				return False
		# Check all possibilities when computer chose s
		elif Comp == 's':
			if You == 'g':
				return True
			elif You == 'w':
				return False
	Comp = ''
	randNo = random.randint(1, 3)
	# Computer will chose random number from 1 to 3
	if randNo == 1:
		Comp = 's'
	elif randNo == 2:
		Comp = 'w'
	elif randNo == 3:
		Comp = 'g'
	You = input("Your turn: ")
	if You not in ['w' , 's' , 'g']:
		print ("\nInvalid choise\n\n")
	else :
		print (f"Computer choose: {Comp}\n")
		a = gameWin(Comp , You)
		if a == None:
			print ('The game is tie\n\n')
		elif a:
			print ('Congratulations! , You win\n\n')
		else:
			print ('Sorry! , You lose\n\n')