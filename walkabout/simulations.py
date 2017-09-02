import walkabout

def brownian_motion(**args):
    @walkabout.build_simulation
    def simulate(previous_value, volatility):
        percent_change = walkabout.utility.random_value(volatility)
        absolute_change = walkabout.utility.absolute_change(previous_value, percent_change)
        return previous_value + absolute_change
    return simulate(**args)

def geometric_brownian_motion(**args):
    @walkabout.build_simulation
    def simulate(previous_value, drift, volatility):
        volatility_percent_change = walkabout.utility.random_value(volatility)
        volatility_absolute_change = walkabout.utility.absolute_change(previous_value, volatility_percent_change)
        drift_absolute_change = walkabout.utility.absolute_change(previous_value, drift)
        return previous_value + volatility_absolute_change + drift_absolute_change
    return simulate(**args)
