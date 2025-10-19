# 🦟 Mosquitoes and Monsoons
### *An Analytical View of Rainfall vs Dengue Trends in Dhaka (2020–2025)*

This repository contains the data scraping, cleaning, analysis, and visualization scripts for a project examining the complex relationship between **rainfall, weather parameters, and Dengue Fever incidence in Dhaka, Bangladesh, from 2020 to 2025.**

***

## 🧭 Motivation

While searching for an interesting project idea, a close friend of mine was affected by dengue. That experience made me realize the real-world impact of the disease and inspired me to explore its patterns. Given the strong seasonal nature of dengue in Dhaka, I decided to analyze its connection with weather parameters like rainfall, temperature, and humidity.

***

## 🎯 Objectives

The primary goals of this analytical project are to:

1.  **Visualize Seasonal Patterns** of Rainfall and Dengue Cases.
2.  **Show Statistical Correlation** Between Rainfall and Dengue Incidence.
3.  **Display the Impact of Temperature and Humidity** on Dengue Risk.
4.  **Detect and Highlight Anomalies or Outliers** (Identify unusual patterns such as dengue spikes without recent rainfall or during off-season months using alerts, annotations, or color-coded markers.)

***

## 💡 Overview

This project started with collecting around **12,000 rows** of time-series data from multiple websites. I used **Selenium** to handle pages with dynamic content and **Beautiful Soup** for simpler static pages. After gathering the data, I cleaned and processed everything using **Pandas** and **NumPy** to create a clean, reliable dataset for analysis and visualization.

***

## 📊 Data Sources

| Data Type | Source URL |
| :--- | :--- |
| **Weather Data** (Temperature, Humidity, etc.) | `https://www.wunderground.com/history/daily/bd/dhaka/VGHS/` |
| **Dengue Case Data** | `https://dashboard.dghs.gov.bd/pages/heoc_dengue_v1` |
| **Rainfall Data** | `https://live8.bmd.gov.bd/map/1/d/2025-01-01` |

### Anomaly Detection Criteria

An anomaly day is defined as:
> A day with **more than 20 dengue cases** AND the **previous 5 days had zero rainfall**.

*(Units: Temperature in °C, Rainfall in mm)*

***

## 🔍 Key Findings

### Seasonal Trends
* **Dengue Cases:** Cases typically begin to increase in **March/April**, reaching a **peak in September/October**, before starting a slight decrease. **February** consistently records the lowest number of cases.
* **Rainfall:** Rainy days commence in **March**, with the highest rainfall peak observed in **June**. **January** is the month with the lowest average number of rainy days.

### Key Performance Indicators (KPIs)
* **2023** was the year with the **highest recorded dengue cases**, totaling around **110,000**. **August 2023** was the peak month, reporting approximately **29,000 cases**.
* **2024** was the **most rainy year**, recording about **5,500 mm** of precipitation. **June 2024** was the most rainy month with roughly **1,800 mm**.
* The months of **November, December, and January** contain the highest number of **anomaly days**.

### Relations & Meteorological Impact
* **Temperature & Humidity:** There is a strong positive correlation: as temperature and humidity increase, dengue cases also rise.
    * The **highest risk window** is identified when **Temperature is $24-32^{\circ}C$** and **Humidity is $65-85\%$**.
    * Risk is especially elevated with **Temperature between $28-32^{\circ}C$** and **Humidity between $70-85\%$**.
    * Most anomaly days have **high humidity**, indicating that humidity is a persistent driver across various temperatures, while low humidity days rarely result in anomalies.
* **Rainfall Dynamics:**
    * Many days with **high dengue case counts** recorded **zero rainfall** on that specific day. This suggests that the *preceding days'* rainfall, which creates stagnant water pools, is a more critical factor than current-day rain.
    * If daily rainfall **exceeds $130$ mm**, the chance of a dengue case increase is very low, as heavy rain may flush out mosquito breeding sites.
    * Basically, days with **no current rain** but that have **previous days with rainfall** have a high chance for a dengue case increase.


***

## 📈 Tableau Public Dashboard

### Overview Dashboard
![alt text](src/img/overview.png)

This Dashboard explores how weather conditions **rainfall**, **temperature**, and **humidity** may influence the rise of **dengue cases** in **Dhaka**.

- View **yearly totals** of dengue cases, rainfall, average humidity, and temperature.
- See **daily anomalies vs normal days** based on weather patterns.
- Explore **monthly trends** of dengue cases and rainfall across years.
- Check the **top 5 days** with the highest dengue cases and the rainfall trends leading up to them.

### Relations Dashboard
![alt text](src/img/relations.png)

What You Can View on This Dashboard.

- View the relationship between **Temperature & Humidity vs Dengue**
- Understand how **Humidity and Temperature impact Anomalies**
- Analyze **Yearly Dengue and Rainfall Trends**
- Explore **Monthly Dengue and Rainfall Patterns**
- Discover the **Correlation Between Rainfall and Dengue**

**Tableau Public Dashboard Link:**
[View Now](https://public.tableau.com/views/Analyzingweather-DenguecorrelationinDhaka20202025/Intro)


***

## 🔧 Requirements and Setup

To run the data processing and analysis scripts, follow the steps below. It's recommended to use a **virtual environment** to manage dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/alaminsframe/Weather-Dengue-Trends-in-Dhaka.git
cd Weather-Dengue-Trends-in-Dhaka
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

```bash
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```