def add(de, a, g):
	if de == 0:
		a -= g
		a %= 26
		return a
	else:
		a += g
		a %= 26
		return a
def calc(de, a, v, y):
	if de == 0:
		if v % 2 == 1:
			a -= y
			a %= 26
		else:
			a += y
			a %= 26
	else:
		if v % 2 == 0:
			a -= y
			a %= 26
		else:
			a += y
			a %= 26
	return a
de = int(input("1 for - +, 0 for + -: "))
x = input().lower()
y = int(input("shift ratio: "))
z = len(x)
f = int(input("1 for addition shift, 0 for none: "))
if f == 1:
	g = int(input("addition shift: "))
w = 0
v = 1
word = ""
while z != 0:
	a = ord(x[w])
	if a > 96 and a < 123:
		a -= 97
		if f == 1:
			a = add(de, a, g)
		a = calc(de, a, v, y)
		a += 97
	word += chr(a)
	z -= 1
	w += 1
	v += 1
print(word)
