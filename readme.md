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

```python
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

```python
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

```python
from walkabout import build_simulation, utility, result

@build_simulation
def geometric_brownian_motion(previous_value, drift, volatility, **params):
    volatility_percent_change = utility.random_value(volatility)
    volatility_absolute_change = utility.absolute_change(previous_value, volatility_percent_change)
    drift_absolute_change = utility.absolute_change(previous_value, drift)
    return result(previous_value + volatility_absolute_change + drift_absolute_change)
```

To execute:

```python
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

The data available to your step function is everything you provided in the dictionary that was passed into the original simulation call, plus some dynamic data the simulation provides. This dataset is passed into your step function as a dictionary that you can either access directly or via name function parameters:

```python
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
    print(current_path) // [95, 65, 90, 100]
    print(params['iterations']) // 5
```

A simulation step must end with returning the function `result` with the calculated value for the step passed in.

```python
def cool_step_function(**params):
    ...
    return result(105)
```

You may also want to update a simulation parameter value dynamically in a step of the simulation. To do this, you simply add a dict with the key or keys of parameters you want to change as the second argument to the `result` function:

```python
params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.05, 255),
    'drift': walkabout.utility.scale_percent(0.10, 255),
    'rare_outcome': False,
    'starting_value': 15
}

...

def cool_step_function(previous_value, rare_outcome, volatility, **params):
    ...
    if previous_value > 100:
        rare_outcome = True
    return result(105, {'rare_outcome': rare_outcome, 'volatility': volatility + 0.01})
```

Then in the next simulation step `rare_outcome` will be set as `True` and `volatility` will be incremented by 0.01.

Be careful, if you unintentionally overwrite a parameter like 'steps', bizarre behaviors could occur.

You can also dynamically create new parameters in a simulation step. However, you will be responsible for the defaults and checking if keys exist to avoid errors:

```python
params = {
    'steps': 255,
    'iterations': 5,
    'volatility': walkabout.utility.scale_stdev(0.05, 255),
    'drift': walkabout.utility.scale_percent(0.10, 255),
    'starting_value': 15
}

...

def cool_step_function(previous_value, new_param1 = 0, **params):
    ...
    
    print(new_param1)

    if 'new_param2' in params:
        print(new_param2)

    return result(105, {'new_param1': 1, 'new_param2': 2})
```

### Utility Functions

Walkabout provides a continuously updated list of utility functions to help with building your simulations.



## Todo:

* Add better documentation of features
* Add more types of simulations
* calculate in parallel with threads
* Return statistics about simulations
* Add Tests

## Inspiration

This project was inspired by this [blog post](http://www.turingfinance.com/random-walks-down-wall-street-stochastic-processes-in-python/)