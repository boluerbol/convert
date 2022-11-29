with open("song.txt", "r") as file:
    content = file.read()
    str(content)

song = []

for i in range(len(content)):
    song.append(content[i])
print(song)

res = []

for ele in song:
    res.extend(ord(num) for num in ele)
print("The ascii list is : " + str(res))

l = [ bin(list_item)[2:] for list_item in res ]
print(l)

for j in range(len(l)):
    a = list(l[j])
    for i in range(len(a)):
        if a[i] == '1':
            a[i] = '0'
        else:
            a[i] = '1'
        l[j] = "".join(a)

print(l)

for i in range(len(l)):
    a = int(l[i],2)
    l[i] = a

print(l) 

f = []
for i in range(len(l)):
    f.append(chr(l[i]))

print(f)


the_end = "".join(f)

print("THE TXT IS READY  >>>>>>   ", the_end)