# 🦟 Mosquitoes and Monsoons  
### *An Analytical View of Rainfall vs Dengue Trends in Dhaka (2020–2025)*

![Banner](https://img.shields.io/badge/Dengue%20Analysis-2020--2025-blue)  
*A data-driven exploration of how monsoonal weather patterns influence dengue outbreaks in Dhaka, Bangladesh.*

---

## 📌 Overview

"**Mosquitoes and Monsoons**" is a comprehensive analytical project exploring the relationship between climatic factors—primarily rainfall, temperature, and humidity—and the spread of dengue fever in Dhaka from 2020 to 2025. By integrating official weather and health datasets, this project highlights seasonal trends, statistical correlations, and anomaly patterns to better understand when and why dengue outbreaks occur.

This work is intended to support epidemiologists, urban planners, public health professionals, and policymakers in better predicting and mitigating dengue risks, particularly in highly urbanized monsoon-prone areas like Dhaka.

---

## 🎯 Objectives

1. 📈 **Visualize Seasonal Patterns** of Rainfall and Dengue Cases  
2. 📊 **Show Statistical Correlation** Between Rainfall and Dengue Incidence  
3. ⏳ **Illustrate Time-Lag Effects** Between Rainfall and Dengue Outbreaks  
4. 🌡️ **Display the Impact of Temperature and Humidity** on Dengue Risk  
5. 🚨 **Detect and Highlight Anomalies or Outliers**, such as dengue spikes during off-season or rainless days

---

## 🔍 Key Findings

### 📆 **Seasonal Trends**
- Dengue cases begin to rise around **March/April**, peaking in **September/October**, then slowly declining. **February** records the **lowest** dengue incidence.
- Rainy days start increasing from **March**, peaking in **June**. **January** sees the **least rainfall**.

### 📌 **KPI Highlights**
- **2023** had the **highest dengue cases** (~110,000 cases), with **August** alone recording ~29,000 cases.
- **2024** was the **wettest year**, with **~5,500 mm rainfall**. **June** alone had **~1,800 mm**.
- **Anomaly-prone months**: November, December, and January — typically dry months but observed significant dengue activity.

### 🔁 **Climatic Relationships**
- Dengue risk **increases** when:
  - **Temperature** is between **28–32°C**
  - **Humidity** is between **70–85%**
- High humidity is a **common factor** in most anomaly days, regardless of temperature.
- Surprisingly, **many high-case days** had **zero rainfall**, but prior days with moderate rain. This suggests a **time-lag effect**.
- **Rainfall above 130 mm/day** tends to **suppress** dengue transmission — likely due to larval washouts.

### ⚠️ **Anomaly Detection Criteria**
A day is marked **anomalous** if:
- It recorded **>20 dengue cases**
- **Previous 5 days** had **zero rainfall**

---

## 🧰 Requirements

Install dependencies using a Python virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate

# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install pandas==2.3.0 beautifulsoup4==4.13.0 selenium==4.35.0
