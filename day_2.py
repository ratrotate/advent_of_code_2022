def rock_paper_scissors(path):
    first = 0
    second = 0
    
    for string in open(path):
        value = string.split()
#       the first task        
        first, second = value_score_check(value, first, second)
#       the second task
        first, second = value_score_check2(value, first, second)
        print(value, first, second)
    
    return 'The first task:', second, '\nThe second task:', second

def value_score_check(value, first, second):
    print(value)
    if value[0] == 'A':
        first += 1
    elif value[0] == 'B':
        first += 2
    elif value[0] == 'C':
        first += 3

    if value[1] == 'X':
        second += 1
    elif value[1] == 'Y':
        second += 2
    elif value[1] == 'Z':
        second += 3
    
    if ((value[0] == 'A') and (value[1] == 'X')) or ((value[0] == 'B') and (value[1] == 'Y')) or ((value[0] == 'C') and (value[1] == 'Z')):
        first += 3
        second += 3
    if ((value[0] == 'A') and (value[1] == 'Y')) or ((value[0] == 'C') and (value[1] == 'X')) or ((value[0] == 'B') and (value[1] == 'Z')):
        second += 6
    if ((value[0] == 'B') and (value[1] == 'X')) or ((value[0] == 'A') and (value[1] == 'Z')) or ((value[0] == 'C') and (value[1] == 'Y')):
        first += 6
    return first, second

def value_score_check2(value, first, second):
    
    if (value[0] == 'A') and (value[1] == 'Y'):
        first += 4
        second += 4
    if (value[0] == 'B') and (value[1] == 'Y'):
        first += 5
        second += 5
    if (value[0] == 'C') and (value[1] == 'Y'):
        first += 6
        second += 6
    if (value[0] == 'A') and (value[1] == 'X'):
        first += 7
        second += 3
    if (value[0] == 'B') and (value[1] == 'X'):
        first += 8
        second += 1
    if (value[0] == 'C') and (value[1] == 'X'):
        first += 9
        second += 2
    if (value[0] == 'A') and (value[1] == 'Z'):
        first += 1
        second += 8
    if (value[0] == 'B') and (value[1] == 'Z'):
        first += 2
        second += 9
    if (value[0] == 'C') and (value[1] == 'Z'):
        first += 3
        second += 7
    return first, second
