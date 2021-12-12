# Prombola
*A Probabilistic war of Tambola*

> Prombola is  a game inspired from a very old traditional Indian game called Tambola. It is played with a uniform distribution of natural numbers. We have renovated the game, and done statistical analysis of the winning strategies of the game when played with N-1 other players and this has been designed to be played at fundraiser or charity events to raise money.

## Game Rules

Game Play Rules:
* There’s a Caller in the game, who calls numbers ranging from [1,90] sequentially, not in any order, it is usually randomly.
* There can be N players, no limit on the number of players.
* Each player gets a ticket which is composed of a 3X9 grid, where the cells are meant to be filled with numbers. A ticket, consists of 15 numbers drawn uniformly without repetition from [1,90], and they are scattered over the grid with the given constraints:
  * Every column has at least one number.
  * Every row can have at most 5 numbers
  * Column 1 has values between 1–10 
  * Column 2 has values from 11–20
  * Column 3 has values from 21–30 and so on till column 8 with values from 71–80
  * Column 9 has values from 81–90 
* In every turn, until a player wins, the caller calls out one number. The players who have that number present on their tickets cross it out.
* The player to complete a particular winning strategy wins the reward for that strategy. There’s a strategy priority order among all the strategies, and the rewards are decided accordingly. 

In order to redesign and renovate this game to be played at charity events and fundraisers, we will be analyzing the game for N players and based on the expectations of the game winning probabilities, the rewards for the winner(s) will be set so as to maximize the house advantage.

In this project, we have attempted to observe and understand the patterns of winning based on strategies, number of players and the distribution of sequences using a probabilistic and statistical approach. It is important to simulate the game unbiased to conclude on our observations. This report will discuss what to expect when one is playing to win a particular strategy against many other players. Since the game doesn't involve a human approach to strategizing it, we will look at the probabilistic model of the game. We have strategized the house policies on deciding the game prize money keeping in mind that most of the player money has to be donated to a charity whilst keeping the participating players content as well.

