n=1
for i in range(5,-1,-1):
    print(i*'*'+n*" "+i*'*')
    n+=2
n-=2
for i in range(6):
    print(i*'*'+n*" "+i*'*')
    n-=2
    
