n, q = map(int, input().split())
caps = list(map(int, input().split()))
used = [0] * n
next = [n] * n

stack = []
# Find next bowl in case of overflow
for i in range(len(caps) - 1, -1, -1):
    while stack and caps[stack[-1]] <= caps[i]:
        stack.pop()
    if stack:
        next[i] = stack[-1]
    stack.append(i)

skip = list(range(n + 1))

for _ in range(q):
    operation, *other = input().split()
    if operation == "?":
        print(used[int(other[0]) - 1])
    else:
        cur, ad = map(int, other)
        cur -= 1
        orig = cur
        cur = skip[cur]
        stack = [cur]
        while 1:
            if cur == n:
                break
            if used[cur] == caps[cur]:
                cur = skip[max(next[cur], skip[cur])]
                stack.append(cur)
                continue
            rem = min(ad, caps[cur] - used[cur])
            ad -= rem
            used[cur] += rem
            if not ad:
                break
            cur = skip[next[cur]]
            skip[orig] = cur
        for e in stack:
            skip[e] = cur
