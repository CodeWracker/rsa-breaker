e = int(input())
n = int(input())
fi_n = int(input())

#d*e = k*fi_n +1

achou = 0
limite = 0
k = 1
while(achou<1 and limite<1):
    de = k*fi_n +1
    if(de%e == 0):
        achou = 1
        print(de/e)
    if(de>e*fi_n):
        print(str(de)+ ' ' + str(e*fi_n))
        limite = 1
    k = k+1
