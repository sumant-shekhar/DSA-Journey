def roman_num(x):
    if x < 1 or x > 3999:
        return "Invalid"

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    
    result = ""
    
    for i in range(len(val)):
        while x >= val[i]:
            result += syb[i]
            x -= val[i]
    
    return result


# input
number = int(input("Enter Number (1-3999): "))
print(roman_num(number))