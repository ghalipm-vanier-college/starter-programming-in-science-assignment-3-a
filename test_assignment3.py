# DO NOT MODIFY THIS FILE — DOING SO MAY RESULT IN A ZERO.
import unittest
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Assignment3 import (
    plot_parabola,
    plot_trig_waves,
    plot_array_from_txt,
    plot_temperature_csv,
    plot_scatter_from_csv,
    plot_heatmap
)

def test_plot_parabola():
    try:
        plt.figure()
        plot_parabola()
        success = True
    except Exception:
        success = False
    assert success

def test_plot_trig_waves():
    try:
        plt.figure()
        plot_trig_waves()
        success = True
    except Exception:
        success = False
    assert success

def test_plot_array_from_txt():
    filename = "test_array.txt"
    with open(filename, "w") as f:
        f.write("1.5 2.3 4.8 9.1")
    try:
        plt.figure()
        plot_array_from_txt(filename)
        success = True
    except Exception:
        success = False
    os.remove(filename)
    assert success

def test_plot_temperature_csv():
    filename = "temperature_test.csv"
    with open(filename, "w") as f:
        f.write("Month,Temperature\nJan,-5\nFeb,-3\nMar,2\nApr,9\nMay,15\nJun,20\nJul,23\nAug,22\nSep,17\nOct,10\nNov,3\nDec,-2\n")
    try:
        plt.figure()
        plot_temperature_csv(filename)
        success = True
    except Exception:
        success = False
    os.remove(filename)
    assert success

def test_plot_scatter_from_csv():
    filename = "scatter_test.csv"
    with open(filename, "w") as f:
        f.write("Height,Weight\n150,50\n160,57\n170,65\n180,73\n190,82\n")
    try:
        plt.figure()
        plot_scatter_from_csv(filename)
        success = True
    except Exception:
        success = False
    os.remove(filename)
    assert success

def test_plot_heatmap():
    filename = "matrix_test.txt"
    with open(filename, "w") as f:
        f.write("1 3 5 2\n4 6 1 0\n7 2 8 9\n3 5 7 1\n")
    try:
        plt.figure()
        plot_heatmap(filename)
        success = True
    except Exception:
        success = False
    os.remove(filename)
    assert success

if __name__ == "__main__":
    unittest.main()
