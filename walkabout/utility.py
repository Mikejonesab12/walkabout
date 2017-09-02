import math
import numpy.random as rand

def random_value(vol):
	return rand.normal(loc=0, scale=vol)

def random_event(prob, vol):
	if rand.rand() > prob:
		return 0
	return rand.normal(scale=vol)

def scale_stdev(number, units):
    return number * math.sqrt(1/units)

def scale_percent(number, units):
    return ((number + 1)**(1/units)) - 1

def absolute_change(value, percent):
    return value * percent

def get_correlated_value(source_a, source_b, corr_coef):
    return ((corr_coef * source_a) + math.sqrt(1 - (corr_coef**2 * source_b)))
