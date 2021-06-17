def binarytodecimal(binary,l,r):
    n=binary[l:r+1]
    print(n)
    decimal=int(n,2)
    print(decimal)
    if decimal %2 ==0:
        return "even"
    else:
        return "odd"

n=int(input("enter the length of the array:"))
arr=[]
for i in range(n):
    val=int(input("index "+str(i)+":"))
    if val==0 or val==1:
        arr.append(val)
    else:
        exit()
binary=''.join(map(str,arr))
L=int(input("Left index:"))
R=int(input("Right index:"))

print(binarytodecimal(binary,L,R))
