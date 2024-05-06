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

import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

def generate_random_points_with_timestamps(num_points, min_lat, max_lat, min_long, max_long):
    """
    Generate random points on a map with timestamps within the specified latitude and longitude range.

    Args:
    - num_points (int): The number of random points to generate.
    - min_lat (float): The minimum latitude.
    - max_lat (float): The maximum latitude.
    - min_long (float): The minimum longitude.
    - max_long (float): The maximum longitude.

    Returns:
    - DataFrame: Each row contains a timestamp, latitude, and longitude.
    """
    random_points = []
    for _ in range(num_points):
        lat = random.uniform(min_lat, max_lat)
        long = random.uniform(min_long, max_long)
        random_points.append((lat, long))
    
    # Generate random timestamps
    timestamps = pd.date_range(start='2024-01-01', periods=num_points, freq='D')
    
    # Create DataFrame with timestamps, latitudes, and longitudes
    df = pd.DataFrame(random_points, columns=['Latitude', 'Longitude'])
    df['Timestamp'] = timestamps
    
    return df

def forecast_points(df, forecast_steps=12):
    """
    Forecast future points using autoregression (AR) model.

    Args:
    - df (DataFrame): DataFrame containing timestamped points.
    - forecast_steps (int): The number of forecast steps to predict.

    Returns:
    - DataFrame: Forecasted future points.
    """
    # Extract latitude and longitude columns
    points = df[['Latitude', 'Longitude']].copy()
    
    # Fit autoregression model for latitude
    model_lat = AutoReg(points['Latitude'], lags=1)
    model_fit_lat = model_lat.fit()
    
    # Forecast latitude
    forecast_lat = model_fit_lat.forecast(steps=forecast_steps)
    
    # Fit autoregression model for longitude
    model_long = AutoReg(points['Longitude'], lags=1)
    model_fit_long = model_long.fit()
    
    # Forecast longitude
    forecast_long = model_fit_long.forecast(steps=forecast_steps)
    
    # Create DataFrame for forecasted points
    forecasted_points = pd.DataFrame({'Latitude': forecast_lat, 'Longitude': forecast_long})
    
    return forecasted_points

