
import pandas as pd

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df


def normalize_column(df, column):
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df


import matplotlib.pyplot as plt
import seaborn as sns

class Custom:
    def __init__(self, style="seaborn"):
        
        plt.style.use(style)
    
    def pie_chart(self, labels, sizes, title="Pie Chart", colors=None, explode=None):
        
        plt.figure(figsize=(8, 8))
        plt.pie(
            sizes, 
            labels=labels, 
            colors=colors, 
            explode=explode, 
            autopct='%1.1f%%', 
            shadow=True, 
            startangle=90
        )
        plt.title(title)
        plt.axis('equal')  
        plt.show()

    def bar_chart(self, categories, values, title="Bar Chart", xlabel="Categories",
                  ylabel="Values", color="blue"):
        
        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color=color)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def scatter_plot(self, x, y, title="Scatter Plot", xlabel="X-axis", ylabel="Y-axis",
                     color="blue", size=20):
       
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, c=color, s=size, alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    def histogram(self, data, bins=10, title="Histogram", xlabel="Values", ylabel="Frequency",
                  color="blue"):
        
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=bins, color=color, alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    
