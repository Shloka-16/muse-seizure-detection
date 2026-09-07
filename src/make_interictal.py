import mne
import numpy as np
import os

# Seizure-free EDF files
files = [
    "data/chb01/chb01_01.edf",
    "data/chb01/chb01_02.edf"
]

window_duration = 5 * 60  # 5 minutes

windows = []
labels = []
metadata = []

for file in files:

    print(f"\nProcessing {file}...")

    raw = mne.io.read_raw_edf(file, preload=True)

    sfreq = int(raw.info["sfreq"])
    recording_duration = raw.times[-1]

    # Extract non-overlapping 5-minute windows
    for window_start in range(
        0,
        int(recording_duration) - window_duration + 1,
        window_duration
    ):

        window_end = window_start + window_duration

        window = raw.copy().crop(
            tmin=window_start,
            tmax=window_end
        )

        data = window.get_data()

        # Make every window exactly 76800 samples
        data = data[:, :window_duration * sfreq]

        windows.append(data)

        # 0 = interictal
        labels.append(0)

        metadata.append({
            "file": file,
            "start": window_start,
            "end": window_end,
            "label": 0
        })

        print(
            f"Window: {window_start} → {window_end} seconds | "
            f"Shape: {data.shape} | Label: 0"
        )

# Convert to NumPy arrays
X = np.array(windows)
y = np.array(labels)

print("\nDataset:")
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Labels:", y)

# Create output directory
os.makedirs("data/processed", exist_ok=True)

# Save
np.savez(
    "data/processed/chb01_interictal.npz",
    X=X,
    y=y
)

print("\nSaved to: data/processed/chb01_interictal.npz")