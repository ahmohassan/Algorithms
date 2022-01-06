def main():
    base = int(input("Enter The base number: "))
    pwr = int(input("Enter The power number: "))

    calculate(base,pwr)

def calculate(base,power):

    # if power==0:
    #     return 1
    # elif power % 2==0:
    #     return print(calculate(base*base , power/2))
    # else:
    #     return print( base * calculate(base*base, (power-1)/2))

    if power>=0:
        return print(base**power)
    else:
        return 0

main()