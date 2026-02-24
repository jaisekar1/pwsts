import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def run_all_models(features):
    results = {}

    # ---------------------------------------
    # 1️⃣ Isolation Forest (Unsupervised)
    # ---------------------------------------
    iso = IsolationForest(contamination=0.05, random_state=42)
    iso_labels = iso.fit_predict(features)

    results["isolation_forest"] = iso_labels
    results["isolation_model"] = iso

    # ---------------------------------------
    # 2️⃣ KMeans Clustering
    # ---------------------------------------
    kmeans = KMeans(n_clusters=4, random_state=42)
    cluster_labels = kmeans.fit_predict(features)

    results["kmeans"] = cluster_labels
    results["kmeans_model"] = kmeans

    # ---------------------------------------
    # 3️⃣ Random Forest (Supervised)
    # For demo purpose, use Isolation labels as pseudo-labels
    # ---------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        iso_labels,
        test_size=0.3,
        random_state=42
    )

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    # Evaluation Metrics
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted"),
        "Recall": recall_score(y_test, y_pred, average="weighted"),
        "F1 Score": f1_score(y_test, y_pred, average="weighted")
    }

    results["random_forest_model"] = rf
    results["evaluation_metrics"] = metrics

    return results


# ---------------------------------------
# Explainable AI
# ---------------------------------------
def show_feature_importance(model, X):
    importance = model.feature_importances_

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(X.columns, importance)
    plt.xticks(rotation=45)
    plt.title("Feature Importance (Random Forest)")
    plt.tight_layout()

    st.pyplot(fig)