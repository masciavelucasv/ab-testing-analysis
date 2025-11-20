# A/B Testing Analysis 📊

This repository demonstrates a **complete A/B testing workflow** using a synthetic dataset of user events. It allows comparison of **Variant A and Variant B** in terms of **conversion rate** and **revenue**, both **overall** and **per marketing channel**.  

Key features:

- 📈 User-level aggregation of metrics (conversion, revenue, logins)  
- 📊 Overall and channel-level statistical analysis  
- 🔬 Z-test for conversion rate and t-test for revenue  
- 📉 Visualizations for quick interpretation  
- 🏆 Identification of the “winning” variant per metric and channel

---

## Dataset 🗂️

The dataset simulates 5,000 users with random events:

- **Columns:**
  - `user_id` 🆔  
  - `event` 🎯 (`signup`, `login`, `purchase`, `share`, `feature_use`)  
  - `timestamp` ⏰  
  - `channel` 📣 (`email`, `social`, `ads`, `organic`)  
  - `variant` 🅰️🅱️  
  - `revenue` 💰

- **File:** `my_data.csv` (or generate using `generate_dataset.py`)

---

## Features / Workflow 🚀

### Overall A/B Test
- Aggregates user-level metrics:
  - `converted` ✅ (made at least one purchase)  
  - `total_revenue` 💵  
  - `num_logins` 🔑  
- Calculates **conversion rate** and **average revenue** per variant  
- Performs **z-test** (conversion) and **t-test** (revenue)  
- Visualizes results with bar charts 📊

### Channel-Level Analysis
- Aggregates metrics per user **per channel** 📡  
- Computes conversion and revenue per variant per channel  
- Performs statistical tests and identifies **winning variants** 🏆  
- Generates channel-level visualizations

---


```bash
git clone https://github.com/masciavelucasv/ab-testing-analysis.git
cd ab-testing-analysis


