import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("creditcard.csv")

X = data.drop("Class", axis=1)
y = data["Class"]

# Train model
model = RandomForestClassifier(n_estimators=20, random_state=42, n_jobs=-1)
model.fit(X, y)

# Save model
joblib.dump(model, "fraud_model.pkl")

print("Model saved successfully!")