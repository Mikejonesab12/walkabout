# Walkabout #

Walkabout is a stochastic process simulation framework.

It currently includes Brownian Motion and Geometric Brownian Motion simulators.

In addition, Walkabout provides an easy interface to build your own stochastic process simulation.

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

The type of simulation you want may not exist in this package. Walkabout provides an interface to easily create and run your own simulation.

Below is the exact code that was used to build the Geometric Brownian Motion simulation:

```
from walkabout import build_simulation, utility, result

@build_simulation
def geometric_brownian_motion(previous_value, drift, volatility, **params):
    volatility_percent_change = utility.random_value(volatility)
    volatility_absolute_change = utility.absolute_change(previous_value, volatility_percent_change)
    drift_absolute_change = utility.absolute_change(previous_value, drift)
    return result(previous_value + volatility_absolute_change + drift_absolute_change)
```

Then to use:

```
params = {
    'steps': 255,
    'iterations': 5,
    'volatility': utility.scale_stdev(0.05, 255),
    'drift': utility.scale_percent(0.10, 255),
    'starting_value': 15
}

reults = geometric_brownian_motion(**params)
```

You write your simulation from the perspective of a single step in the entire simulation.

The data available to your step function is everything you provided in the dictionary that was passed into the original simulation call, plus some dynamic data the simulation provides. This dataset is passed into your step function as a dictionary that you can either access directly or name function parameters:

```
params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.05, 255),
    'drift': walkabout.utility.scale_percent(0.10, 255),
    'starting_value': 15
}

simulation_data = {
    'previous_value': 100,
    'current_path': [95, 65, 90, 100]
}

@build_simulation
def cool_step_function(current_path, **params):
    print(params['previous_value']) // 100
    print('current_path') // [95, 65, 90, 100]
    print(params['iterations']) // 5
```

A simulation step must end with returning the function `result` with the calculated value for the step passed in.

```
def cool_step_function(**params):
    ...
    return result(105)
```

You may want to persist your own data from simulation step to simulation step. You can do this by passing in a dict as the second param to the `result` function:

```
def cool_step_function(previous_value, rare_outcome=false, **params):
    ...
    if previous_value > 100:
        rare_outcome = True
    return result(105, {'rare_outcome': rare_outcome})
```

Then in the next iteration `rare_outcome` will be reflected as `True`.

With this method, you can overwrite any variable passed into the step function if the same name, like `volatility`, is used. This may be what you want. For example, a complex financial simulation may have stock volatility be dynamic and change throughout the simulation. You could do that by:

```
def cool_step_function(**params):
    ...
    return result(105, {volatility: 0.25})
```

However, this could be done on accident and cause bizarre behaviors.

If you are using a named function parameter, make sure you are setting a default, e.g. `rare_outcome = True`, because on the first step of the simulation it will not be defined and a syntax error will occur. Or you can forgo named function parameters and access from the `**params` function parameter instead.

## Todo:

* Add better documentation of features
* Add more types of simulations
* calculate in parallel with threads
* Return statistics about simulations
* Add Tests

## Inspiration

This project was inspired by this [blog post](http://www.turingfinance.com/random-walks-down-wall-street-stochastic-processes-in-python/)