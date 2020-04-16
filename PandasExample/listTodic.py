def list2dic(lists,keys):
    dicts = {}
    for z in lists:
        k = z[0]
        temp = {}
        for i in range(0, len(keys)):
            temp[keys[i]] = z[i+1]
        dicts[k] = temp
    return dicts