from random import randint


def flip(n, numIterations, hits):
	for i in range(int(n)):
		x = randint(0, div_count - 1)
		if divs[x] == 1:
			hits += 1
			divs[x] = 0
	if hits > (.99 * div_count):
		return (numIterations / 10.0);
	else:
		return flip(n, numIterations+1, hits)


if __name__ == "__main__":
	for attempt in range(10):
		div_count = 0
		n = 100
		hits = 0
		divs = []
		for i in range(n):
			divs.append(1)
			div_count += 1
		time = flip(div_count * .01, numIterations = 0, hits = 0)
		print(time)
