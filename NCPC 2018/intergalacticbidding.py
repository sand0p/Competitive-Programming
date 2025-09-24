n, price = map(int, input().split())
ppl = []
for _ in range(n):
    name, p = input().split()
    ppl.append((int(p), name))

ppl.sort(reverse=1)
check_next = False
check_next_indx = 0
p1 = []
p1_s = 0

for i in range(n):
    k, name = ppl[i]
    if k > price:
        continue
    elif k == price:
        check_next = True
        check_next_indx = i + 1
        p1.append(name)
        p1_s += k
    elif p1_s + k <= price:
        p1.append(name)
        p1_s += k
        
p2 = []
p2_s = 0

if check_next:
    for i in range(check_next_indx, n):
        k, name = ppl[i]
        if p2_s + k <= price:
            p2.append(name)
            p2_s += k

num = 0
if p1_s == price:
    num += len(p1)
if p2_s == price:
    num += len(p2)
    
print(num)

if p1_s == price:
    for e in p1:
        print(e)
if p2_s == price:
    for e in p2:
        print(e)
