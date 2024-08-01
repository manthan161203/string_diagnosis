def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers = numbers.replace('\n', ',')
    num_list = numbers.split(',')
    return sum(int(num) for num in num_list)
