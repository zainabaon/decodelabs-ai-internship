"""Classify Iris flowers with a K-Nearest Neighbors model.

This beginner-friendly example uses scikit-learn's built-in Iris dataset.
"""

# Import the dataset, preprocessing, model, data split, and evaluation tools.
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def main():
    # 1. Load the built-in Iris dataset (150 samples, 4 measurements, 3 flower classes).
    iris = load_iris()
    X = iris.data  # Features: sepal length/width and petal length/width.
    y = iris.target  # Labels: the numeric class for each flower.

    # 2. Scale each feature so every measurement has comparable influence on distance.
    # StandardScaler gives features a mean of 0 and a standard deviation of 1.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 3. Randomly split the scaled data: 80% for training and 20% for testing.
    # random_state makes the split reproducible; shuffle=True is explicit for beginners.
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.20,
        shuffle=True,
        random_state=42,
        stratify=y,
    )

    # 4. Create and train a KNN classifier using the five nearest training examples.
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)

    # 5. Predict the flower class for each unseen test example.
    y_pred = knn_model.predict(X_test)

    # 6. Evaluate the predictions with the requested classification metrics.
    accuracy = accuracy_score(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=iris.target_names)

    # 7. Print clearly labeled results.
    print("Iris K-Nearest Neighbors Classification Results")
    print("=" * 50)
    print(f"Dataset samples: {X.shape[0]}")
    print(f"Features per sample: {X.shape[1]}")
    print(f"Classes: {len(iris.target_names)} ({', '.join(iris.target_names)})")
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples: {X_test.shape[0]}")
    print(f"KNN neighbors (k): {knn_model.n_neighbors}")
    print()
    print(f"Accuracy: {accuracy:.2%}")
    print()
    print("Confusion Matrix")
    print("Rows = actual classes; columns = predicted classes")
    print(matrix)
    print()
    print("Classification Report")
    print(report)


if __name__ == "__main__":
    main()
