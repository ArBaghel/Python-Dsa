def Temperature(Min:int,Max:int,Step:int) ->int:
    for F in range(Min , Max+1 , Step):
        c=5*(F-32)//9
        print (f"farenheit {F} - Celcius {c}",end="")
    return 0
def main():
    Min, Max, Step=map(int,input().split())
    Temperature(Min,Max,Step)
if __name__=="__main__":
    main()