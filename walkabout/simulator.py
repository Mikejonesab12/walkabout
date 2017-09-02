
def build_simulation(handler):
    def wrapper(type = 'full_path', **params):
        if(type=='last_value'):
            return get_last_values(handler, **params)
        else:
            return get_full_paths(handler, **params)
    return wrapper

def get_full_paths(handler, starting_value=0, iterations=0, steps=0, **params):
    paths = []
    for _ in range(iterations):
        path = [starting_value]
        for i in range(steps):
            path.append(handler(previous_value=path[i], **params))
        paths.append(path);
    if(len(paths)==1):
        return paths[0]
    return paths

def get_last_values(handler, starting_value=0, iterations=0, steps=0, **params):
    paths = []
    for _ in range(iterations):
        last_val = starting_value
        for i in range(steps):
            last_val = handler(previous_value=last_val, **params)
        paths.append(last_val);
    return paths
