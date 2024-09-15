# EXPERIMENT 3 - Python Data Analysis

## I. Intended Learning Outcomes

1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

## II. Materials Used
1. [Cars File](http://bit.ly/Cars_file)
2. Jupyter Notebook
3. ChatGPT

## III. Instructions
1. Write a Python script/code in the Jupyter Notebook to do the given problems.
2. Submit your Jupyter notebook in the dedicated submission bin.

### Problem 1
> [!NOTE]
> _Save your file as Surname_Pandas-P1.py_

**Using knowledge obtained from the experiment and demonstrations:**
1. Load the corresponding .csv file into a data frame named cars using pandas
2. Display the first five and last five rows of the resulting cars.

### Problem 2
> [!NOTE]
> _Save your file as Surname_Pandas-P2.py_

**Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.:**
1. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
2. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
3. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
4. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

## IV. Solutions
Set up the libraries for numerical computing, data manipulation, and mathematical operations.
``` js
import numpy as np
import pandas as pd
from math import *
``` 
### ***Problem 1***
> **1. Load the corresponding .csv file into a data frame named 'cars'**

> [!NOTE]
> The file must be on the same folder as the notebook
```js
cars = pd.read_csv('cars.csv')
cars
```
> **2. Display the first five and last five rows of the resulting cars**

```js
print("First five rows of the 'cars' data frame:")
cars.head()
```
```js
print("\nLast five rows of the 'cars' data frame:")
cars.tail()
```
**Explanation**

_`.head()` : Gets the first five rows_

_`.tail()` : Gets the last five rows._

### ***Problem 2***
> **1. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.**

   ```js
   print("First five rows with odd-numbered columns:")
   cars.iloc[:5, ::2]
   ```

   **Explanation**

  _`iloc[:5]` : Selects the first five rows._ 
  
  _`::2:` : Slices every second column, starting from column 0._
  
> **2. Display the row that contains the ‘Model’ of ‘Mazda RX4’.**

   ```js
   print("\nRow with the 'Mazda RX4':")
   mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
   mazda_rx4
   ```
**Explanation**

  _`cars['Model'] == 'Mazda RX4'` : Creates a boolean mask where the 'Model' column equals 'Mazda RX4'._
  
  _`cars[...]` : Selects the row where the condition is True, displaying the full row corresponding to 'Mazda RX4'._
  
> **4. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?**

```js
print("\nNumber of cylinders in 'Camaro Z28':")
camaro_z28_cyl = cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0]
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]
```
**Explanation**

_`cars[cars['Model'] == 'Camaro Z28']`: Selects the row(s) in the DataFrame where the 'Model' matches 'Camaro Z28'._

_`['cyl']`: Extracts the 'cyl' column (which contains the number of cylinders) from the selected row._

_`.values[0]`: Retrieves the first value from the resulting array, which is the number of cylinders for 'Camaro Z28'._

_`cars.loc[...]`: Uses the .loc function to select rows based on a condition._

_`cars['Model'] == 'Camaro Z28'`: Creates a boolean condition that identifies the row where the 'Model' is 'Camaro Z28'._

_`['Model', 'cyl']`: Specifies that only the 'Model' and 'cyl' columns should be shown for the matching row(s)._

> **5. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.**

```js
print("\nCylinders and gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':")
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
selected_cars = cars[cars['Model'].isin(models)][['Model', 'cyl', 'gear']]
selected_cars
```
**Explanation**

_`models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']` creates a list of the car models you are interested in: `'Mazda RX4 Wag'`, `'Ford Pantera L'`, and `'Honda Civic'`_

_`cars['Model'].isin([...])`: Checks whether the 'Model' column contains any of the specified car models._

_`[['Model', 'cyl', 'gear']]` : selects only the 'Model', 'cyl', and 'gear' columns from the filtered DataFrame._

## V. Other Informations
Author: Daphne P. Robleado

Section: 2ECE-A

## VI. See Version History
* 3 Readme file completed
* 2 Uploaded Notebook and .py files
* 1 Repository has been established
