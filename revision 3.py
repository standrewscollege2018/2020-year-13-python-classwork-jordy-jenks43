ask = True
count = 0
total = 0
while ask == True:
  n=int(input())
  if n == 0:
    ask = False
  else:
    count += 1
    total += n
print(round(total/count))
