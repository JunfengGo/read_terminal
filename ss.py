f=open('New Text Document (2).txt')
label=[]
label2=[]
lines=f.readlines()
for i in range(100):
    if i%2==1:
        num=lines[i][-7:-1]
        label.append(num)
for i in range(100,200):
    if i%2==1:
        num=lines[i][-7:-1]
        label2.append(num)
print(label)
print('#############################################')
print(label2)
with open('c1.txt','w') as f:
    for item in label:
        f.write(item)
        f.write('\n')
with open('c2.txt','w') as f:
    for item in label2:
        f.write(item)
        f.write('\n')






