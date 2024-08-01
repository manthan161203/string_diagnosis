def add(numbers: str) -> int:
    if numbers == "":
        return 0
    num_list = numbers.split(',')
    return sum(int(num) for num in num_list)
