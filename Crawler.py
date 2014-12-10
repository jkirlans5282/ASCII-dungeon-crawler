import random
import os
class floor:
	def __init__(self, things):    #where things is a 2d array
		self.things=things
	def setFloor(self,newFloor):       #new floor
		del self.things
		self.things=newFloor
	def getThingAt(self,y,x):
		return self.things[y][x] 	   #think about it its correct
	def setThingAt(self,y,x,newThing): #where newThing is a character
		self.things[y][x]=newThing
	def printFloor(self):
		os.system('clear')        #clear previous screen
		for f in self.things:
			string="".join(f) 	  #turn array into string
			print(string)
class enemy:
	def __init__(self, y,x,character):
		self.x=x
		self.y=y
		self.character=character
	def move(self,floor):
		xORy=random.randint(0,1) #determine move x or move y
		distance=random.randint(-1,1)
		if xORy==0:
			if self.x+distance>=1 and self.x+distance<=4:
				if floor[self.y][self.x+distance]==" " or floor[self.y][self.x+distance] in "54321":
					self.x+=distance
					location=[self.x,self.y]
				else:
					location=[self.x,self.y]
			else:
				location=[self.x,self.y]
		else: 
			if self.y+distance>=1 and self.y+distance<=4:
				if floor[self.y+distance][self.x]==" " or floor[self.y+distance][self.x] in "54321":
					self.y+=distance
					location=[self.x, self.y]
				else:
					location=[self.x,self.y] # not the most elegant way to do it but It works, and I'm like 90% sure the if's must be nested rather then using and
			else:
				location=[self.x, self.y]
		return location
class player:
	def __init__(self,y,x,character,playerScore):
		self.alive=True
		self.x=x
		self.y=y
		self.character=character
		self.playerScore=playerScore
	def takeDamage(self):
		temp=int(self.character)
		temp=temp-1
		if temp==-1:
			player.alive=False
			print("you died gaaaammme over")
		temp=str(temp)
		self.character=temp
	def addScore(self):
		self.playerScore+=1
	def moveRight(self):
		self.x+=1
	def moveLeft(self):
		self.x-=1
	def moveUp(self):    #because we're moving locations in the array
		self.y-=1		 #to go up, we go back one element in the array
	def moveDown(self):
		self.y+=1
