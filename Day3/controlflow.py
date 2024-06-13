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

for client, status in clients.copy().items():
    if status == 'inactive':
        del clients[client]


clients

active_clients = {}
for client,status in clients.items():
    if status == 'active':
        active_clients[client]=status
active_clients



#range() function
for i in range(10):
    print(i)
    

list(range(5,10))

list(range(0,100,9))

x = ['janak','shyam','sushant','kishor']
for i in range(len(x)):
    print(i,x[i])
    
range(10)

sum(range(10))

#4.4. break and continue Statements, and else Clauses on Loops
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n, 'equals', x,'*', n//x)
            break
    else:
        print(n,'is a prime number')
        
        
#4.5. pass Statements

while True:
    pass

class MyEmptyClass:
    pass

#4.6. match Statements

def http_error(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "Not found"
        case 418:
            return "I am a teapot"
        case _:
            return "Something is wrong with the internet"