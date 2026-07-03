#Hawaii Tourism and Inflation Analysis (2019-2024)

#Overview

This project looks into whether or not Hawaii's tourism recovery after COVID-19 drove higher inflation compared to the 
national average, using the Federal Reserve CPI data and Hawaii Tourism Authority visitor arrival data from 2019-2024.

#Key Finding 
Even though tourism did not recover fully to pre-covid levels (around 7% below 2019 in 2024), Hawaii's inflation tracked 
closely to the national average throughout the period. This suggests that Hawaii's inflation is driven by the same national forces,
such as (supply chains, energy) rather than tourism demand specifically. 

#Tools used 
- Python (pandas, matplotlib, fredapi)
- FRED API (Federal Reserve Economic Data)
- Hawaii Tourism Authority (HTA) Annual Visitor Statistics

#Files
- hawaiitourism.py - main 
- hawaii_visitors_chart.png - Hawaii visitor arrivals % change from 2019
- hawaii_cpi_chart.png - Hawaii vs national CPI since Jan 2019
- hawaii_combined_chart.png - side by side comparison

#Data Sources
- CPI data: U.S. Bureau of Labor Statistics via FRED
- Visitor arrivals: Hawaii Tourism Authority 2024 Annual Report
