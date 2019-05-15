def get_days(days):
    total = ''
    for i in range(1, 8):
        if str(i) in days:
            total += str(i)
        else:
            total += '0'
    return total
