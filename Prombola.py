import random
import numpy as np
import sys

#GAME PARAMETERS
mu, sigma = 50, 35 # mean and standard deviation
n=90 #range of numbers that will be called
N=5 #number of player
C=15 #number of cards the caller calls
R=10 #number of cards with players
rowsInTicket=3  #number of rows in the players' tickets
columnsInTicket=9  #number of columns in the players' tickets
     


#To define the distribution of tickets, 
# we generate random numbers from a normal distribution with the specified mu and sigma
# To avoid numbers >100 we take module of the numbers with 100
# To avoid negative numbers, we take an absolute of their values
s = np.random.normal(mu, sigma, n)   
ticketNumberDistribution = abs(np.floor(s)%n)  
print(ticketNumberDistribution)


#####insert ticket generating function here


allPlayerTickets = []

for i in range(N):
    tickets = getTickets()
    allPlayerTickets.append(tickets)
print(allPlayerTickets)


callerSelectionIndex=np.random.randint(low=1, high=n, size=C)
callerTickets = np.array(ticketNumberDistribution[callerSelectionIndex])
print(callerTickets)


number_sequence = random.sample(range(1, 101), 100)
print(number_sequence)



#Priority orders
EarlyFive =6 # The ticket with first five number dabbed
TopLine = 5  # The ticket with all the numbers of the top row dabbed fastest.
MiddleLine = 4#The ticket with all the numbers of the middle row dabbed fastest.
BottomLine = 3 #The ticket with the numbers of the bottom row dabbed fasted.
FourCorners = 2 # The ticket with all four corners marked first i.e. 1st and last numbers of top and bottom rows.
FullHouse = 1 #The ticket with all the 15 numbers marked first.
gameStateLen = 7
gameState = {'InGame' : '0','FullHouse' : '1','FourCorners' : '2','BottomLine' : '3', 'MiddleLine':'4','TopLine':'5','EarlyFive':'6'}
playerStates = [ [0] * gameStateLen for _ in range(N)]



def FullHouse(allPlayerTickets):
    for i in range(N):
        count = 0
        if(sum(allPlayerTickets[i]) == 0):
            playerStates[i][FullHouse] = 1
def EarlyFive(allPlayerTickets):
    for i in range(N):
        if(allPlayerTickets[i].count(0) == 17):
            playerStates[i][EarlyFive] = 1
def TopLine(allPlayerTickets):
    for i in range(N):
        if(sum(allPlayerTickets[i][0]) == 0):
            playerStates[i][TopLine] = 1
def MiddleLine(allPlayerTickets):
    for i in range(N):
        if(sum(allPlayerTickets[i][1]) == 0):
            playerStates[i][MiddleLine] = 1
def BottomLine(allPlayerTickets):
    for i in range(N):
        if(sum(allPlayerTickets[i][2]) == 0):
            playerStates[i][BottomLine] = 1
def FourCorners(allPlayerTickets):
    for i in range(N):
        if(allPlayerTickets[i][0][0] 
           + allPlayerTickets[i][0][columnsInTicket-1] 
           + allPlayerTickets[i][rowsInTicket-1][0] 
           + allPlayerTickets[i][rowsInTicket-1][columnsInTicket-1] == 0):
            playerStates[i][FourCorners] = 1
            
            
            
            
            
#TODOOOOOOOOO, fix this shitty code
def slashTickets(allPlayerTickets, called_num):
    for i in range(N):
            for a in range(rowsInTicket):
                for b in range(columnsInTicket):
                    if allPlayerTickets[i][a][b] == called_num:
                        allPlayerTickets[i][a][b] = 0            
                        
                    
for call_index,call_value in enum(number_sequence):
    
    