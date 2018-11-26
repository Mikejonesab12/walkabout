from walkabout import build_simulation, utility, result


@build_simulation
def brownian_motion(previous_value, volatility, **params):
    percent_change = utility.random_value(volatility)
    absolute_change = utility.absolute_change(previous_value, percent_change)
    return result(previous_value + absolute_change)


@build_simulation
def geometric_brownian_motion(previous_value, drift, volatility, **params):
    returns_percent_change = utility.random_value(volatility)
    returns_absolute_change = utility.absolute_change(
        previous_value,
        returns_percent_change
    )
    drift_absolute_change = utility.absolute_change(previous_value, drift)
    return result(previous_value + returns_absolute_change + drift_absolute_change)


@build_simulation
def merton_jump_diffusion(previous_value, drift, volatility, jump_probability, jump_average, jump_volatility, **params):
    if utility.random_event(jump_probability):
        drop_percentage = utility.random_value(average=jump_average, stdev=jump_volatility) * -1
        drop_absolute_change = utility.absolute_change(
            previous_value, 
            drop_percentage
        )
        return result(previous_value + drop_absolute_change)

    returns_percent_change = utility.random_value(volatility)
    returns_absolute_change = utility.absolute_change(
        previous_value,
        returns_percent_change
    )
    drift_absolute_change = utility.absolute_change(previous_value, drift)

    return result(previous_value + returns_absolute_change + drift_absolute_change)
