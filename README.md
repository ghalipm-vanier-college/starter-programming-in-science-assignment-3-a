-- # starter-programming-in-science-assignment-3-a
420-SN1-RE: Programming In Science Fall 2025

---

# **Programming in Science – Assignment 3**

This is the starter project for **Programming in Science – Assignment 3**.
Written in Python and tested with **unittest / pytest**.
The focus of this assignment is **data visualization using NumPy, Pandas, and Matplotlib** with both **.txt** and **.csv** data files.

---

## **Question(s)**

---

### **1️⃣ (15%) Plot a Mathematical Function Using NumPy (`np.linspace`)**

Write a function that:

* Uses `np.linspace()` to generate **100 x-values** between **-10 and 10**
* Computes the function
  [
  y = x^2 + 2x - 3
  ]
* Plots the curve using Matplotlib with:

  * A title
  * Labeled axes
  * A grid

#### Example call:

```python
plot_parabola()
```

---

### **2️⃣ (15%) Linear Function vs. Oscillating Linear Function Using NumPy (`np.arange`)**

Write a function that:

- Uses `np.arange(-20, 20, 0.05)` to generate x-values
- Computes:
  - \( y_1 = x \)  (a straight line)
  - \( y_2 = x + \sin(x) \)  (the same line with a periodic oscillation)
- Plots **both curves** on the same graph
- Adds:
  - legend
  - axis labels
  - title

This plot illustrates how the function \( \sin(x) \) causes the curve to **oscillate around the baseline line** \( y = x \).

#### Example:
```python
plot_trig_waves()



---

### **3️⃣ (15%) Reading Array Data from a Text File (.txt)**

Write a function that reads a `.txt` file containing a **single line of space-separated numbers**, such as:

```
1.5 2.3 4.8 9.1
```

The function should:

* Read the file
* Convert the data into a **NumPy array**
* Plot the values as a **simple line plot**

Use `np.loadtxt()` or `np.genfromtxt()`.

#### Example:

```python
plot_array_from_txt("data.txt")
```

---

### **4️⃣ (15%) Monthly Temperature Plot from CSV (Pandas Line Plot)**

Write a function that:

1. Reads a CSV file containing two columns:

   ```
   Month,Temperature
   Jan, -5
   Feb, -3
   Mar, 2
   Apr, 9
   May, 15
   Jun, 20
   Jul, 23
   Aug, 22
   Sep, 17
   Oct, 10
   Nov, 3
   Dec, -2
   ```

2. Uses **Pandas** to read the data

3. Plots the temperature over months as a **line graph**

4. Labels axes and adds a title (e.g., “Average Monthly Temperature”)

#### Example:

```python
plot_temperature_csv("temperature.csv")
```

---

### **5️⃣ (20%) Scatter Plot from CSV Using Pandas**

Write a function that:

* Reads a CSV file with two numerical columns (e.g., Height vs. Weight, Temperature vs. Pressure)
* Uses Pandas to load the data
* Produces a **scatter plot**
* Labels axes, adds a title, and includes a grid

Example CSV:

```
Height,Weight
150,50
160,57
170,65
180,73
190,82
```

#### Example:

```python
plot_scatter_from_csv("measurements.csv")
```

---

### **6️⃣ (20%) Heatmap from a 2D Numeric File (NumPy or Pandas)**

Write a function that:

1. Reads a **2D numeric dataset** from a `.txt` or `.csv` file
2. Loads it as either:

   * a NumPy array (for `.txt` files), or
   * a Pandas DataFrame (for `.csv` files)
3. Generates a **heatmap** using `plt.imshow()`
4. Adds:

   * colorbar
   * title
   * labeled axes

Example matrix (`matrix.txt`):

```
1 3 5 2
4 6 1 0
7 2 8 9
3 5 7 1
```

#### Example:

```python
plot_heatmap("matrix.txt")
```

---

## **Plotting Requirement**

For Questions **1–6**, the auto-tests verify only that the functions *run without error*.
 **You must include screenshots of each generated plot** in your submission for full marks.

---

## **▶ Run Command**

```
pytest
```

or

```
python -m unittest
```


