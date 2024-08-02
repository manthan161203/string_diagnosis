import re

def add(numbers: str) -> int:
    print(f"Input string: {numbers}")
    
    # Return 0 if the input is an empty string
    if not numbers:
        print("Empty input, returning 0.")
        return 0

    delimiter = ','
    # Check for custom delimiter specification
    if numbers.startswith("//"):
        parts = numbers.split('\n', 1)
        delimiter_part = parts[0][2:]
        numbers = parts[1]
        print(f"Custom delimiter part: '{delimiter_part}'")
        print(f"Numbers part after delimiter extraction: '{numbers}'")
        
        # Handle multiple custom delimiters enclosed in square brackets
        if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            print(f"Extracted delimiters: {delimiters}")
            for delim in delimiters:
                numbers = numbers.replace(delim, ',')
                print(f"Replaced '{delim}' with ',': '{numbers}'")
        else:
            # Handle single custom delimiter
            delimiter = delimiter_part
            numbers = numbers.replace(delimiter, ',')
            print(f"Replaced '{delimiter}' with ',': '{numbers}'")
    
    # Replace newlines with commas to unify delimiter usage
    numbers = numbers.replace('\n', ',')
    print(f"After replacing newlines: '{numbers}'")
    
    # Split the numbers by commas
    num_list = numbers.split(',')
    print(f"Split numbers: {num_list}")
    
    # Identify negative numbers
    negatives = [num for num in num_list if num and int(num) < 0]
    if negatives:
        print(f"Negatives found: {negatives}")
        raise ValueError(f"Negative numbers not allowed: {', '.join(negatives)}")
    
    # Calculate the sum, ignoring numbers greater than 1000
    total = 0
    for num in num_list:
        if num and int(num) <= 1000:
            total += int(num)

    print(f"Total sum (excluding >1000): {total}")
    
    return total
