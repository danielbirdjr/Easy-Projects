# rock beats scissors
# paper beats rock
# scissors beats paper

# Rock, Paper, or Scissors (or 'quit' to exit): rock
# Draw
# Computer wins: 0 | Your wins: 0

# Rock, Paper, or Scissors (or 'quit' to exit): rock
# You won!
# Computer wins: 0 | Your wins: 1

# Rock, Paper, or Scissors (or 'quit' to exit): quit
# Exiting the game, goodbye.
import random

user_wins = 0
computer_wins = 0

def play():
  while True:
    user = input("\nRock, Paper, or Scissors (or 'quit' to exit): ").lower()

    if user == 'quit':
      return 'exit'
    
    if user not in ('rock', 'paper', 'scissors'): 
      return "Invalid input. Enter 'rock', 'paper', or 'scissors': "
      continue
    
    computer = random.choice(['rock', 'paper', 'scissors'])

    global user_wins, computer_wins

    if user == computer:
      return 'Draw'
    
    if is_win(user, computer):
      user_wins += 1
      return 'You won!'
    
    if is_win(computer, user):
      computer_wins += 1
      return 'You lost'
    
def is_win(player, opponent):
  if(player == 'rock' and opponent == 'scissors') or \
    (player == 'paper' and opponent == 'rock') or \
    (player == 'scissors' and opponent == 'paper'):

    return True
  
while True: 
  result = play()

  if result == 'exit':
    print('Exiting the game. Goodbye!\n')
    break

  print(result)
  print(f'Your wins: {user_wins} | Computer wins: {computer_wins}')