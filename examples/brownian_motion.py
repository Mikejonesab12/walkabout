import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import walkabout


params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.20, from_unit=255, to_unit=1),
    'starting_value': 15
}

results = walkabout.simulations.brownian_motion(**params)

for result in results:
    plt.plot(result)
plt.savefig('brownian-motion-results.png')
plt.show()
