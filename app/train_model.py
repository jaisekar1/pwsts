
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/sample_dataset/network_sample.csv")
X = df.drop("Label", axis=1)
y = df["Label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/trained_models/rf_model.pkl")
print("Model trained and saved.")
