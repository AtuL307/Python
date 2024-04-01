if __name__ == '__main__':
    N = int(input())
    my_list = list()
    
    commands = {
        "insert" : lambda a, b: my_list.insert(a,b),
        "append" : lambda a: my_list.append(a),
        "remove" : lambda a: my_list.remove(a),
        "pop": lambda: my_list.pop(),
        "sort": lambda: my_list.sort(),
        "reverse": lambda : my_list.reverse(),
        "print" : lambda : print(my_list)
    }

    for _ in range(N):
        inp = input().split()
        commands[inp[0]](*list(map(int, inp[1:])))



    # using eval()
    """for _ in range(N):
        command, *args = input().split()
    
        if command == 'print':
            print(my_list)
        
        else:
            l = f"my_list.{command}{tuple(map(int, args))}"
            eval(l)"""
        