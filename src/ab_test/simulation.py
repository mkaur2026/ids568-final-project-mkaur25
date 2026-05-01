import numpy as np
from scipy import stats


np.random.seed(42)

# ----------------------------
# Experiment setup
# ----------------------------
CONTROL_NAME = "Baseline batching config"
TREATMENT_NAME = "Improved batching config"

N_CONTROL = 1000
N_TREATMENT = 1000

# Simulated success rates
# Success = request completed within acceptable latency and returned output
CONTROL_SUCCESS_RATE = 0.88
TREATMENT_SUCCESS_RATE = 0.92

# Simulated latency in milliseconds
CONTROL_LATENCY_MEAN = 120
TREATMENT_LATENCY_MEAN = 105
LATENCY_STD = 25


def two_proportion_z_test(control_successes, control_n, treatment_successes, treatment_n):
    p_control = control_successes / control_n
    p_treatment = treatment_successes / treatment_n

    pooled = (control_successes + treatment_successes) / (control_n + treatment_n)
    standard_error = np.sqrt(
        pooled * (1 - pooled) * ((1 / control_n) + (1 / treatment_n))
    )

    z_stat = (p_treatment - p_control) / standard_error
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    return p_control, p_treatment, z_stat, p_value


def main():
    control_outcomes = np.random.random(N_CONTROL) < CONTROL_SUCCESS_RATE
    treatment_outcomes = np.random.random(N_TREATMENT) < TREATMENT_SUCCESS_RATE

    control_successes = control_outcomes.sum()
    treatment_successes = treatment_outcomes.sum()

    p_control, p_treatment, z_stat, p_value = two_proportion_z_test(
        control_successes,
        N_CONTROL,
        treatment_successes,
        N_TREATMENT
    )

    control_latency = np.random.normal(CONTROL_LATENCY_MEAN, LATENCY_STD, N_CONTROL)
    treatment_latency = np.random.normal(TREATMENT_LATENCY_MEAN, LATENCY_STD, N_TREATMENT)

    t_stat, latency_p_value = stats.ttest_ind(control_latency, treatment_latency)

    print("A/B Test Simulation Results")
    print("---------------------------")
    print(f"Control: {CONTROL_NAME}")
    print(f"Treatment: {TREATMENT_NAME}")
    print()
    print(f"Control success rate: {p_control:.3f}")
    print(f"Treatment success rate: {p_treatment:.3f}")
    print(f"Relative lift: {((p_treatment - p_control) / p_control) * 100:.2f}%")
    print(f"Z-statistic: {z_stat:.3f}")
    print(f"P-value: {p_value:.4f}")
    print()
    print(f"Control average latency: {control_latency.mean():.2f} ms")
    print(f"Treatment average latency: {treatment_latency.mean():.2f} ms")
    print(f"Latency p-value: {latency_p_value:.4f}")
    print()

    if p_value < 0.05 and treatment_latency.mean() < control_latency.mean():
        print("Recommendation: SHIP TREATMENT")
    elif p_value < 0.05:
        print("Recommendation: INVESTIGATE GUARDRAILS")
    else:
        print("Recommendation: RUN MORE DATA")


if __name__ == "__main__":
    main()
