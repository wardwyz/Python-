s1 ='abcdefg'
s2 ='defabcdoabcdeftw'
s3 = '1234a'

def findit(str1,str2):
    count = 0
    length = len(str1)

    for sublen in range(length,0,-1):
        for start in range(0,length-sublen +1):
            substr = str1[start:start + sublen]
            count += 1
            if str2.find(substr) > -1:
                print('count={},substrlen={}'.format(count,sublen))
                return substr

print(findit(s1,s2))
print(findit(s1,s3))