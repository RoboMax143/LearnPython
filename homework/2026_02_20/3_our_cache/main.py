def cache(func):
    cached_results = dict()

    def wrapper(*args):
        key = args
        if key not in cached_results:
            cached_results[key] = func(*args)
        return cached_results[key]
    
    return wrapper


@cache
def my_sum(a, b):
    print(f"Вычисляю сумму {a} + {b}")
    return a + b


if __name__ == "__main__":
    print(my_sum(2, 3))
    print(my_sum(2, 3))
    print(my_sum(4, 5))
    print(my_sum(4, 5))
