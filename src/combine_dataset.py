import numpy as np

# Load preictal data
preictal = np.load("data/processed/chb01_preictal.npz")
X_preictal = preictal["X"]
y_preictal = preictal["y"]

# Load interictal data
interictal = np.load("data/processed/chb01_interictal.npz")
X_interictal = interictal["X"]
y_interictal = interictal["y"]

# Combine the two datasets
X = np.concatenate([X_preictal, X_interictal], axis=0)
y = np.concatenate([y_preictal, y_interictal], axis=0)

print("Combined dataset:")
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Number of preictal windows:", np.sum(y == 1))
print("Number of interictal windows:", np.sum(y == 0))

# Save combined dataset
np.savez(
    "data/processed/chb01_forecasting.npz",
    X=X,
    y=y
)

print("\nSaved to: data/processed/chb01_forecasting.npz")