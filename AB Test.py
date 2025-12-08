# ---------------------------
# 1. Imports and dataset
# ---------------------------
import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"my_data.csv")

# ---------------------------
# 2. User-level A/B test
# ---------------------------

# Create indicator columns
df["converted"] = (df["event"] == "purchase").astype(int)
df["is_login"] = (df["event"] == "login").astype(int)

# Aggregate per user and variant
user_metrics = df.groupby(["user_id", "variant"]).agg(
    converted=("converted", "max"),        # user converted at least once
    total_revenue=("revenue", "sum"),
    num_logins=("is_login", "sum")).reset_index()

# Metrics per variant
metrics_summary = user_metrics.groupby("variant").agg(
    conversion_rate=("converted", "mean"),
    avg_revenue=("total_revenue", "mean"),
    num_users=("user_id", "count")).reset_index()

print("=== Overall A/B Metrics ===")
print(metrics_summary)

# ---------------------------
# 3. Statistical Tests
# ---------------------------

# Conversion z-test
counts = user_metrics.groupby("variant")["converted"].sum().values
nobs = user_metrics.groupby("variant")["converted"].count().values
conv_stat, conv_pval = proportions_ztest(counts, nobs)

# Revenue t-test
rev_A = user_metrics[user_metrics["variant"] == "A"]["total_revenue"]
rev_B = user_metrics[user_metrics["variant"] == "B"]["total_revenue"]
rev_stat, rev_pval = ttest_ind(rev_A, rev_B, equal_var=False)

print("\n=== Overall Statistical Tests ===")
print(f"Conversion rate z-test: z={conv_stat:.3f}, p-value={conv_pval:.3f}")
print(f"Revenue t-test: t={rev_stat:.3f}, p-value={rev_pval:.3f}")

# ---------------------------
# 4. Visualizations
# ---------------------------

# Conversion Rate Plot
plt.figure(figsize=(6, 4))
plt.bar(metrics_summary['variant'], metrics_summary['conversion_rate'], 
        color=['skyblue', 'salmon'])
plt.ylabel("Conversion Rate")
plt.title("Overall Conversion Rate by Variant")
plt.show()

# Average Revenue Plot
plt.figure(figsize=(6, 4))
plt.bar(metrics_summary['variant'], metrics_summary['avg_revenue'], 
        color=['skyblue', 'salmon'])
plt.ylabel("Average Revenue")
plt.title("Overall Average Revenue by Variant")
plt.show()



