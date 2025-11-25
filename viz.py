import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io_utils import *




#------------ Graph builder -----------------

class GraphBuilder:
    """
    Creates visualization with different types of graphs
    """
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
        plt.figure(figsize=(8,5))
        plt.plot(x, y, label=label, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid(True)
        plt.show()

    def scatter_plot(self, x, y, label="Points", alpha=0.6, color="purple"):
        plt.figure(figsize=(8,5))
        plt.scatter(x, y, label=label, alpha=alpha, color=color)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid(True)
        plt.show()


#------------ Simulering -----------------

class Simulator:
    """
    Calculates the number of sick people, creates simulation and visualizes the difference
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.sannolikhet_sjuk = self._beräkna_sannolikhet()
        self.simulerade_värden = self._simulera_sjukdomar()

    #RÄKNA ANDEL SJUKA PERSONER I DATAN
    def _beräkna_sannolikhet(self) -> float:
        sjuk = (self.df["disease"] == 1).sum()
        total = len(self.df)
        print(f"Antal sjuka: {sjuk} av {total}")
        return sjuk / total

    #SIMULERA 1000 SLUMPADE PERSONER MED SAMMA SANNOLIKHET FÖR SJUKDOM
    def _simulera_sjukdomar(self, n: int = 1000) -> np.ndarray:
        np.random.seed(42)
        return np.random.choice([0, 1], size=n,p=[1 - self.sannolikhet_sjuk, self.sannolikhet_sjuk])  # använder choice eftersom detta är binär lista istället för normalfördelade värden. La även in "p" för parametrar i sannolikhet

    #JÄMFÖR SIMULERADE ANDELEN MED DEN VERKLIGA ANDELEN
    def real_mean(self, n: int) -> float:   
        return np.mean(np.random.choice(self.df["disease"], size=n, replace=False))

    def sample_mean(self, n: int) -> float: 
        return np.mean(np.random.choice(self.simulerade_värden, size=n, replace=False))


    #JÄMFÖR SIMULERADE ANDELEN MED DEN VERKLIGA ANDELEN O VISUALISERAR
    def jämför_simulering(self, n: int = 200, R: int = 2000):
        means_real = np.array([self.real_mean(n) for _ in range(R)])
        means_simulation = np.array([self.sample_mean(n) for _ in range(R)])

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(means_real, bins=30, alpha=0.6, label="Verkliga data")
        ax.hist(means_simulation, bins=30, alpha=0.6, label="Simulerade data")
        ax.axvline(self.sannolikhet_sjuk, color="k", linestyle="--", label="Verklig andel sjuka")
        ax.set_title("Jämförelse mellan verklig och simulerad sjukdom")
        ax.set_xlabel("Andel sjuka")
        ax.set_ylabel("Frekvens")
        ax.grid(True, axis="y")
        ax.legend()
        plt.show()

