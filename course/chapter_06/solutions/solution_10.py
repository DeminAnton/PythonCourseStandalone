n = int(input())

for i in range(n):
    for j in range(n):
        if(n -2-abs(round(n/2)-i) >n -2-abs(round(n/2)-j)):
            print(n -2-abs(round(n/2)-j),end=" ")
        else:
            print(n -2-abs(round(n/2)-i),end=" ")
    print()


        