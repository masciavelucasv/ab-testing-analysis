# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 16:47:21 2025

@author: masci
"""

# ---------------------------
# 1. Imports and dataset
# ---------------------------
import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\masci\OneDrive - Jonkoping University\Desktop\Projects\my_data.csv")

# ---------------------------
# 2. User-level A/B test
# ---------------------------
# Aggregate per user
user_metrics = df.groupby(['user_id', 'variant']).agg(
    converted=('event', lambda x: int('purchase' in x.values)),
    total_revenue=('revenue', 'sum'),
    num_logins=('event', lambda x: (x == 'login').sum())
).reset_index()

# Metrics per variant
metrics_summary = user_metrics.groupby('variant').agg(
    conversion_rate=('converted', 'mean'),
    avg_revenue=('total_revenue', 'mean'),
    num_users=('user_id', 'count')
).reset_index()

print("=== Overall A/B Metrics ===")
print(metrics_summary)

# Statistical tests
counts = user_metrics.groupby('variant')['converted'].sum().values
nobs = user_metrics.groupby('variant')['converted'].count().values
conv_stat, conv_pval = proportions_ztest(counts, nobs)

rev_A = user_metrics[user_metrics['variant']=='A']['total_revenue']
rev_B = user_metrics[user_metrics['variant']=='B']['total_revenue']
rev_stat, rev_pval = ttest_ind(rev_A, rev_B, equal_var=False)

print("\n=== Overall Statistical Tests ===")
print(f"Conversion rate z-test: z={conv_stat:.3f}, p-value={conv_pval:.3f}")
print(f"Revenue t-test: t={rev_stat:.3f}, p-value={rev_pval:.3f}")

# Visualize overall metrics
plt.figure(figsize=(6,4))
plt.bar(metrics_summary['variant'], metrics_summary['conversion_rate'], color=['skyblue','salmon'])
plt.ylabel('Conversion Rate')
plt.title('Overall Conversion Rate by Variant')
plt.show()

plt.figure(figsize=(6,4))
plt.bar(metrics_summary['variant'], metrics_summary['avg_revenue'], color=['skyblue','salmon'])
plt.ylabel('Average Revenue')
plt.title('Overall Average Revenue by Variant')
plt.show()

# ---------------------------
# 3. Channel-level A/B analysis
# ---------------------------
channel_metrics = df.groupby(['user_id','variant','channel']).agg(
    converted=('event', lambda x: int('purchase' in x.values)),
    total_revenue=('revenue', 'sum')
).reset_index()

# Metrics per channel and variant
channel_summary = channel_metrics.groupby(['channel','variant']).agg(
    conversion_rate=('converted', 'mean'),
    avg_revenue=('total_revenue', 'mean'),
    num_users=('user_id','count')
).reset_index()

print("\n=== Channel-level Metrics ===")
print(channel_summary)

# Statistical tests per channel
results = []
for channel in df['channel'].unique():
    data = channel_metrics[channel_metrics['channel']==channel]
    
    # Conversion z-test
    counts = data.groupby('variant')['converted'].sum().values
    nobs = data.groupby('variant')['converted'].count().values
    conv_stat, conv_pval = proportions_ztest(counts, nobs)
    
    # Revenue t-test
    rev_A = data[data['variant']=='A']['total_revenue']
    rev_B = data[data['variant']=='B']['total_revenue']
    rev_stat, rev_pval = ttest_ind(rev_A, rev_B, equal_var=False)
    
    # Determine winner
    conv_winner = 'A' if data[data['variant']=='A']['converted'].mean() > data[data['variant']=='B']['converted'].mean() else 'B'
    rev_winner = 'A' if rev_A.mean() > rev_B.mean() else 'B'
    
    results.append([channel, conv_stat, conv_pval, conv_winner, rev_stat, rev_pval, rev_winner])

results_df = pd.DataFrame(results, columns=[
    'channel', 'conv_z', 'conv_pval', 'conv_winner', 
    'rev_t', 'rev_pval', 'rev_winner'
])

print("\n=== Channel-level Statistical Tests with Winners ===")
print(results_df)

# ---------------------------
# 4. Visualizations per channel
# ---------------------------
# Conversion rate per channel
plt.figure(figsize=(10,5))
for variant in ['A','B']:
    subset = channel_summary[channel_summary['variant']==variant]
    plt.bar(subset['channel'], subset['conversion_rate'], alpha=0.7, label=f'Variant {variant}')
plt.ylabel('Conversion Rate')
plt.title('Conversion Rate by Variant per Channel')
plt.legend()
plt.show()

# Revenue per channel
plt.figure(figsize=(10,5))
for variant in ['A','B']:
    subset = channel_summary[channel_summary['variant']==variant]
    plt.bar(subset['channel'], subset['avg_revenue'], alpha=0.7, label=f'Variant {variant}')
plt.ylabel('Average Revenue')
plt.title('Average Revenue by Variant per Channel')
plt.legend()
plt.show()
