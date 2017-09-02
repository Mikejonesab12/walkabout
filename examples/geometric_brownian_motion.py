import sys
sys.path.append('../')

import walkabout
import matplotlib.pyplot as plt

params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.20,255),
    'drift': walkabout.utility.scale_percent(0.03,255),
    'starting_value': 15
}

results = walkabout.simulations.geometric_brownian_motion(**params)

for result in results:
    plt.plot(result)
plt.show()
