import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = ','
    if numbers.startswith("//"):
        parts = numbers.split('\n', 1)
        delimiter_part = parts[0][2:]
        numbers = parts[1]
        if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            for delim in delimiters:
                numbers = numbers.replace(delim, ',')
        else:
            delimiter = delimiter_part
            numbers = numbers.replace(delimiter, ',')
    numbers = numbers.replace('\n', ',')
    num_list = numbers.split(',')
    negatives = [num for num in num_list if int(num) < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")
    return sum(int(num) for num in num_list if int(num) <= 1000)
