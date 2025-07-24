# Custom_ModulE

# 📊 Data Cleaning and Visualization Toolkit (Python)

This repository provides a simple and reusable toolkit for performing basic **data preprocessing** and **visualizations** in Python. It includes functions for data cleaning, normalization, and a class-based interface for generating various types of plots using Matplotlib and Seaborn.

---

## 📁 Contents

- `data_utils.py` – Python module with:
  - `clean_data(df)` – removes missing values and duplicates
  - `normalize_column(df, column)` – standardizes a column using z-score
  - `Custom` class with:
    - `pie_chart()`
    - `bar_chart()`
    - `scatter_plot()`
    - `histogram()`

---

## 🧹 Data Preprocessing Functions

### `clean_data(df)`
Removes all `NaN` values and duplicate rows from the DataFrame.

### `normalize_column(df, column)`
Standardizes a numeric column by subtracting the mean and dividing by the standard deviation.

---

## 📊 Visualization Class: `Custom`

A flexible utility class to generate clean and styled plots using `matplotlib` with optional support for different themes (e.g., seaborn).

### Methods Included:
| Method | Description |
|--------|-------------|
| `pie_chart()` | Creates a pie chart with labels and percentages |
| `bar_chart()` | Generates a bar chart for categorical data |
| `scatter_plot()` | Creates a scatter plot with customizable size/color |
| `histogram()` | Displays a histogram with adjustable bin size |

---

## 🔧 Usage Example

```python
import pandas as pd
from data_utils import clean_data, normalize_column, Custom

# Sample DataFrame
df = pd.read_csv('your_dataset.csv')

# Clean and normalize
df = clean_data(df)
df = normalize_column(df, 'price')

# Create plots
viz = Custom(style='seaborn')
viz.bar_chart(df['brand'], df['price'], title='Average Laptop Price by Brand')

