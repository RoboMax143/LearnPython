def smallest_divisor(n: int) -> int:
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n

if __name__ == "__main__":
    n = int(input("Введите число: "))
    result = smallest_divisor(n)
    print(f"Наименьший делитель, отличный от единицы: {result}")
