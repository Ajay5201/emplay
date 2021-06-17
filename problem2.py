def swapping(st):
    lst=[]
    lst[:0]=st

    for i in range(len(st)):

        j=i
        while j<len(st)-1:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            j+=2

    return ''.join(lst)

string=input("enter the string:")
print(swapping(string))
