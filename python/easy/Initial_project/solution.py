def fruits(tuple_of_fruits):
    result = {}
    for f in tuple_of_fruits:
        if (f.get('shape') == 'sphere' and
            300 <= f.get('mass') <= 600 and
            100 <= f.get('volume') <= 500):
            name = f.get('name')
            if name is not None:
                result[name] = result.get(name, 0) + 1
    return result

if __name__ == "__main__":
    output = fruits((
        {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
        {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
        {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
        {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250},
    ))
    print(output)  # {'apple': 2, 'lemon': 1}
