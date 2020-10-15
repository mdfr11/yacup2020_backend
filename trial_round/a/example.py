j = input().strip()
s = input().strip()
 
result = 0
for char in s:
  if char in j:
  	result += 1
 
print(result)