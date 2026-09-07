import mne

file = "data/chb01/chb01_03.edf"

raw = mne.io.read_raw_edf(file, preload=True)

print(raw)
print()
print("Number of channels:", len(raw.ch_names))
print("Sampling frequency:", raw.info["sfreq"], "Hz")
print("Duration:", raw.times[-1], "seconds")
print()
print("Channels:")
for channel in raw.ch_names:
    print(channel)