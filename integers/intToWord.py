

def intToWord (n):
    str = ""
    while n > 0:
        c = chr(n % 32 + 96)
        if c < "a" or c > "z":
            c = " "
        str += c
        n /= 32
    return str



