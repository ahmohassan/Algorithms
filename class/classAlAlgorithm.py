class Algorithms:

    # this function calculates the power of any number (N^n,N^n,N^n,N^n)
    #for example (2^4, 8^5, )
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

    # this function calculates the Summetion of n1+n2+n3....
    #for example (1+2+3+4+.........)
    def sumof(n):
        if n==0: 
            return 0
        else:
            return (n*(n+1))/2
    

    #this functions can check if the Letter 
    #is Reapted in the String 
    #For example ("ABCAB") Then result is A
    #Becausse A is reated to 2 times and other Example is
    # ("BTCDT") then result is T
    def compareString(giveMeString):
        counts = {}
        for char in giveMeString:
            if char in counts:
                return char
            counts[char] = 1
        return None