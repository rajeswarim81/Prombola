import random
import numpy as np
import matplotlib.pyplot as plt

# Priority orders
FullHouse = 0  # The ticket with all the 15 numbers marked first.
TopLine = 1  # The ticket with all the numbers of the top row dabbed fastest.
MiddleLine = 2  # The ticket with all the numbers of the middle row dabbed fastest.
BottomLine = 3  # The ticket with the numbers of the bottom row dabbed fasted.
FourCorners = 4 # The ticket with all four corners marked first i.e. 1st and last numbers of top and bottom rows.
EarlyFive = 5 # The ticket with first five number dabbed
gameStateLen = 6
# print(calling_number_sequence)
def call_game(calling_number_sequence, N=10):
    # GAME PARAMETERS
    mu, sigma = 50, 35  # mean and standard deviation
    n = 90  # range of numbers that will be called
    C = 15  # number of cards the caller calls
    R = 10  # number of cards with players
    rowsInTicket = 3  # number of rows in the players' tickets
    columnsInTicket = 9  # number of columns in the players' tickets

    # To define the distribution of tickets,
    # we generate random numbers from a normal distribution with the specified mu and sigma
    # To avoid numbers >100 we take module of the numbers with 100
    # To avoid negative numbers, we take an absolute of their values
    s = np.random.normal(mu, sigma, n)
    ticketNumberDistribution = abs(np.floor(s) % n)


    ##print(ticketNumberDistribution)


    #####insert ticket generating function here
    def getTicket():
        tkt = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

        l = []
        while 1 < 2:
            a = random.randint(1, 89)

            if a not in l:
                if d[int(a / 10)] < 3:
                    l.append(a)
                    d[int(a / 10)] += 1
                    if len(l) == 15:
                        break

        for x in l:
            x1 = int(x / 10)
            while 1 < 2:
                a = random.randint(0, 2)
                if tkt[a][x1] == 0:
                    tkt[a][x1] = x
                    break

        return tkt


    allPlayerTickets = []

    for i in range(N):
        tickets = getTicket()
        allPlayerTickets.append(np.array(tickets))
    # print(allPlayerTickets)

    callerSelectionIndex = np.random.randint(low=1, high=n, size=C)
    callerTickets = np.array(ticketNumberDistribution[callerSelectionIndex])
    # print(callerTickets)


    gameState = {'InGame': '0', 'FullHouse': '1', 'FourCorners': '2', 'BottomLine': '3', 'MiddleLine': '4', 'TopLine': '5',
                 'EarlyFive': '6'}
    playerStates = np.zeros((N,6))
    strategies_winning_turn = [0] * gameStateLen


    def full_house(allPlayerTickets):
        for i in range(N):
            if np.sum(allPlayerTickets[i]) == 0:
                playerStates[i,FullHouse] = 1


    def early_five(allPlayerTickets):
        for i in range(N):
            if np.count_nonzero(allPlayerTickets[i] == 0) == 17:
                playerStates[i,EarlyFive] = 1


    def top_line(allPlayerTickets):
        for i in range(N):
            if np.sum(allPlayerTickets[i][0]) == 0:
                playerStates[i,TopLine] = 1


    def middle_line(allPlayerTickets):
        for i in range(N):
            if np.sum(allPlayerTickets[i][1]) == 0:
                playerStates[i,MiddleLine] = 1


    def bottom_line(allPlayerTickets):
        for i in range(N):
            if np.sum(allPlayerTickets[i][2]) == 0:
                playerStates[i,BottomLine] = 1


    def four_corners(allPlayerTickets):
        for i in range(N):
            if (allPlayerTickets[i][0][0]
                    + allPlayerTickets[i][0][columnsInTicket - 1]
                    + allPlayerTickets[i][rowsInTicket - 1][0]
                    + allPlayerTickets[i][rowsInTicket - 1][columnsInTicket - 1] == 0):
                playerStates[i,FourCorners] = 1


    # TODOOOOOOOOO, fix this shitty code
    def slash_tickets(allPlayerTickets, called_num):
        '''Replaces the called number with 0'''
        for i in range(N):
            allPlayerTickets[i][allPlayerTickets[i] == called_num] = 0
            # for a in range(rowsInTicket):
            #     for b in range(columnsInTicket):
            #         if allPlayerTickets[i][a][b] == called_num:
            #             allPlayerTickets[i][a][b] = 0
            #             break


    def call_numbers():
        pn = 0  # player number
        for turn in range(len(calling_number_sequence)):
            called_number = calling_number_sequence[turn]
            slash_tickets(allPlayerTickets, called_number)  # slashing the called numbers on all tickets
            if strategies_winning_turn[FullHouse] == 0:
                full_house(allPlayerTickets)
                # check if full house is achieved
                if np.any(playerStates[:, FullHouse] == 1):
                    strategies_winning_turn[FullHouse] = turn

            if strategies_winning_turn[BottomLine] == 0:
                bottom_line(allPlayerTickets)
                if np.any(playerStates[:, BottomLine] == 1):
                    strategies_winning_turn[BottomLine] = turn

            if strategies_winning_turn[MiddleLine] == 0:
                middle_line(allPlayerTickets)
                if np.any(playerStates[:, MiddleLine] == 1):
                    strategies_winning_turn[MiddleLine] = turn

            if strategies_winning_turn[TopLine] == 0:
                top_line(allPlayerTickets)
                if np.any(playerStates[:, TopLine] == 1):
                    strategies_winning_turn[TopLine] = turn

            if strategies_winning_turn[FourCorners] == 0:
                four_corners(allPlayerTickets)
                if np.any(playerStates[:, FourCorners] == 1):
                    strategies_winning_turn[FourCorners] = turn

            if strategies_winning_turn[EarlyFive] == 0:
                early_five(allPlayerTickets)
                if np.any(playerStates[:, EarlyFive] == 1):
                    strategies_winning_turn[EarlyFive] = turn

            if set(playerStates[pn])=={1}:
                break

    call_numbers()
    return strategies_winning_turn


def run_sumilations(iterations, players):
    winningTurnDistribution = np.zeros((6, 90)) #six winning strategies and 90 turns
    iters = iterations #simulations = 10^5
    for i in range(iters):
        calling_number_sequence = random.sample(range(1, 91), 90)
        strategies_winning_turn = call_game(calling_number_sequence,players)
        for each in range(len(strategies_winning_turn)):
            winningTurnDistribution[each, strategies_winning_turn[each]] +=1

    expectation = []
    for each in range(6):
        #avg.append(np.average(winningTurnDistribution[each]))
        winningTurnDistribution[each] = winningTurnDistribution[each]/iters
        expectation.append(np.average((np.arange(1,91)), weights=winningTurnDistribution[each]))

    return expectation

winning_expectation = np.zeros((6,100))
for players in range(2,100,10):
   expect = run_sumilations(100,players)
   for i in range(len(expect)):
        winning_expectation[i,players] = expect[i]
print(winning_expectation)
