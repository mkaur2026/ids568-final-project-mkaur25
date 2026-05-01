import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulate "reference" (training data)
reference = np.random.normal(50, 10, 1000)

# Simulate "current" (production data with drift)
current = np.random.normal(60, 15, 1000)


def calculate_psi(reference, current, bins=10):
    ref_hist, bin_edges = np.histogram(reference, bins=bins)
    cur_hist, _ = np.histogram(current, bins=bin_edges)

    ref_perc = (ref_hist + 1) / (len(reference) + bins)
    cur_perc = (cur_hist + 1) / (len(current) + bins)

    psi = np.sum((cur_perc - ref_perc) * np.log(cur_perc / ref_perc))
    return psi


psi_value = calculate_psi(reference, current)

print("Drift Detection Results")
print("-----------------------")
print(f"PSI value: {psi_value:.4f}")

if psi_value < 0.1:
    print("No significant drift")
elif psi_value < 0.2:
    print("Moderate drift detected")
else:
    print("Significant drift detected")


# Plot distributions
plt.hist(reference, bins=30, alpha=0.5, label="Reference Data")
plt.hist(current, bins=30, alpha=0.5, label="Current Data")
plt.legend()
plt.title("Drift Detection: Reference vs Current")
plt.xlabel("Feature Value")
plt.ylabel("Frequency")

plt.savefig("visualizations/drift_plot.png")
plt.show()
