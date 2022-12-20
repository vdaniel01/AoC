with open("1.txt") as f:
    kaloriak = [x.split("\n") for x in f.read().split("\n\n")]

kaloriak_osszege = []

for kaloria in kaloriak:
    kaloriak_osszege.append(sum(map(lambda x: int(x),  kaloria)))

kaloriak_osszege.sort(reverse=True)

print(f"1. feladat megoldása: {kaloriak_osszege[0]}")
print(f"2. feladat megoldása: {kaloriak_osszege[0]+kaloriak_osszege[1]+kaloriak_osszege[2]}")


"""
for line in open(0):
    if(line =="\n"):
        a.append(0)
        continue
    else:
        a[-1] += int(line)

print(max(a))

while True:
    try:
        x = input()
    except:
        break

    if x == "":
        a.append(0)
        continue
    else:
        a[-1] += int(x)

print(max(a))
"""