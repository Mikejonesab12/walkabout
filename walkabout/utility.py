import math
import numpy.random as rand


def random_value(stdev, average = 0):
    return rand.normal(loc=average, scale=stdev)


def random_event(probability=0.5):
    if rand.rand() < probability:
        return True
    return False


def scale_stdev(number, from_unit, to_unit):
    return float(number) * math.sqrt(float(to_unit) / float(from_unit))


def scale_percent(number, from_unit, to_unit):
    return ((float(number) + 1)**(to_unit/float(from_unit))) - 1


def absolute_change(value, percent):
    return float(value) * float(percent)
