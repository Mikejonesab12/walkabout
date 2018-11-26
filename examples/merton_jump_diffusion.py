import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import walkabout

params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.05, from_unit=255, to_unit=1),
    'drift': walkabout.utility.scale_percent(0.10, from_unit=255, to_unit=1),
    'starting_value': 15,
    'jump_probability': 0.003,
    'jump_average': 0.02,
    'jump_volatility': 0.00001
}

results = walkabout.simulations.merton_jump_diffusion(**params)

for result in results:
    plt.plot(result)
plt.savefig('merton-jump-diffusion-results.png')
plt.show()
