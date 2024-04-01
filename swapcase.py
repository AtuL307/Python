def swap_case(s):
    str = ""
    for i in s:
        if i.isupper():
           str += i.lower() 
        elif i.islower():
           str += i.upper()
        else:
            str += i    
    return str

if __name__ == '__main__':
    swap = swap_case('HackerRank.com presents "Pythonist 2".')
    print(swap)