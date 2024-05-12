import os
import cv2
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Function to load images from a folder
def load_images(folder_path):
    images = []
    labels = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Assuming images are JPG or PNG
            img = cv2.imread(os.path.join(folder_path, filename))
            # Convert image to grayscale (if needed) and resize to a fixed size
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            img = cv2.resize(img, (100, 100))  # Resize image to 100x100
            images.append(img.flatten())  # Flatten image array
            labels.append(filename.split("_")[0])  # Extract label from filename
    return np.array(images), np.array(labels)

def run(folder_path):
    # Load images and labels from the folder
    images, labels = load_images(folder_path)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    # Train Naive Bayes classifier
    nb_classifier = GaussianNB()
    nb_classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = nb_classifier.predict(X_test)

    # Evaluate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Compute precision and recall
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    print("Precision:", precision)
    print("Recall:", recall)
    return accuracy, precision, recall
