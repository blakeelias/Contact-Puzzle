from random import randint


def flip(n):
	hits = 0
	for i in range(int(n)):
		x = randint(0, div_count - 1)
		if divs[x] == 1:
			hits += 1
			divs[x] = 0
	return hits

def iterate(n):
	hits = 0
	numIterations = 0
	while hits <= (.99 * div_count):
		hits += flip(n)
		numIterations += 1
	return (numIterations / 10.0);

if __name__ == "__main__":
	times = []
	for attempt in range(10):
		div_count = 100
		divs = [1] * div_count
		time = iterate(div_count * .01)
		times.append(time)
	print(times)
	print(sum(times) / len(times))
