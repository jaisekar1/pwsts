from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.svm import OneClassSVM
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

def run_multi_models(X, y=None):

    results = {}

    # Isolation Forest
    iso = IsolationForest(contamination=0.05, random_state=42)
    iso_pred = iso.fit_predict(X)
    results["IsolationForest"] = iso_pred

    # One-Class SVM
    svm = OneClassSVM(nu=0.05)
    svm_pred = svm.fit_predict(X)
    results["OneClassSVM"] = svm_pred

    # KMeans Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    cluster_pred = kmeans.fit_predict(X)
    results["KMeans"] = cluster_pred

    # Random Forest (if labels available)
    if y is not None:
        rf = RandomForestClassifier()
        rf.fit(X, y)
        rf_pred = rf.predict(X)

        results["RandomForest"] = {
            "Accuracy": accuracy_score(y, rf_pred),
            "Precision": precision_score(y, rf_pred),
            "Recall": recall_score(y, rf_pred),
            "F1": f1_score(y, rf_pred)
        }

    return results