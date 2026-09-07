import mne
import numpy as np
import os

file = "data/chb01/chb01_03.edf"

raw = mne.io.read_raw_edf(file, preload=True)

# Seizure timing from chb01-summary.txt
seizure_start = 2996
seizure_end = 3036

# Experiment definitions
preictal_duration = 30 * 60  # 30 minutes
window_duration = 5 * 60     # 5 minutes

preictal_start = seizure_start - preictal_duration

# Store windows and labels
windows = []
labels = []

# Extract all 5-minute preictal windows
for window_start in range(
    preictal_start,
    seizure_start,
    window_duration
):
    window_end = window_start + window_duration

    window = raw.copy().crop(
        tmin=window_start,
        tmax=window_end
    )

    data = window.get_data()

    # Remove MNE's extra endpoint sample
    data = data[:, :window_duration * int(raw.info["sfreq"])]

    windows.append(data)
    labels.append(1)

# Convert lists to NumPy arrays
X = np.array(windows)
y = np.array(labels)

print()
print("Dataset:")
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Labels:", y)

# Create output directory
os.makedirs("data/processed", exist_ok=True)

# Save dataset
np.savez(
    "data/processed/chb01_preictal.npz",
    X=X,
    y=y
)

print()
print("Saved to: data/processed/chb01_preictal.npz")