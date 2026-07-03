#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:11:51 2026

@author: dianalee
"""
# importing tools 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from fredapi import Fred

fred = Fred(api_key='7dd16f3d49b0e24ca0d5954de9d238ac')

cpi_series = {
    'Hawaii CPI':   'CUUSA426SA0S',  # Hawaii overall CPI
    'National CPI': 'CPIAUCSL',      # US overall CPI
}


cpi_data = pd.DataFrame()

# Download each CPI series
for name, code in cpi_series.items():
    try:
        s = fred.get_series(code, observation_start='2019-01-01', observation_end='2024-12-01')
        cpi_data[name] = s
        print(f'Downloaded: {name}')
    except:
        print(f'Could not download: {name} — skipping')
        
 #turn into percentage        
cpi_baseline = cpi_data.iloc[0]
cpi_pct = ((cpi_data - cpi_baseline) / cpi_baseline) * 100


print(cpi_pct.head())


#plotting
plt.figure(figsize=(12, 6))

# line for columns
for col in cpi_pct.columns:
    plt.plot(cpi_pct.index, cpi_pct[col], label=col, linewidth=2)
    
plt.title('Hawaii vs National Inflation Since Jan 2019', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=11)
plt.ylabel('% Change from Jan 2019', fontsize=11)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)

ax = plt.gca()
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/Users/dianalee/Desktop/hawaii_cpi_chart.png', dpi=150, bbox_inches='tight')
print('CPI chart saved!')


years = [2019, 2020, 2021, 2022, 2023, 2024]
visitors = [10243165, 2678073, 6777760, 9138674, 9499995, 9533375]

# Store in a pandas Series so we can plot it easily
# A Series is like a single column of data with labels
visitor_data = pd.Series(visitors, index=years, name='Visitor Arrivals')

# Convert to % change from 2019 (pre-COVID baseline)
# 2019 is our starting point so it becomes 0%
visitor_baseline = visitor_data[2019]
visitor_pct = ((visitor_data - visitor_baseline) / visitor_baseline) * 100

# Print to check
print(visitor_pct)


# Create a new chart
plt.figure(figsize=(12, 6))

# Draw line

plt.plot(visitor_pct.index, visitor_pct.values, 
         label='Visitor Arrivals', linewidth=2, color='#2196F3', marker='o')

# Add a horizontal line at 0% so we can see the pre-COVID baseline
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='2019 Baseline')

# Add title and labels
plt.title('Hawaii Visitor Arrivals % Change from 2019', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=11)
plt.ylabel('% Change from 2019', fontsize=11)
plt.legend(loc='lower right', fontsize=10)
plt.grid(True, alpha=0.3)

# Style the chart
ax = plt.gca()
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('/Users/dianalee/Desktop/hawaii_visitors_chart.png', dpi=150, bbox_inches='tight')
print('Visitor chart saved!')


# combined chart, ax1 left, ax2 right 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# left chart: Hawaii vs National CPI
for col in cpi_pct.columns:
    ax1.plot(cpi_pct.index, cpi_pct[col], label=col, linewidth=2)
ax1.set_title('Hawaii vs National Inflation (CPI)', fontsize=13, fontweight='bold')
ax1.set_xlabel('Date', fontsize=11)
ax1.set_ylabel('% Change from Jan 2019', fontsize=11)
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# right chart: Visitor arrivals
ax2.plot(visitor_pct.index, visitor_pct.values,
         label='Visitor Arrivals', linewidth=2, color='#2196F3', marker='o')
ax2.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='2019 Baseline')
ax2.set_title('Hawaii Tourism Recovery', fontsize=13, fontweight='bold')
ax2.set_xlabel('Year', fontsize=11)
ax2.set_ylabel('% Change from 2019', fontsize=11)
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
ax2.legend(loc='lower right', fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# big title across the whole figure
fig.suptitle('Did Hawaii Tourism Recovery Drive Higher Inflation?', 
             fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('/Users/dianalee/Desktop/hawaii_combined_chart.png', dpi=150, bbox_inches='tight')
print('Combined chart saved!')


















