import random

user_wins = 0
computer_wins = 0

def play():
  while True:
    user = input("\nRock, Paper, or Scissors (or 'quit' to exit): ").lower()

    if user in ('quit', 'exit', 'end', 'finished', 'finish', 'done'):
      return 'exit'
    
    if user not in ('rock', 'paper', 'scissors'):
      print("Try again, pick 'rock', 'paper', or 'scissors'")
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
      return("You lost!")
 
    
def is_win(player, opponent):
  if(player == 'rock' and opponent == 'scissors') or \
    (player == 'scissors' and opponent == 'paper') or \
    (player == 'paper' and opponent == 'rock'):
    return True

while True: 
  result = play()

  if result == 'exit':
    print("Exiting the game, goodbye.\n")
    break
  
  print(result)
  print(f"Computer wins: {computer_wins} | Your wins: {user_wins}")
