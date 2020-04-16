def csv2list(filename):
    lists = []
    f = open('.\\CSV\\Lotto.csv','r')
    while True:
        line = f.readline().rstrip('\n')
        if line:
            line = line.split(',')
            lists.append(line)
        else:
            break
    return lists

accounts = csv2list('.\\CSV\\Lotto.csv')
print(accounts[1])
