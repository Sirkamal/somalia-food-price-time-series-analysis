# Somalia Food Price Time Series Analysis

## Project Overview

This project analyzes historical staple food prices in Somalia using the World Food Programme (WFP VAM) dataset.
The goal is to transform a large, messy real-world dataset into a clean analytical dataset and extract meaningful economic insights.

The analysis focuses on staple commodities including maize, sorghum, rice, and wheat flour across multiple regions and years.

---

## Objectives

* Clean and preprocess raw market price data
* Handle missing values and inconsistent entries
* Analyze long-term food price trends
* Compare price behavior between staple commodities
* Study correlation between major staple foods
* Prepare dataset for predictive modeling

---

## Dataset

Source: World Food Programme (WFP) - Vulnerability Analysis and Mapping (VAM)

The dataset contains:

* Market locations
* Commodity type
* Units and currency
* Monthly price observations
* Multi-year coverage (1995–2021)

---

## Data Preparation

Key preprocessing steps:

* Column selection and renaming
* Date construction from Year and Month
* Handling missing values (NaN analysis)
* Filtering Somalia-specific records
* Creating time-indexed data
* Feature reduction using correlation analysis

---

## Exploratory Data Analysis

Performed analyses include:

* Price distribution visualization
* Commodity average price comparison
* Monthly trend visualization
* Time series plots
* Correlation heatmap between staple foods

Main insight:
Strong correlation was observed between Maize and Sorghum prices, suggesting shared market drivers.

---

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Future Work

* Price forecasting using regression models
* Time-series modeling
* Inflation proxy estimation
* Market shock detection

---

## Author

Kamal Mohamed
Mogadishu, Somalia
Open to Remote Opportunities
