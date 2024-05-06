"""The common module contains common functions and classes used by the other modules.
"""

def hello_world():
    """Prints "Hello World!" to the console.
    """
    print("Hello World!")


def calculate_average(sequence):
    """
    Calculate the average value of a sequence.

    Args:
        sequence (list or tuple): The sequence of numbers.

    Returns:
        float: The average value of the sequence.
    """
    if not sequence:
        return None  # Return None for empty sequence

    total = sum(sequence)
    average = total / len(sequence)
    return average

def sum_of_sequence(sequence):
    """
    Calculate the sum of a sequence.

    Args:
    sequence (list): A list of numbers.

    Returns:
    float: The sum of the numbers in the sequence.
    """
    total = 0
    for num in sequence:
        total += num
    return total

def solve_linear_equation(a, b):
    """
    Solve a linear equation of the form ax + b = 0.

    Args:
        a (float): Coefficient of the variable.
        b (float): Constant term.

    Returns:
        float: The solution for the variable x.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a linear equation.")

    return -b / a

import random

def generate_random_points(num_points, min_lat, max_lat, min_long, max_long):
    """
    Generate random points on a map within the specified latitude and longitude range.

    Args:
    - num_points (int): The number of random points to generate.
    - min_lat (float): The minimum latitude.
    - max_lat (float): The maximum latitude.
    - min_long (float): The minimum longitude.
    - max_long (float): The maximum longitude.

    Returns:
    - List of tuples: Each tuple contains the latitude and longitude of a random point.
    """
    random_points = []
    for _ in range(num_points):
        lat = random.uniform(min_lat, max_lat)
        long = random.uniform(min_long, max_long)
        random_points.append((lat, long))
    return random_points



import random


def generate_random_points(num_points, min_lat, max_lat, min_long, max_long):
    """
    Generate random points on a map within the specified latitude and longitude range.

    Args:
    - num_points (int): The number of random points to generate.
    - min_lat (float): The minimum latitude.
    - max_lat (float): The maximum latitude.
    - min_long (float): The minimum longitude.
    - max_long (float): The maximum longitude.

    Returns:
    - List of tuples: Each tuple contains the latitude and longitude of a random point.
    """
    random_points = []
    for _ in range(num_points):
        lat = random.uniform(min_lat, max_lat)
        long = random.uniform(min_long, max_long)
        random_points.append((lat, long))
    return random_points



