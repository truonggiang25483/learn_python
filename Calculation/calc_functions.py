def factorial(n):
    n = int(n)
    ans = n;
    while n > 1:
        ans = ans * (n-1)
        n -= 1
    return ans

    if n == 0:
        return 1

    if n > 40:
        return "--> This value will not fit!"

    if n < 0:
        return "--> Syntax Error"


def to_roman(n):
    try:
        n = int(n)
    except:
        return "--> Syntax Error"

    if n > 4999:
        return "--> Number out of Range!"
    #Create tuple and dictionary#
    num_breaks = (1000,900,500,400,100,90,50,40,10,9,5,4,1)

    letters = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
        }

    #Start the algorithm#
    result = ""
    for value in num_breaks:
        while n >= value:
            result = result + letters[value]
            n = n - value    
    return result

def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "--> Syntax Error"

def from_binary(n):
    try:
        return int(n,2)
    except:
        return "--> Syntax Error"

        
