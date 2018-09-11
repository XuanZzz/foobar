def answer(x, y):
	level = x - 1 + y -1
	covered = level * (level + 1) / 2
	return covered+x

print(answer(5,10))