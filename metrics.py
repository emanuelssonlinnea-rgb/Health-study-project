import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from math import sqrt
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
from sklearn.linear_model import LinearRegression
from io_utils import *
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns



# #RÄKNA UT MEDEL,MEDIA, MIN & MAX

class Metrics:
    """
    Calculates the average, median, minimum and maximum of various columns in the health_study_dataset
    """
    def __init__(self,df: pd.DataFrame):
        self.df = df
    def average(self, column_list: list)-> dict:
        averages = {}
        for col in column_list:
            if col not in self.df.columns:
                raise ValueError(f"Column '{col}' not found in health_study_dataset.")
            numeric_values = pd.to_numeric(self.df[col], errors = "coerce")
            mean_value = numeric_values.mean()
            if pd.isna(mean_value):
                raise ValueError(f"Column '{col}' contains no numeric values.")
            averages[col] = mean_value
        return averages
    def median(self, column_list: list)-> dict:
        medians = {}
        for col in column_list:
            if col not in self.df.columns:
                raise ValueError(f"Column '{col}' not found in health_study_dataset.")
            numeric_values = pd.to_numeric(self.df[col], errors = "coerce")
            median_value = numeric_values.median()
            if pd.isna(median_value):
                raise ValueError(f"Column '{col}' contains no numeric values.")
            medians[col] = median_value
        return medians
    def minimum(self, column_list: list)-> dict:
        minimums = {}
        for col in column_list:
            if col not in self.df.columns:
                raise ValueError(f"Column '{col}' not found in health_study_dataset.")
            numeric_values = pd.to_numeric(self.df[col], errors = "coerce")
            minimum_value = numeric_values.min()
            if pd.isna(minimum_value):
                raise ValueError(f"Column '{col}' contains no numeric values.")
            minimums[col] = minimum_value
        return minimums
    def maximum(self, column_list: list)-> dict:
        maximums = {}
        for col in column_list:
            if col not in self.df.columns:
                raise ValueError(f"Column '{col}' not found in health_study_dataset.")
            numeric_values = pd.to_numeric(self.df[col], errors = "coerce")
            maximum_value = numeric_values.max()
            if pd.isna(maximum_value):
                raise ValueError(f"Column '{col}' contains no numeric values.")
            maximums[col] = maximum_value
        return maximums

