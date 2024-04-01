if __name__ == "__main__":

    alphanum = input()
    lower = []
    upper = []
    odd = []
    even = []
    if alphanum.isalnum:
        # 1st approach
        """for i in range(len(alphanum)):
            if alphanum[i].islower():
                lower.append(alphanum[i])
            elif alphanum[i].isupper():
                upper.append(alphanum[i])
            elif alphanum[i].isdigit and int(alphanum[i]) % 2 == 0:
                even.append(alphanum[i])
            else:
                odd.append(alphanum[i])
                
    lower.sort()
    upper.sort()
    odd.sort()
    even.sort()

    print("".join(lower + upper + odd + even ))            
    """
        

        # 2st approach
        lower_case = [ i for i in alphanum if i.islower()]
        upper_case = [ i for i in alphanum if i.isupper()]
        digit = [x for x in alphanum if x.isdigit()]
        odd_digit = [ i for i in digit if int(i) % 2 != 0]
        even_digit = [ i for i in digit  if int(i) % 2 == 0]

        j = "".join(sorted(lower_case) + sorted(upper_case) + sorted(odd_digit) + sorted(even_digit) )
        print(j)
    
"""
    input = Sorting1234
    output = gnitorS1324
"""
    
      
