# Take sb (source number system base), db (destination number system base) and sn (number in source format). Write a function that converts sn to its counterpart in destination number system. Print the value returned.


# Input Format

# Constraints
# 0 < N <= 1000000000
# sb and db <= 10


# Output Format

# Sample Input
# 8
# 2 
# 33
# Sample Output
# 11011
def convert(sb,db,sn):
    decimal=0
    power_sb=1
    while sn>0:
        digit=sn%10
        decimal+=digit*power_sb
        sn//=10
        power_sb*=sb
    result=0
    power_db=1
    while decimal>0:
        digit=decimal%db
        result+=digit*power_db
        decimal//=db
        power_db*=10
    return result
print(convert(8,2,33))