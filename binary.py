from functools import reduce

hexbinaer = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E", 
    "15": "F",
    "16": "G"
}
hexbinaer1 = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14, 
    "F": 15,
    "G": 16
}


def binary_ten(n: int) -> int:
    """ returns n in system binary ten.
    n most be from binary two
    >>> binaer_ten(1010)
    10
    """
    return int(str(n), 2)
def binary_two(n: int) -> int:
    """ returns n in binary system two.
    n most be in binary ten and n > 0
    >>> binary_two(10)
    1010
    """
    return bin(n)[2:]
def from_base_10_binaer(s: int, n: int) -> str:
    """ calculat number in system 10 to a
    given new number system.
    constrans s <= 16, s > 1
    n >= 0
    >>> from_base_10_binaer(2, 16)
    10000
    >>> from_base_10_binaer(3, 23)
    212
    >>> from_base_10_binaer(16, 26)
    "1A"
    """
    if 0 <= n and n < s:
        if s >= 10 and n >= 10:
            return hexbinaer[str(n)]
        return str(n)
    return from_base_10_binaer(s, n//s) + hexbinaer[str(n%s)]
def to_base_10_binaer(s: int, n: str) -> int:
    """ calculat number to base 10 from system s
    constrant n is case sensetiv
    n >= 0
    s <= 16, s > 1
    >>> to_base_10_binaer(2, "1000")
    8
    >>> to_base_10_binaer(16, "1A")
    26
    """
    """
    if str(n) == "":
        return 0
    return int(to_base_10_binaer(s, str(n)[1:])) + hexbinaer1[str(n)[0]] * (s ** (int(len(str(n)))-1))
    """
    return str(n) != "" and int(to_base_10_binaer(s, str(n)[1:])) + hexbinaer1[str(n)[0]] * (s ** (int(len(str(n)))-1))
def binaer_plus(s: int, n: str, m: str) -> str:
    """ returns the n plus m in binaer
    constrant n and m are case sensetiv
    n and m >= 0
    s <= 16 and s > 1
    >>> binaer_plus(16, "F", "F")
    30
    """
    num1 = to_base_10_binaer(s, n)
    num2 = to_base_10_binaer(s, m)
    return from_base_10_binaer(s, num1 + num2)
def binaer_minus(s: int, n: str, m: str) -> str:
    """ returns the n plus m in binaer
    constrant n and m are case sensetiv
    n and m >= 0
    n >= m
    s <= 16 and s > 1
    >>> binaer_plus(16, "F", "F")
    0
    >>> binaer_minus(2, "1100", "1000")
    100
    """
    num1 = to_base_10_binaer(s, n)
    num2 = to_base_10_binaer(s, m)
    return from_base_10_binaer(s, num1 - num2)

def twos_complement_ten(n: str) -> int:
    """ returns the twos complement of n.
    n most be in binary two
    >>> twos_complement_ten("1010")
    -6
    >>> twos_complement_ten("010")
    2
    >>> twos_complement_ten("110")
    -2
    """
    negativ = binary_ten(int(n[0] + "0"*(len(n)-1)))
    posativ = binary_ten(int(n[1:]))
    return posativ - negativ
def from_twos_complement(n: int) -> int:
    """ returns n in twos comlement 
    >>> from_twoscomlement(-1)
    11
    >>> from_twoscomlement(-2)
    10
    >>> from_twoscomlement(10)
    01010
    """
    if n < 0: # negativ
        return "1"+f"{binary_two(-n)}"
    else:
        return "0"+f"{binary_two(n)}"
def flydende_decimalpunkt(bit: str, eksponent: int = 3) -> str:
    """ flydende decimalpunkt binaer """
    negatation = bit[0]     # disamol is negativ
    complement = bit[1:eksponent+1] # bit version of eksponent
    mantisse = f"1{bit[1+eksponent:]}"  # diamol number 

    ex1 = to_base_10_binaer(2,complement[1:len(complement)])
    if complement[0] == "1": # negativ eksponent
        ex2 = to_base_10_binaer(2, complement[0]+"0"*(eksponent-1))
        eksponent = ex1 - ex2
    else:                   # pasativ eksponent
        eksponent = ex1
    #print(eksponent)
    if int(eksponent) < 0:  # negativ number move . to the right (smaller number)
        for i in range(eksponent,0):
            if i != -1:
                mantisse = "0"+mantisse
            else:
                if negatation == "1":
                    mantisse = "-0."+mantisse
                else:
                    mantisse = "0."+mantisse
    else:                   # posativ number move . to the left (bigger number)
        mantisse = list(mantisse)
        mantisse.insert(eksponent+1, ".")
        mantisse = reduce(lambda x,y:x+y, mantisse, "")
        if negatation == "1":
            mantisse = "-"+mantisse
    return mantisse
def decimalpoint_binary(decimalpoint: str) -> str:
    """ returns the binary version of a decimalpoint 
    >>> decimalpoint_binary("-0.10110") 
    "11110110" 
    >>> decimalpoint_binary("1.011")
    "00000110"
    """
    num1 = decimalpoint.split(".")[0].replace("-","")
    num2 = decimalpoint.split(".")[1]
    if num1.find("1") != -1:    # eksponenten is posativ or 0
        eks = len(num1)-1
        mantese = num1[1:]
        for x in range(0,4-len(mantese)):
            if x >= len(num2):
                mantese += "0"
            else:
                mantese += num2[x]

        eks = str(binary_two(int(eks)))
        if eks == "1":
            eks = "01"
        elif eks == "0":
            eks = "00"
        eks = "0"+eks   # becouse eksponenten is posativ
    else:                       # eksponenten is negativ
        for idx, x in enumerate(num2):
            if x == "1":
                eks = idx+1
                mantese = num2[idx+1:]
                break
        eks = str(binary_two(4 - int(eks)))
        if eks == "1":
            eks = "01"
        elif eks == "0":
            eks = "00"
        eks = "1"+eks   # becouse eksponenten is negativ
        while len(mantese) < 4: # encase mantese is too short
            mantese += "0"
    if decimalpoint[0] == "-":
        return "1"+eks+mantese
    else:
        return "0"+eks+mantese




#print(from_base_10_binaer(2, 1010010111110001))
#print(from_base_10_binaer(16, 42481))
#print(to_base_10_binaer(2, 1010010111110001))
#print(to_base_10_binaer(2, 11001))
#print(flydende_decimalpunkt("00100110", 3))
#print(binaer_plus(2, 10101111, 1))
#print(binaer_minus(2, 11001, 10000000))
