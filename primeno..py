##Prime number method 1
n=int(input())
for i  in range(2,n):
    if n%i==0:
        print(f'{n} is Not a Prime Number')
        break
else:
    print('Prime number')



##prime number method 2
n=int(input())
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(f'{n} Not a Prime Number')
        break
else:
    print(f'{n} Prime number')


##prime number method 3
n=int(input())
for i  in range(2,n//2+1):
    if n%i==0:
        print(f'{n} is Not a Prime Number')
        break
else:
    print(f'{n} Prime number')
    
##check numbers prime or not
n1=int(input())
for i  in range(2,n1):
    if n1%i==0:
        print(f'{n1} is Not a Prime Number')
        break
else:
    print(f'{n1} Prime number')
n2=int(input())
for i  in range(2,n2):
    if n%i==0:
        print(f'{n2} is Not a Prime Number')
        break
else:
    print(f'{n2} Prime number')
n3=int(input())
for i  in range(2,n3):
    if n%i==0:
        print(f'{n3} is Not a Prime Number')
        break
else:
    print(f'{n3} Prime number')



#Finding prime  numbers 1 to 20
n=int(input())    
for num in range(1, 21):            
    if num < 2:
        continue            

    is_prime = True                

    for i in range(2, num):        
        if num % i == 0:
            is_prime = False       
            break
    if is_prime:
        print(num, end=' ')     


#Finding prime  numbers 1 to n
n=int(input())    
for num in range(1, n):            
    if num < 2:
        continue            

    is_prime = True                

    for i in range(2, num):        
        if num % i == 0:
            is_prime = False       
            break
    if is_prime:
        print(num, end=' ')     

#Finding next prime number
n=int(input())
next_num=n+1
while True:
    is_prime = True
    for i in range(2, next_num):
        if next_num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Next prime number is:", next_num)
        break
    next_num += 1







    
            
