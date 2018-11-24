from walkabout import build_simulation, utility, result

@build_simulation
def brownian_motion(previous_value, volatility, **params):
    percent_change = utility.random_value(volatility)
    absolute_change = utility.absolute_change(previous_value, percent_change)
    return result(previous_value + absolute_change)

@build_simulation
def geometric_brownian_motion(previous_value, drift, volatility, **params):
    volatility_percent_change = utility.random_value(volatility)
    volatility_absolute_change = utility.absolute_change(previous_value, volatility_percent_change)
    drift_absolute_change = utility.absolute_change(previous_value, drift)
    return result(previous_value + volatility_absolute_change + drift_absolute_change)