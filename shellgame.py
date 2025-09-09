
def game_rules(): # prints out rules for the game
  print('There are 3 rows of shells.\n')
  print('Row 1 starts with 1 shell. Row 2 starts with 3 shells. Row 3 starts with 5 shells.\n')
  print('Players must take turns removing shells from each row.\n')
  print('The player is only allowed to take shells from one row per move, but is allowed to take as many from that row as they would like.\n')
  print('The player to remove the last shell loses the game.\n')
  print('You are not allowed to remove 0 shells for your turn\n\n')
  input('Press enter to continue. ')
 

def users(): # saves user's names and returns their inputs to the main function
  player_1 = input('Player 1: ').capitalize()
  player_2 = input('Player 2: ').capitalize()
  return [player_1, player_2]

def create_state(): # creates the state of the game by stating the number of shells per row
  return [1, 3, 5]

def print_state(state): #prints the state of the game with the corresponding number of shells in their respective rows

  def printed_numbers(row):
    print('')
    if state[row] == 0:
      print('--------- \n')
    if state[row] == 1:
      print('    o \n')
    if state[row] == 2:
      print('   o o \n')
    if state[row] == 3:
      print('  o o o \n')
    if state[row] == 4:
      print(' o o o o \n')
    if state[row] == 5:
      print('o o o o o \n')
  printed_numbers(0)
  printed_numbers(1)
  printed_numbers(2)

def normalize_row(text): # lowercases and removes all spaces in the player's input then returns that value; denies inputs for rows that do not exist
  t = text.strip().lower()
  if t in ("1", "one"): return 0
  if t in ("2", "two"): return 1
  if t in ("3", "three"): return 2
  return "invalid"

def normalize_quantity(number): # lowercases and removes spaces in the player's input hten returns that value; denies inputs for quantities of shells that do not exist
  t = number.strip().lower()
  if t in ("0", "zero"): return "zero"
  if t in ('1', 'one'): return 1
  if t in ('2', 'two'): return 2
  if t in ('3', 'three'): return 3
  if t in ('4', 'four'): return 4
  if t in ('5', 'five'): return 5
  return 'invalid'

def remove_shell(state, row, quantity): # updates the state of the game given the row and number of shells removed chosen by the player
  current = state[row]
  new = current - quantity
  return new

def validate_row(state, row): # determines if there is a number of shells within the selected row
  if state[row] == 0:
    print('There are no shells in this row.\n Please choose another row.')
    return False
  else: return True

def validate_quantity(state, row, quantity): # determines if there are enough shells within a row to remove the amount input by the player
  if state[row] - quantity < 0:
    print('You are trying to remove too many shells from this row.\n Please try again')
    return False
  else: return True

def switch_player(users, player): # updates whose 'turn' it is in the game
  if player == users[0]: return users[1]
  else: return users[0]

def win_check(state, player, users): # scans the game state to see if there are zero shells left after a turn. if there are zero shells, then the last person to move is announced the loser

  if state[0] == state[1] == state[2] == 0:
    loser = player
    winner = switch_player(users, player)
    print(loser + ', YOU LOSE!')
    print(winner + ' WINS!')
    return True

def main():
  game_rules()
  usernames = users()
  player_1 = usernames[0]
  player_2 = usernames[1]
  current_player = player_1
  state = create_state()

  while True:

    print(current_player + "'s Turn")
    print_state(state)

    raw_row = input('What row would you like to remove shells from? ')
    row = normalize_row(raw_row)

    if row == "invalid":
      print('**INVALID CHOICE')
      continue

    valid = validate_row(state, row)
    if not valid: continue

    raw_quantity =  input('How many shells are you removing? ')
    quantity = normalize_quantity(raw_quantity)

    if quantity == "zero":
      print('YOU MUST MOVE AT LEAST ONE SHELL')
      continue

    if quantity == 'invalid':
      print('**INVALID CHOICE')
      continue

    valid = validate_quantity(state, row, quantity)
    if not valid: continue

    state[row] = remove_shell(state, row, quantity)

    win = win_check(state, current_player, usernames)

    if win: break

    current_player = switch_player(usernames, current_player)

main()