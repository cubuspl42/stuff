from numpy import array as vector

dirs = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def entry_duration(dir, len):
	assert dir in dirs
	if dir == 5:
		return len
	elif dir in (1, 3, 7, 9):
		return 1.41 * len / speed
	else:
		return len / speed

def entry_vector(dir, len):
	assert dir in dirs
	mx = dir in (1, 4, 7) and -1 or dir in (3, 6, 9) and 1 or 0
	my = dir in (7, 8, 9) and -1 or dir in (1, 2, 3) and 1 or 0
	return vector(mx * len, my * len);

def position(origin, t, path, speed):
	for i in range(2):
		T = 0
		pos = origin
		for dir, len in path:
			dur = entry_duration(dir, len)
			vec = entry_vector(dir, len)
			if t <= T + dur:
				return pos + (t-T)/dur * vec
			T += dur
			pos += vec
		assert i == 0
		t = t % T

path = [
	(9, 300),
	(5, 75),
	(3, 300),
	(5, 75),
	(2, 500),
	(5, 75),
	(4, 600),
	(5, 75),
	(8, 500),
	(5, 75),
]
