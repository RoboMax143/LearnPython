import json
import os

def cache(filename='cache.json', key_type='positional'):
    def decorator(func):
        cache_dict = {}

        if os.path.exists(filename):
            try:
                f = open(filename, 'r', encoding='utf-8')
                loaded = json.load(f)
                f.close()
                cache_dict.clear()
                cache_dict.update(loaded)
            except (FileNotFoundError, json.JSONDecodeError):
                pass

        def save_cache():
            f = open(filename, 'w', encoding='utf-8')
            json.dump(cache_dict, f)
            f.close()

        def wrapper(*args, **kwargs):
            if key_type == 'positional':
                original_key = args
            else:
                original_key = tuple(sorted(kwargs.items()))

            key = str(original_key)

            if key not in cache_dict:
                result = func(*args, **kwargs)
                cache_dict[key] = result
                save_cache()

            return cache_dict[key]

        return wrapper
    return decorator


@cache(filename='my_sum.json', key_type='positional')
def my_sum(a, b):
    print("Сумма для args")
    return a + b

@cache(filename='greet.json', key_type='named')
def greet(name, greeting="Hello"):
    print("Приветствие для kwargs")
    return f"{greeting}, {name}!"

if __name__ == '__main__':
    print(my_sum(2, 3))
    print(my_sum(2, 3))

    print(greet(name="Alice"))
    print(greet(greeting="Hi", name="Bob"))
    print(greet(name="Alice"))
