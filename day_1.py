def calorie_counting(path):
    current = 0
    total = 0

    for string in open(path):
        if len(string) > 1:
            current += int(string)
        else:
            if total < current:
                total = current
            current = 0
    return(total)
    
    def calorie_counting2(path):
    top_three = [0 for elem in range(3)]
    current = 0

    for string in open(path):
        if len(string) > 1:
            current += int(string)
        else:
            if current > top_three[0]:
                top_three[0] = current
                top_three.sort()
            current = 0
    return sum(top_three)
