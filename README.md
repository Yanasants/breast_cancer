<h1 align="center">Dataset Breast Cancer Data - Exploratory Analysis</h1>

> ⏳ Project in process

<h3 align="center">Dataset Breast Cancer Data</h3>

The dataset contains 569 rows and 33 columns. 

Attribute Information (available on: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data):

1) ID number
2) Diagnosis (M = malignant, B = benign)
3-32)

Ten real-valued features are computed for each cell nucleus:

a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. For instance, field 3 is Mean Radius, field
13 is Radius SE, field 23 is Worst Radius.

<p align="center">
  <img width="2000" height="180" src="https://user-images.githubusercontent.com/59098432/205473353-886a9956-c2dd-4298-912b-4556b30816e6.png">
</p>

<h3 align="center">Number of occurencies by each diagnosis</h3>

<p align="center">
  <img width="500" height="400" src="https://user-images.githubusercontent.com/59098432/205528781-d212e394-5dfd-4690-a348-6381c2ead7b1.png">
</p>

A plausible step is to analyze the correlations between the features and the diagnosis to understand which ones deserve focus to predict the diagnosis. The next analysis were built using only mean columns (columns 0 to 12).

<h3 align="center">Correlations between features</h3>

<p align="center">
  <img width="900" height="400" src="https://user-images.githubusercontent.com/59098432/205526529-aa2af0d2-e268-4782-868f-7b87698b5e76.png">
</p>

This way is possible to focus on features with larger correlation with diagnosis, like *mean concave points* and *mean perimeter*.

<h3 align="center">Mean Concave Points Distribution by Diagnosis</h3>

<p align="center">
  <img width="700" height="400" src="https://user-images.githubusercontent.com/59098432/205528142-9c90f92b-f8f0-4869-8780-dfbc6bbc11ee.png">
</p>

<h3 align="center">Diagnosis on correlation between mean concave points and mean perimeter</h3>

<p align="center">
  <img width="700" height="500" src="https://user-images.githubusercontent.com/59098432/205528973-814eec36-79c9-4fa0-b3fa-3a3dc9f3b429.png">
</p>