def generateMap(playerScore, doorLocation, currentFloor): #playerScore will be in floors cleared+enemies killed. doorLocation used for multiple door options both playerscore and doorlocation are not really used yet.
	difficulty=30
	floor00=[ ['+','-','-','-','+'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ',' ',' ',' '],
			  ['|',' ',' ',' ','|'],
			  ['+','-','-','-','+']]

	floor01=[ ['+','-','-','-','+'],
			  ['|',' ',' ',' ','|'],
			  [' ',' ',' ',' ','|'],
			  ['|',' ',' ',' ','|'],
			  ['+','-','-','-','+']]

	floor02=[ ['+','-',' ','-','+'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ',' ',' ',' '],
			  ['|',' ',' ',' ','|'],
			  ['+','-','-','-','+']]

	floor03=[ ['+','-','-','-','+'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ',' ',' ',' '],
			  ['|',' ',' ',' ','|'],
			  ['+','-',' ','-','+']]

	floor04=[ ['+','-','-','-','+'],
			  ['|',' ',' ',' ','|'],
			  [' ',' ',' ',' ',' '],
			  ['|',' ',' ',' ','|'],
			  ['+','-','-','-','+']]

	floor05=[ ['+','-',' ','-','+'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ',' ',' ','|'],
			  ['+','-',' ','-','+']]

	floor06=[ ['+','-',' ','-','+'],
			  ['|',' ',' ',' ','|'],
			  [' ',' ',' ',' ','|'],
			  ['|',' ',' ',' ','|'],
			  ['+','-','-','-','+']]

	floor07=[ ['+','-','-','-','+'],
			  ['|',' ',' ',' ','|'],
			  [' ',' ',' ',' ','|'],
			  ['|',' ',' ',' ','|'],
			  ['+','-',' ','-','+']]

	floor08=[ ['+','-',' ','-','+'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ','-',' ',' '],
			  ['|',' ',' ',' ','|'],
			  ['+','-','-','-','+']]

	floor09=[ ['+','-','-','-','+'],
			  ['|',' ',' ',' ','|'],
			  ['|',' ','|',' ',' '],
			  ['|',' ',' ',' ','|'],
			  ['+','-',' ','-','+']]

	floor10=[ ['+','-','-','-','-','-','+'], 
			  ['|',' ',' ',' ',' ',' ','|'],
			  [' ',' ',' ',' ','E','3','|'],
			  ['|',' ',' ',' ',' ',' ','|'],
			  ['+','-','-','-','-','-','+']]

	floor11=[ ['+','-','-',' ','-','-','+'], 
			  ['|',' ',' ',' ',' ',' ','|'],
			  ['|',' ',' ',' ','E','3','|'],
			  ['|',' ',' ',' ',' ',' ','|'],
			  ['+','-','-','-','-','-','+']]

	floor12=[ ['+','-','-','-','-','-','+'], 
			  ['|',' ',' ',' ',' ',' ','|'],
			  ['|',' ',' ',' ','E','3','|'],
			  ['|',' ',' ',' ',' ',' ','|'],
			  ['+','-','-',' ','-','-','+']]

	floors=[floor01,floor02,floor03,floor04,floor05,floor06,floor07,floor08,floor09]
	availableFloors=[]
	if doorLocation=="top":
		for floor in floors:
			if floor[4][2]==" "and floor != floor04 and floor!=currentFloor: #checks for door at proper coresponding location (y,x)
				availableFloors.append(floor)
			if playerScore>=difficulty:
				availableFloors.append(floor12)
	elif doorLocation=="bottom":
		for floor in floors:
			if floor[0][2]==" " and floor != floor04 and floor!=currentFloor:
				availableFloors.append(floor)
			if playerScore>=difficulty:
				availableFloors.append(floor11)
	elif doorLocation=="right":
		for floor in floors:
			if floor[2][0]==" " and floor != floor05 and floor!=currentFloor: # this should be right?
				availableFloors.append(floor)
			if playerScore>=difficulty:
				availableFloors.append(floor10) # they must have traveled through/beaten a total of 25 enemies/rooms
	elif doorLocation=="left":
		for floor in floors:
			if floor[2][4]==" "and floor != floor05 and floor!=currentFloor:
				availableFloors.append(floor)
	x=random.randint(0,len(availableFloors)-1)
	return availableFloors[x]
floor00=[ ['+','-','-','-','+'],
		  ['|',' ',' ',' ','|'],
		  ['|',' ',' ',' ',' '],
		  ['|',' ',' ',' ','|'],
		  ['+','-','-','-','+']]
floor=floor(floor00)
player=player(1,1,'5',0)
enemy=enemy(2,2,'@')
floor.setThingAt(player.y,player.x,player.character)
print("welcome to zampanos castle, it randomly shifts and warps the space around you try and find the treasure hidden inside.")
x=input("hit any button to begin")
while player.alive:
	floor.printFloor()
	print("SCORE: {0}".format(player.playerScore))
	if player.x+1<len(floor.things[0]) and floor.getThingAt(player.y,player.x+1)=='E':
		print("you won the game by finding the treasure!")
		break
	keyStroke=input("wasd to move ijkl to attack, you can only attack when an enemy is nearby: ")
	floor.setThingAt(player.y,player.x,' ')
	if keyStroke=='w':
		if player.y-1>=0:
			if floor.getThingAt(player.y-1,player.x)==" " or floor.getThingAt(player.y-1, player.x)=="@":
				player.moveUp()
				move=True
	elif keyStroke=='s':
		if player.y+1<=4:
			if floor.getThingAt(player.y+1,player.x)==" "or floor.getThingAt(player.y+1, player.x)=="@":
				player.moveDown()
				move=True
	elif keyStroke=='a':
		if player.x-1>=0:
			if floor.getThingAt(player.y,player.x-1)==" "or floor.getThingAt(player.y, player.x-1)=="@":
				player.moveLeft()
				move=True
	elif keyStroke=='d':
		if player.x+1<=len(floor.things[0])-1:
			if floor.getThingAt(player.y,player.x+1)==" "or floor.getThingAt(player.y, player.x+1)=="@":
				player.moveRight()
				move=True
	else:
		move=False
	if keyStroke=='i':
		if player.y-1>=0:
			if floor.getThingAt(player.y-1,player.x)=="@":
				enemy.character=" "
				player.addScore()
				player.addScore()
	elif keyStroke=='k':
		if player.y+1<=5:
			if floor.getThingAt(player.y+1,player.x)=="@":
				enemy.character=" "
				player.addScore()
				player.addScore()
	elif keyStroke=='l':
		if player.x+1>=0:
			if floor.getThingAt(player.y,player.x+1)=="@":
				enemy.character=" "
				player.addScore()
				player.addScore()
	elif keyStroke=='j':
		if player.x-1>=0:
			if floor.getThingAt(player.y,player.x-1)=="@":
				enemy.character=" "
				player.addScore()
				player.addScore()
	if player.x==2 and player.y==0 and move: #move var prevents floor from auto jumping if the player does not move out of the door space, with it, the player must move out of the door and back into it
		floor.setFloor(generateMap(player.playerScore,"top",floor.things)) #returns the new floor
		player.x=2
		player.y=4
		player.addScore()
		enemy.character="@"	
	elif player.x==4 and player.y==2 and move:
		floor.setFloor(generateMap(player.playerScore,"right",floor.things))
		player.x=0
		player.y=2
		player.addScore()
		enemy.character="@"
	elif player.x==0 and player.y==2 and move:
		floor.setFloor(generateMap(player.playerScore,"left",floor.things))
		player.x=4
		player.y=2
		player.addScore()
		enemy.character="@"
	elif player.x==2 and player.y==4 and move:
		floor.setFloor(generateMap(player.playerScore,"bottom",floor.things))
		player.x=2
		player.y=0
		player.addScore()
		enemy.character="@"
	if enemy.character != " ":
		floor.setThingAt(enemy.y, enemy.x," ")
		enemy.move(floor.things)
		floor.setThingAt(enemy.y,enemy.x,enemy.character)
	else:
		floor.setThingAt(enemy.y,enemy.x, " ")
	if enemy.y==player.y and enemy.x==player.x and enemy.character!=" ":
		player.takeDamage()
	floor.setThingAt(player.y,player.x,player.character)