a=int(input( "Enter a number: "))
b=int(input( "Enter a number: "))
sum_of_even = 0
for i in range(a,b+1):
  if i%2==0:
    sum_of_even += i
print(sum_of_even)