# Walkabout #

Walkabout is a stochastic process simulation framework.

It currently includes Brownian Motion and Geometric Brownian Motion simulators.

In addition, Walkabout provides an easy interface to build your own stochastic process simulations.

## Local Testing and Development

Install the package dependencies.

In the root of the project run `python setup.py install`

## Usage

Walkabout comes with some simulations ready out of the box.

#### Brownian Motion ####

In simple terms, Brownian Motion is just random movements. Previous movements have no effect on the probability of the direction and magnitude of the next random movement.

```
import walkabout

params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.20, 255),
    'starting_value': 15
}

results = walkabout.simulations.brownian_motion(**params)
```
![Brownian Motion Results Graph](https://raw.githubusercontent.com/Mikejonesab12/walkabout/master/examples/images/brownian-motion-results.png)

#### Geometric Brownian Motion ####

Is the Brownian Motion process, but with an added constant drift factor.

```
import walkabout

params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.05, 255),
    'drift': walkabout.utility.scale_percent(0.10, 255),
    'starting_value': 15
}

results = walkabout.simulations.geometric_brownian_motion(**params)
```

![Geometric Brownian Motion Results Graph](https://raw.githubusercontent.com/Mikejonesab12/walkabout/master/examples/images/geometric-brownian-motion-results.png)

#### Additional Notes ####

See `examples/` for complete usage including graphing the results.

To run these examples make sure your working directory is the `examples/` folder and then run `python3 {simulation name}.py` 

### Build your own Simulation


## Todo:

* Add better documentation of features
* Add more types of simulations
* calculate in parallel with threads
* Return statistics about simulations
* Add Tests

## Inspiration

This project was inspired by this [blog post](http://www.turingfinance.com/random-walks-down-wall-street-stochastic-processes-in-python/)