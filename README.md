Dataset

Source: World Food Programme (WFP) — VAM Food Prices Database

The dataset contains:

Multiple countries

Multiple regions and markets

Different commodities (rice, maize, sorghum, wheat, fuel, livestock, etc.)

Monthly price observations across multiple years

The raw dataset contains:

Missing values

Inconsistent observations

Non-overlapping time series

Redundant variables

The project focuses specifically on Somalia to perform deep analysis instead of shallow global analysis.

Objectives

Clean and structure a messy real-world dataset

Filter country-specific observations (Somalia)

Standardize column names and remove irrelevant variables

Investigate missing values and incomplete time series

Analyze staple food price behavior over time

Identify relationships between staple commodities

Prepare the data for future machine learning modeling

Workflow
1. Data Cleaning

Renamed columns for readability

Removed unnecessary identifiers

Converted Month + Year into time index

Filtered Somalia observations

Standardized units and currencies

Investigated missing values (NaN analysis)

2. Exploratory Data Analysis

Price distribution analysis (histograms)

Commodity average price comparison

Time-series price trends

Staple food filtering

Correlation analysis between staple foods

3. Handling Missing Data

Major issue discovered:
Different commodities were recorded in different months.

Solution:

Identified overlapping time periods

Built a “core commodity dataset”

Removed incomplete observations only when necessary

This allowed meaningful comparison across commodities.

Key Findings
Strong Correlation Between Staple Foods

A very high correlation (~0.97) was observed between:

Sorghum (red)

Maize (white)

This suggests:

Shared supply shocks

Linked food markets

Possible substitution behavior in consumption

Price Volatility

Staple food prices show:

Sudden spikes

Long-term inflation trends

Common movement across commodities

This indicates market-wide economic pressure rather than isolated commodity shocks.

Skills Demonstrated

Python (Pandas, Matplotlib, Seaborn)

Data cleaning and transformation

Handling missing values

Feature selection

Time series aggregation

Correlation analysis

Data visualization

Analytical reasoning

Project Structure
Food-Price-Analysis/
│
├── data/
│   └── wfpvam_foodprices.csv
│
├── notebooks/
│   └── analysis.ipynb
│
└── README.md