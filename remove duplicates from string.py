str="sdsfssssfffftabcabcaa"
n=len(str)
i=0
while(i<n):
    j=n-1
    for k in range(j,i,-1):
        if str[i]==str[k]:
            str=str[:k]+str[k+1:]
    n=len(str)
    i+=1
print(str)
TC=>O(n^2)
SC=>O(1)
            OR
print("".join(dict.fromkeys(str)))
