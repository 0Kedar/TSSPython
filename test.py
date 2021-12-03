if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(arr)
    m=k=0
    for i in range(n):
        if(l[i]==m): continue
        if(l[i]>m):
            k=m
            m=l[i]
        elif(l[i]>k):
            k=l[i]
        print(m,k)
    print(k)
