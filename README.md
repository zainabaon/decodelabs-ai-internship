# Iris KNN Classification

A foundational supervised-learning project that classifies Iris flowers into three species — Setosa, Versicolor, and Virginica — using a K-Nearest Neighbors (KNN) model built with scikit-learn.

This project, covers the core supervised-learning pipeline: loading data, scaling features, splitting into train/test sets, training a classifier, and evaluating results beyond plain accuracy.

## What it does

The script:
1. Loads scikit-learn's built-in Iris dataset (150 samples, 4 features, 3 classes)
2. Scales the four input features using `StandardScaler` (mean = 0, variance = 1)
3. Splits the data into an 80/20 train/test set, shuffled and stratified by class
4. Trains a K-Nearest Neighbors classifier with `k=5`
5. Predicts on the held-out test set
6. Evaluates performance using accuracy, a confusion matrix, and a full classification report (precision, recall, F1-score)

## Requirements

- Python 3.9+
- scikit-learn >= 1.0

## Setup & Run

```powershell
python -m pip install -r requirements.txt
python classifier.py
```

## Results

On a typical run (results vary slightly by random seed):

```
Accuracy: 93.33%

Confusion Matrix
[[10  0  0]
 [ 0 10  0]
 [ 0  2  8]]
```

| Class      | Precision | Recall | F1-score |
|------------|-----------|--------|----------|
| Setosa     | 1.00      | 1.00   | 1.00     |
| Versicolor | 0.83      | 1.00   | 0.91     |
| Virginica  | 1.00      | 0.80   | 0.89     |

### Key finding

Setosa is perfectly separable from the other two species — the model never confuses it with anything. The only errors occur between **Versicolor and Virginica**, which is expected: these two species have naturally overlapping petal and sepal measurements in the real world. Two Virginica samples were misclassified as Versicolor, which is why Virginica's recall (0.80) is lower than its precision (1.00).

This is also the core lesson of the exercise: **accuracy alone (93%) hides where the model actually struggles.** The confusion matrix and per-class F1 scores reveal that the weakness is specifically in distinguishing Versicolor from Virginica, not a general model failure.

## Project structure

```
P2/
├── classifier.py         # Main training/evaluation script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Possible next steps

- Try different values of `k` (e.g. 1, 3, 7, 15) and compare accuracy/F1 to find the optimal value
- Test other classifiers (Logistic Regression, Decision Tree, SVM) and compare performance
- Visualize the decision boundaries or a pairplot of the four features by species
- Try the model on a slightly noisy or synthetic new dataset to see how it generalizes