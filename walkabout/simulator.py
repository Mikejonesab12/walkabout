
def build_simulation(handler):
    def wrapper(type = 'full_path', **params):
        if(type=='last_value'):
            return get_last_values(handler, **params)
        else:
            return get_full_paths(handler, **params)
    return wrapper

def get_full_paths(handler, starting_value=0, iterations=0, steps=0, **params):
    paths = []
    state = {}
    for iteration in range(iterations):
        path = [starting_value]
        for step in range(steps):
            result = handler(**{'previous_value': path[step], 'current_path': path, **params, **state})
            path.append(result['value'])
            state = result['state']
        paths.append(path)
    return paths

def get_last_values(handler, starting_value=0, iterations=0, steps=0, **params):
    paths = []
    state = {}
    for iteration in range(iterations):
        last_val = starting_value
        for step in range(steps):
            result = handler(**{'previous_value': last_val, **params, **state})
            last_val = result['value']
            state = result['state']
        paths.append(last_val)
    return paths

def result(value, state = {}):
    return {
        'value': value,
        'state': state
    }