#!/usr/bin/env python3
"""
AI Lab 1: Introduction to Python for AI
Author: Aprameya S J
Date: August 2025

This lab covers basic Python concepts commonly used in AI applications.
Note: Install numpy and matplotlib for advanced features (pip install -r requirements.txt)
"""

import math
import statistics

def basic_statistics(data):
    """
    Calculate basic statistics for a dataset.
    
    Args:
        data (list): List of numerical values
        
    Returns:
        dict: Dictionary containing mean, median, and standard deviation
    """
    stats = {
        'mean': statistics.mean(data),
        'median': statistics.median(data),
        'std_dev': statistics.stdev(data) if len(data) > 1 else 0,
        'min': min(data),
        'max': max(data)
    }
    
    return stats

def plot_data_ascii(data, title="Data Visualization"):
    """
    Create a simple ASCII plot of the data.
    
    Args:
        data (list): List of numerical values
        title (str): Title for the plot
    """
    print(f"\n{title}")
    print("=" * len(title))
    
    # Normalize data for ASCII display
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        normalized = [1 for _ in data]
    else:
        normalized = [(x - min_val) / (max_val - min_val) for x in data]
    
    # Create ASCII bar chart
    width = 50
    for i, val in enumerate(normalized):
        bar_length = int(val * width)
        bar = "#" * bar_length
        print(f"{i:2d}: {bar} ({data[i]})")
    print()

def main():
    """
    Main function demonstrating basic AI-related Python operations.
    """
    print("AI Lab 1: Introduction to Python for AI")
    print("=" * 40)
    
    # Sample data
    sample_data = [23, 45, 56, 78, 32, 67, 89, 12, 34, 56, 78, 90, 23, 45, 67]
    
    print(f"Sample Data: {sample_data}")
    print()
    
    # Calculate statistics
    stats = basic_statistics(sample_data)
    
    print("Statistical Analysis:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Standard Deviation: {stats['std_dev']:.2f}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")
    print()
    
    # Demonstrate list comprehension (useful in AI)
    squared_data = [x**2 for x in sample_data]
    print(f"Squared Data: {squared_data[:5]}... (showing first 5)")
    
    # Demonstrate filtering (useful in data preprocessing)
    filtered_data = [x for x in sample_data if x > 50]
    print(f"Values > 50: {filtered_data}")
    
    # Create ASCII visualization
    plot_data_ascii(sample_data, "Sample Data Visualization")
    
    print("Lab 1 completed successfully!")
    print("\nNote: For advanced plotting, install dependencies with:")
    print("pip install -r requirements.txt")

if __name__ == "__main__":
    main()