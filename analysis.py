#!/usr/bin/env python
# coding: utf-8

# Load Libraries first

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data

# In[3]:


df = pd.read_csv(r"C:\Users\abdin\Desktop\Food-Price-Analysis\Data\wfpvam_foodprices.csv")


# Check the Somalia, ag galance

# In[4]:


somalia_df = df[df["adm0_name"] == "Somalia"].copy()

print(somalia_df.shape)
somalia_df.head()


# check all columns and see which ones to drop and which ones to keep

# In[5]:


somalia_df.columns


# Columns to Drop

# In[6]:


drop_columns = ['adm0_id',
                'adm1_id',
                'mkt_id',
                'cm_id',
                'cur_id',
                'pt_id',
                'um_id',
                'mp_commoditysource']


# Columns to keep

# In[7]:


keep_columns = [ "adm0_name",
    "adm1_name",
    "mkt_name",
    "cm_name",
    "cur_name",
    "um_name",
    "mp_year",
    "mp_month",
    "mp_price"]
somalia_df = somalia_df[keep_columns]
somalia_df


# Renaming and giving it to proper names

# In[8]:


somalia_df.rename(columns={
    "adm0_name": "Country",
    "adm1_name": "Region",
    "mkt_name": "Market",
    "cm_name": "Commodity",
    "cur_name": "Currency",
    "um_name": "Unit",
    "mp_year": "Year",
    "mp_month": "Month",
    "mp_price": "Price"
}, inplace= True)
somalia_df


# Only Show somalia

# In[9]:


somalia_df = somalia_df[somalia_df["Country"] == "Somalia"].copy()

print(somalia_df.shape)
somalia_df.head()


# In[10]:


somalia_df[["Commodity", "Price"]].value_counts().head(30)


# How many times that the Commodity contents show in the document

# In[11]:


somalia_df["Commodity"].value_counts().head(25)


# Counting the Units against the Commodity

# In[12]:


somalia_df[["Unit", "Commodity" ]].value_counts().head(20)


# Commodity mean

# In[13]:


commodity_price = (
    somalia_df
    .groupby("Commodity")["Price"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

commodity_price.head(25)


# Calculate Mean for the Commidity against the the Price:

# In[14]:


somalia_df.groupby("Commodity")["Price"].mean()


# In[15]:


somalia_df[["Region", "Commodity", "Unit"]].value_counts().head(20)


# In[16]:


somalia_df.groupby("Commodity")["Region"].value_counts().head(50)


# In[17]:


wheat_df = somalia_df[somalia_df["Commodity"] == "Wheat flour - Retail"].copy()


# In[18]:


wheat_df["Date"] = pd.to_datetime(
    wheat_df["Year"].astype(str) + "-" + wheat_df["Month"].astype(str) + "-01"
)


# In[19]:


wheat_df[["Year","Month","Date"]].head(10)


# Price of Wheat overtime

# In[20]:


monthly_price = (
    wheat_df
    .groupby("Date")["Price"]
    .mean()
    .reset_index()   
)
monthly_price


# In[21]:


plt.figure(figsize=(12,5))
plt.plot(monthly_price['Date'], monthly_price["Price"])
plt.title("Average Wheat Flour Price Overtime")
plt.xlabel ("Year")
plt.ylabel("Prices ShS Per KG")
plt.grid (True)
plt.show()


# In[22]:


plt.figure(figsize=(6,3))

plt.hist(
    wheat_df["Price"],
    bins=50,
    color="steelblue",
    edgecolor="white",
    alpha=1
)

plt.title("Distribution of Wheat Flour Prices", fontsize=13)
plt.xlabel("Price (SOS per KG)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()


# Average Commodity Price in Somalia

# In[23]:


commodity_avg = somalia_df.groupby("Commodity")["Price"].mean().sort_values(ascending=False)
commodity_avg.head(10)


# In[ ]:





# In[24]:


staples = [
     "Rice (imported) - Retail",
    "Wheat flour - Retail",
    "Wheat flour (imported) - Retail",
    "Maize (white) - Retail",
    "Sorghum (red) - Retail",
    "Sorghum (white) - Retail"
]
staple_df = somalia_df[somalia_df["Commodity"].isin(staples)].copy()


# In[25]:


commodity_avg = staple_df.groupby("Commodity")["Price"].mean().sort_values(ascending=False)


# In[26]:


plt.Figure(figsize=(8,4))
commodity_avg.plot(
    kind="bar",
    color="teal",
    edgecolor="White"
)

plt.title("Average Staple Food Prices in Somalia")
plt.xlabel("Commodity", size=14, color="teal")
plt.ylabel("Average Price (SOS per KG)", size=14, color="teal")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[27]:


staple_df["Date"] = pd.to_datetime(
    staple_df["Year"].astype(str) +"-" + staple_df["Month"].astype(str) + "-01"
)


# In[28]:


monthly_trend = (
    staple_df
    .groupby(["Date", "Commodity"])["Price"]
    .mean()
    .reset_index()
)


# In[29]:


plt.figure(figsize=(10,5))

for commodity in monthly_trend["Commodity"].unique():

    subset = monthly_trend[monthly_trend["Commodity"] == commodity]
    plt.plot(subset["Date"], subset["Price"], label=commodity)

plt.title("Monthly Staple Food Prices in Somalia")
plt.xlabel("Year")
plt.ylabel("Price (SOS per KG)")
plt.legend()
plt.tight_layout()
plt.show()


# In[30]:


price_table = monthly_trend.pivot(
    index= "Date",
     columns= "Commodity",
    values= "Price"

)
price_table.head()


# In[31]:


corr_matrix = price_table.corr()
corr_matrix


# In[32]:


price_table.shape


# In[33]:


price_table.isna().sum()


# In[34]:


price_recent = price_table.loc["2007-01-01":]
price_recent = price_recent.dropna(axis=0, how="any")

price_recent.shape


# In[35]:


core_commodities = [
    "Maize (white) - Retail",
    "Rice (imported) - Retail",
    "Sorghum (red) - Retail"
]

price_core = price_table[core_commodities]


# In[36]:


price_core = price_core.dropna()
price_core.shape


# In[37]:


corr_matrix = price_core.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation of Core Staple Foods in Somalia")
plt.tight_layout()
plt.show()

