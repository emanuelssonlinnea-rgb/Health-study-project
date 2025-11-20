import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from math import sqrt
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize




#------------ Graph builder -----------------

class GraphBuilder:
    def __init__(self, title="Health study graphs", xlabel="X-axis", ylabel="Y-axis"):
        self.title=title
        self.xlabel = xlabel
        self.ylabel = ylabel
    
    def hist_plot(self, categories, bins=10, color="skyblue"):
        plt.figure(figsize = (8,5))
        plt.hist(categories,bins=bins, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(True, axis="y")
        plt.show()


    def box_plot(self, data, labels=None, color="mediumorchid"):
        plt.figure(figsize = (8,5))
        box = plt.boxplot(data, patch_artist=True, labels=labels)
        for patch in box['boxes']: # loppar igenom båda lådorna i grafen 
            patch.set_facecolor(color)  #lägger färg i box plot lådorna. 
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(True, axis="y")
        plt.show()

    def bar_plot(self, categories, values, color="plum"):
        plt.figure(figsize = (8,5))
        plt.bar(categories, values, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(True, axis="y")
        plt.show()

    def line_plot(self, x, y, label="Line", color="royalblue"):
        plt.figure(figsize = (8,5))
        plt.bar(x,y, label=label, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid(True, axis="y")
        plt.show()