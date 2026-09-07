# MUSE Seizure Detection

EEG-based seizure forecasting research project using the CHB-MIT Scalp EEG Database.

## Current Dataset Construction

The current pipeline converts the CHB-MIT seizure detection dataset into a preliminary seizure forecasting dataset.

### Experimental Definition

- Preictal period: 30 minutes before seizure onset
- EEG window: 5 minutes
- Window overlap: none
- Preictal label: 1
- Interictal label: 0
- Seizure period excluded

### Current Prototype

Tested on CHB01:

- 1 seizure
- 6 preictal windows
- 22 interictal windows
- 28 total windows
- 23 EEG channels
- 5-minute windows
- 256 Hz sampling rate

This is currently a preprocessing prototype and is not yet sufficient for model training or evaluation.

## Planned Next Steps

1. Generalize preprocessing across CHB-MIT patients
2. Preserve patient/file/seizure metadata
3. Establish leakage-safe train/validation/test splits
4. Determine EEG preprocessing pipeline
5. Address class imbalance
6. Train and evaluate forecasting models

## Data

The CHB-MIT EEG data are not included in this repository. The `data/` directory is excluded through `.gitignore`.
