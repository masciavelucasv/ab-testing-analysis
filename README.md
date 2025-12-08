# 📊 A/B Testing Analysis
This repository showcases a complete end-to-end A/B testing workflow applied to a synthetic dataset of user events.
The goal is to evaluate the performance of Variant A vs Variant B in terms of conversion, revenue, and engagement, both overall and across different marketing channels.

The project demonstrates how to clean experimental data, generate user-level metrics, perform inferential statistical tests, and visualize results to support data-driven decision making.

# 📂 Dataset

The dataset (my_data.csv) simulates 5,000 unique users, each generating multiple events.
It includes a mixture of behavioral and transactional signals to mimic a real product analytics environment.

# Columns
| Column      | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| `user_id`   | Unique anonymous user identifier                            |
| `event`     | User activity (signup, login, purchase, share, feature_use) |
| `timestamp` | Event time                                                  |
| `channel`   | Marketing acquisition channel (email, social, ads, organic) |
| `variant`   | A/B assignment — Variant **A** or **B**                     |
| `revenue`   | Revenue attributed to purchase events                       |

# 🚀 Project Workflow
**1. User-Level Aggregation**

Each user is summarized with:

converted → whether they purchased at least once

total_revenue → sum of all revenue events

num_logins → login frequency

This enables a clean comparison between variants at the user level.

**2. Overall A/B Test**
Metrics computed per variant:

Conversion rate

Average revenue per user

Number of users in each group

Statistical tests:

Two-sample z-test → for conversion rates

Two-sample t-test → for revenue differences

**Visualizations:**

Conversion rate comparison

Average revenue comparison

These help quickly identify which variant performs better.

# 3. Channel-Level Analysis

Users are further segmented by acquisition channel:

-email

-social

-ads

-organic

For each channel and each variant:

-Conversion rate

-Average revenue

-Number of active users

Statistical tests evaluate whether performance differences are significant.

# A “winner” is identified per channel based on both conversion and revenue outcomes.

Channel Visualizations:

-Conversion rate per channel

-Revenue per channel
