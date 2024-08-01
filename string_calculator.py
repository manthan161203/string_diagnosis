def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = ','
    if numbers.startswith("//"):
        parts = numbers.split('\n', 1)
        delimiter = parts[0][2:]
        numbers = parts[1]
    numbers = numbers.replace('\n', delimiter)
    num_list = numbers.split(delimiter)
    return sum(int(num) for num in num_list)
