import numpy.random as rand

def random_value(vol):
	return rand.normal(loc=0, scale=vol)

def random_event(prob, vol):
	if rand.rand() > prob:
		return 0
	return rand.normal(scale=vol)
