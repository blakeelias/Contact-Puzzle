from random import randint


def flip(n, numIterations, hits):
	print("n is", n)
	for i in range(int(n)):
		x = randint(0, div_count - 1)
		if divs[x] == 1:
			hits += 1
			divs[x] = 0
	if hits > (.99 * div_count):
		print('done')
		print(numIterations / 10.0);
	else:
		flip(n, numIterations+1, hits)


if __name__ == "__main__":
	div_count = 0
	n = 100
	hits = 0
	divs = []
	for i in range(n):
		divs.append(1)
		div_count += 1
	flip(div_count * .01, numIterations = 0, hits = 0)
