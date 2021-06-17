def compute_the_final_single_digit_sum(num):
    if num!=0:
        reminder=num%9
        if reminder==0:
            return 9
        else:
            return reminder
    else:
        return 0

num=int(input("enter the number:"))
print(compute_the_final_single_digit_sum(num))
