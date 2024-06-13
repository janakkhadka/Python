#if elif
x = input("Enter the value of x: ")
x = float(x)  

if x < 0:
    print(f"{x} is a negative number")
elif x == 0:
    print(f"{x} is zero")
else:
    print(f"{x} is positive")
    
    
#for statements
words = ['apple','banana','carrot','grapes','mango']
for w in words:
    print(w,len(w))

clients = {'janak': 'active','bishal':'inactive','kishor':'active','pawan':'active'}
