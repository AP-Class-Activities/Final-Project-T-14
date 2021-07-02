t = open('trash2.txt', mode='r', encoding='utf-8')
u = t.readlines()
t.close()

print(u)

new_u = []
for i in range(0, len(u)):
    if '\n' in u[i]:
        new_u.append(u[i].replace('\n', ''))
        if 'CU' in new_u[i]:
            l_id = new_u[i]
print(l_id)
print(new_u)

newL_id = 'CU00000' + str(int(l_id[2:]) + 1)
new_u.remove(l_id)
new_u.append(newL_id)
print('***************')
print(new_u)

with open('trash2.txt', 'w+') as f:
    for item in new_u:
        f.write("%s\n" % item)
    f.close()