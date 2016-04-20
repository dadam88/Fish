import random, math, operator, itertools

class Fish():
	def __init__(self):
		self.size = random.randrange(1,10)
		self.pos = (random.randrange(0,5),random.randrange(0,5))
		self.detection_radius = 50

	def __str__(self):
		return "{0.pos}, {0.size}".format(self)
	
	def move_fish(self, move):
		'''returns None
		increments position by move
		move should be similiar to (1,1), (0,1)
		'''
		# operator allows addition of tuples using map and outputs
		# as list, we then convert back to tuple
		self.pos = tuple(map(operator.add, self.pos, move))

	def detect_fish(self, school):
		detected = []
		[detected.append(fish) for fish in school if get_distance(self.pos, fish.pos) <= self.detection_radius]
		return detected

	def is_smaller(self, fish):
		return self.size > fish.size

	def is_closest(self, fish):
		return get_distance(self.pos, fish.pos)

def get_distance(origin, destination):
    '''(x,y), (x,y) -> returns float
    Calculates distance from (x,y) to (x,y)
    '''
    x = origin[0] - destination[0]
    y = origin[1] - destination[1]
    return math.sqrt(x*x + y*y)
'''
schools = list()
# outcome , for _ in range(10), ifs
[schools.append(Fish()) for _ in range(100)]

a = Fish()
# test all schools against smaller using map
tmp = map(a.is_smaller, schools)
# filter ones that are smaller
smalls = filter(lambda x: x == True, tmp)
detected_fish = a.detect_fish(schools)

print map(a.is_smaller, detected_fish)

# if all smaller == true, go to shortest distance away
# else run like hell
closet = map(a.is_closest, detected_fish)
print min(closet)


# Kill phase
sorted_by_pos = sorted(schools, key= lambda x: x.pos)
'''
def cleanup(fishes):
	groups = {}
	result = []

	for fish in fishes:
		# creates dictionary with positions attacehd to object
		groups.setdefault(fish.pos, []).append(fish)

	for pos, fish in groups.items():
		top = max(fish, key=lambda x: x.size)
		print top, 'chosen from', ', '.join(str(x) for x in fish)
		result.append(top)

	return result