#Joel Wilkins
#02/08
#HLT2(X12)


times=int(input('Please enter a number:\n'))
num=1
for num1 in range (times,times*13, times):
  print(num, 'x', times, '=', num1)
  num=num+1

ans=input('Would you like to enter another number? ')
if ans=='yes':
  times=int(input('Please enter a number:\n'))
  num=1
  for num1 in range (times,times*13, times):
    print(num, 'x', times, '=', num1)
    num=num+1
else:
  print('Thank you')
  
    
    
  

