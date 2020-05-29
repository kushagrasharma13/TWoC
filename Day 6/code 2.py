def segregate0and1(arr, n) :
    count = 0 
    for i in range(0, n) : 
        if (arr[i] == 0) : 
            count = count + 1
    for i in range(0, count) : 
        arr[i] = 0
    for i in range(count, n) : 
        arr[i] = 1
        
def print_arr(arr , n) : 
    print( "Array after segregation is ",end = "") 
  
    for i in range(0, n) : 
        print(arr[i] , end = " ")
        
arr =list(map(int,input().split()))
n = len(arr) 
      
segregate0and1(arr, n) 
print_arr(arr, n)

