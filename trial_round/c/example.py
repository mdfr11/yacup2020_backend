def main():
  with open('input.txt') as fp:
    points, number_of_cards = [int(num) for num in fp.readline().split()]
    cards = fp.readline().strip().split()

  petya = 0
  vasya = 0
  winner = ''
  for _, number in enumerate(cards):
    if int(number) % 15 != 0:
      if int(number) % 5 == 0:
        vasya += 1
      if int(number) % 3 == 0:
        petya += 1
    if vasya == points and not len(winner):
      winner = 'Vasya'
      break
    if petya == points and not len(winner):
      winner = 'Petya'
      break

  if not len(winner):
    if (vasya == petya): winner = "Draw"
    elif (vasya > petya): winner = "Vasya"
    else: winner = "Petya"
  
  print(winner)

main()