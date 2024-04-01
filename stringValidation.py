def string_validation(string):
    # 1st approach
    """alpha = "".join(string[i] for i in range(len(string)) if string[i].isalpha())
    digit = "".join(string[i] for i in range(len(string)) if string[i].isdigit())
    lower = "".join(string[i] for i in range(len(string)) if string[i].islower() )
    upper = "".join(string[i] for i in range(len(string)) if string[i].isupper() )
    
    print(string.isalnum(), alpha.isalpha(), digit.isdigit(), lower.islower(), upper.isupper() , sep="\n")
    """
    # 2nd approach
    print(any(char.isalnum() for char in string))
    print(any(char.isalpha() for char in string))
    print(any(char.isdigit() for char in string))
    print(any(char.islower() for char in string))
    print(any(char.isupper() for char in string))
 
if __name__ == '__main__':
    #swap = swap_case('HackerRank.com presents "Pythonist 2".')
    string = input()
    string_validation(string)


