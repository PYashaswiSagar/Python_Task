"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
    
from typing import List

def calculate_power_with_difference(integers: List[int]) -> List[int]:
    if not integers:
        return []
    
    result = [integers[0] ** 2]  
    for i in range(1, len(integers)):
        prev_power = integers[i - 1] ** 2  
        diff = prev_power - integers[i - 1]  
        result.append(integers[i] ** 2 - diff) 
    
    return result

# Example usage:
print(calculate_power_with_difference([1, 2, 3])) 
print(calculate_power_with_difference([2, 3, 4])) 
