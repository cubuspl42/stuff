from numpy import array as vector
from math import sqrt
from time import sleep

dirs = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# ile czasu trwa dana faza (s)
def phase_duration(dir, len, speed):
	assert dir in dirs
	if dir == 5:
		return len / 1000
	elif dir in (1, 3, 7, 9):
		return sqrt(2) * len / speed
	else:
		return len / speed

# wektor przemieszczenia w danej fazie
def phase_vector(dir, len):
	assert dir in dirs
	mx = dir in (1, 4, 7) and -1 or dir in (3, 6, 9) and 1 or 0
	my = dir in (7, 8, 9) and -1 or dir in (1, 2, 3) and 1 or 0
	return vector((mx * len, my * len));

# pozycja elevatora w danym czasie t
def elevator_position(origin, t, path, speed):
	for i in range(2):
		T = 0
		pos = origin
		for dir, len in path:
			dur = phase_duration(dir, len, speed)
			vec = phase_vector(dir, len)
			if t <= T + dur:
				return pos + (t-T)/dur * vec
			T += dur
			pos += vec
		assert i == 0
		t = t % T

# opis trasy elevatora
# rysujemy domek :)
path = [
	(9, 300),
	(5, 1000),
	(3, 300),
	(5, 1000),
	(2, 250),
	(5, 1000),
	(4, 600),
	(5, 1000),
	(8, 250),
	(5, 1000),
]

origin = (0, 0) # skąd startuje elevator
t = 0 # czas (s)
speed = 300*sqrt(2) # szybkość elevatora (units/s)

while 1:
    print(t, elevator_position(origin, t, path, speed))
    t = t + 0.1
    sleep(0.1)
