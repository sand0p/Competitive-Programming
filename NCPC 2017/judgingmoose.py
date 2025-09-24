l, r = map(int, input().split())
mx = max(l, r)

if l + r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l+r}")
else:
    print(f"Odd {2 * mx}")
