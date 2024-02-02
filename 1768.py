def mergeAlter(str1,str2):
    i = 0 
    j = 0
    res = ""
    while ( i < len(str1)) and (j < len(str2)):
        res = res + str1[i] + str2[j]
        i = i + 1
        j = j + 1
    if i < len(str1):
       res = res + str1[i:]
    elif j < len(str2):
       res = res + str2[j:]
    
    return res


print(mergeAlter("abc","pqr"))


