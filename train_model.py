import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("Maternal Health Risk Data Set (1).csv")

# Encode labels
label_encoder = LabelEncoder()
df["RiskLevel"] = label_encoder.fit_transform(df["RiskLevel"])

# Features & target
X = df.drop("RiskLevel", axis=1)
y = df["RiskLevel"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
