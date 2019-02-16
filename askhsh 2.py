#input num
num = int(input("Please Give a Number:\n"))
#check to be 2-1000000
while int(num) < 2 or int(num) > 1000000:
    num = int(input("Please Give a Number:\n"))
leftover = num
product = 1
i = 1

while product != num:
  i = i + 1
  power = 0
  while leftover%i == 0:
    leftover = leftover/i
    power = power + 1
  if power > 0:
      print (i , "**" , power)
      product = product*i**product
