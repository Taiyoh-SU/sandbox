a=int(input("number: "))
b=a
i=0
while a > 1:
    if a % 2:
        a=(3*a)+1
    else:
        a=a/2
    i+=1
print(f"{b}は{i}回で{a}になります。")