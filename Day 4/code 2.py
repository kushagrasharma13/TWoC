ls=int(input("enter the no. of tuples in your list:  "))
sz=int(input("enter the no of elements in each tuple:  "))
l=[]
for i in range(ls):
    print("enter element in tuple", i+1 ,":  ")
    t=[]
    for j in range(sz):
        e=int(input("enter element"+ str(j+1)+":  "))
        t.append(e)
    l.append(tuple(t))
N=int(input("enter Nth index for sort:  "))
print("Original list:  ", l)
l.sort(key=lambda x : x[N])
print("List after sorting tuple by Nth element of tuple : " ,l)

