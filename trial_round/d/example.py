def main():
  number_of_commits = int(input().strip())
  low = 1
  while low <= number_of_commits:
    mid = (low + number_of_commits) // 2
    print(mid)
    answer = int(input().strip())
    if answer == 1:
      low = mid + 1
    else:
      number_of_commits = mid - 1
  print('!', low)

main()