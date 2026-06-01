def sum_digits(n: int) -> int:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def count_digits(n: int) -> int:
    return len(str(n))

def main():
    number = int(input("Введите число: "))
    s = sum_digits(number)
    cnt = count_digits(number)
  
    print(f"Сумма чисел: {s}")
    print(f"Количество цифр в числе: {cnt}")


if __name__ == "__main__":
    main()
