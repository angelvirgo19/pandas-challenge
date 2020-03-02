#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


filename = "Resources/purchase_data.csv"
purchase_analysis = pd.read_csv(filename)
purchase_analysis


# In[3]:


# checking if the data is clean:

purchase_analysis.count()


# In[4]:


# Player Count:

columns = ["Purchase ID", "SN", "Age", "Gender", "Item ID", "Item Name", "Price"]
Total_Players = len(purchase_analysis["SN"].value_counts())
Total_Players


# In[5]:


# Display the total number of players:

Total_count = pd.DataFrame({"Total Players": [Total_Players]})
Total_count


# In[6]:


# Purchasing Analysis (Total)
#Run basic calculations to obtain number of unique items, average price, etc.



Unique_Items = len(purchase_analysis["Item ID"].value_counts())
Unique_Items


# In[7]:


# alternatively I could print all the values together by using print()

# Unique_Items = len(purchase_analysis["Item ID"].value_counts())
# print(Unique_Items)

# Total_Items_Purchased = purchase_analysis["Item ID"].count()
# Total_Items_Purchased


# In[8]:


Total_Items_Purchased = purchase_analysis["Item ID"].count()
Total_Items_Purchased


# In[9]:


Total_Price = purchase_analysis["Price"].sum()
Total_Price


# In[10]:


Average_price = Total_Price / Total_Items_Purchased
Average_price


# In[11]:


Total_Population = purchase_analysis["SN"].count()
Total_Population


# In[12]:


#Create a summary data frame to hold the results:

Summary_Table_df = pd.DataFrame({"Number of Unique Items": [Unique_Items],
                             "Average Price": [Average_price],
                             "Number of Purchases": [Total_Items_Purchased],
                             "Total Revenue": [Total_Price]}) 
Summary_Table_df


# In[13]:


# Optional: give the displayed data cleaner formatting:
# Display the summary data frame:

Summary_Table_df.style.format({'Average Price':"${:,.2f}",
                         'Total Revenue': '${:,.2f}'})


# In[14]:


# Gender Demographics:
# Count of Male Players
# Count of Female Players
# Count of Other / Non-Disclosed

Gender_analysis = purchase_analysis.groupby("Gender")

total_count_bygender = Gender_analysis.nunique()["SN"]
total_count_bygender


# In[15]:


# Percentage Of Male Players, Female Players and Other/Non-Disclosed Players:

Percentage_players = total_count_bygender / Total_Players * 100
Percentage_players


# In[16]:


# Gender Demographics Display:
Percentage_players = total_count_bygender / Total_Players *100

Gender_Demo_df= pd.DataFrame({ "Total Count": total_count_bygender, "Percentage of Players": Percentage_players})


Gender_Demo_df.index.name = None

Gender_Demo_df


# In[17]:


#Formatting the Gender Demographics Table:

Gender_Demo_df.style.format({'Percentage of Players':"{:,.2f}%"})


# In[18]:


# Purchasing Analysis (Gender):
# Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender

Gender_analysis = purchase_analysis.groupby("Gender")

Total_purchasecount_bygender = Gender_analysis.count()["Item ID"]
Total_purchasecount_bygender


# In[19]:


Total_price_bygender = Gender_analysis.sum()["Price"]
Total_price_bygender


# In[20]:


Avg_purchase_price = Total_price_bygender / Total_purchasecount_bygender
Avg_purchase_price


# In[21]:


AvgTotalPur_perperson = Total_price_bygender/ total_count_bygender
AvgTotalPur_perperson


# In[22]:


# Create a summary data frame to hold the results:

Purchasing_analysis_gendersummary_df = pd.DataFrame({"Purchase Count" : Total_purchasecount_bygender,
                                              "Average Purchase Price": Avg_purchase_price,
                                              "Total Purchase Value": Total_price_bygender,
                                              "Average Total Purchase per Person": AvgTotalPur_perperson})
Purchasing_analysis_gendersummary_df


# In[23]:


# Optional: give the displayed data cleaner formatting:
# Display the summary data frame:


Purchasing_analysis_gendersummary_df.style.format({'Average Purchase Price':"${:,.2f}",
                                                   'Total Purchase Value':"${:,.2f}",
                                                   'Average Total Purchase per Person':"${:,.2f}"})


# In[24]:


# Age Demographics

# Establish bins for ages:

bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[25]:


# Categorize the existing players using the age bins. Hint: use pd.cut()

purchase_analysis["Age Ranges"] = pd.cut(purchase_analysis["Age"], bins, labels=group_names)
purchase_analysis


# In[26]:


# Calculate the numbers and percentages by age group

Age_GroupPurchase = purchase_analysis.groupby("Age Ranges")

Totalcount_age = Age_GroupPurchase["SN"].nunique()
Totalcount_age


# In[27]:


Percent_byage = (Totalcount_age/Total_Players) * 100
Percent_byage


# In[28]:


# Create a summary data frame to hold the results:

Age_Demo = pd.DataFrame({"Total Count": Totalcount_age, "Percentage of Players": Percent_byage })
Age_Demo


# In[29]:


# Optional: round the percentage column to two decimal points
# Display Age Demographics Table

Age_Demo.style.format({"Percentage of Players":"{:,.2f}%"})


# In[30]:


# validating that it includes all data:
sum(Totalcount_age)


# In[31]:


# Purchase Analysis (Age):
# Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


# In[32]:


# Bin the purchase_data data frame by age:
purchase_analysis


# In[33]:


# Average Purchase Price

Total_purchasecount_byage = Age_GroupPurchase.count()["Item ID"]
Total_purchasecount_byage


# In[34]:


# Total Purchase Value

Total_price_byage = Age_GroupPurchase.sum()["Price"]
Total_price_byage


# In[35]:


Avg_purchase_price_age = Total_price_byage / Total_purchasecount_byage
Avg_purchase_price_age


# In[36]:


# Average Purchase Total per Person by Age Group

AvgTotalPur_perperson_age = Total_price_byage/ Totalcount_age
AvgTotalPur_perperson_age


# In[37]:


# Create a summary data frame to hold the results

Purchasing_analysis_agerange_summary_df = pd.DataFrame({"Purchase Count" : Total_purchasecount_byage,
                                              "Average Purchase Price": Avg_purchase_price_age,
                                              "Total Purchase Value": Total_price_byage,
                                              "Average Total Purchase per Person": AvgTotalPur_perperson_age})

Purchasing_analysis_agerange_summary_df


# In[38]:


# Optional: give the displayed data cleaner formatting
# Display the summary data frame

Purchasing_analysis_agerange_summary_df.style.format({'Average Purchase Price':"${:,.2f}",
                                                   'Total Purchase Value':"${:,.2f}",
                                                   'Average Total Purchase per Person':"${:,.2f}"})


# In[39]:


# Top Spenders
# Run basic calculations to obtain the results in the table below


# In[40]:


Purchasecount_topSpenders = purchase_analysis.groupby("SN")

Total_count_perperson = Purchasecount_topSpenders.count()["Purchase ID"]
Total_count_perperson


# In[41]:


max(Total_count_perperson)


# In[42]:


Average_purchaseprice_topspenders = Purchasecount_topSpenders["Price"].mean()
Average_purchaseprice_topspenders


# In[43]:


Total_purchasevalue_topspenders = Purchasecount_topSpenders["Price"].sum()
Total_purchasevalue_topspenders


# In[44]:


## Create a summary data frame to hold the results

Top_Spenders = pd.DataFrame({"Purchase Count": Total_count_perperson,
                             "Average Purchase Price": Average_purchaseprice_topspenders,
                             "Total Purchase Value":Total_purchasevalue_topspenders})
Top_Spenders


# In[45]:


# Sort the total purchase value column in descending order:

Sorted_TopSpenders = Top_Spenders.sort_values(["Total Purchase Value"], ascending = False)
Sorted_TopSpenders


# In[46]:


# Top 5 Spenders:

Sorted_TopSpenders.head()


# In[47]:


# Optional: give the displayed data cleaner formatting:
# Display a preview of the summary data frame:

Sorted_TopSpenders.head().style.format({"Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})


# In[48]:


# Most Popular Items
# Retrieve the Item ID, Item Name, and Item Price columns
# Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value



# In[49]:


Most_popular_item = purchase_analysis.groupby(["Item ID", "Item Name"])

purchased_items = Most_popular_item["Purchase ID"].count()
purchased_items


# In[50]:


Total_value = Most_popular_item["Price"].sum()
Total_value


# In[51]:


Item_price = Total_value/purchased_items
Item_price


# In[52]:


# Create a summary data frame to hold the results

Popular_Items = pd.DataFrame({"Purchase Count": purchased_items , 
                              "Item Price": Item_price, 
                              "Total Purchase Value" : Total_value})
Popular_Items


# In[53]:


# Sort the purchase count column in descending order

Sorted_Popular_Items_bycount = Popular_Items.sort_values(["Purchase Count"], ascending = False)
Sorted_Popular_Items_bycount.head()


# In[54]:


# Optional: give the displayed data cleaner formatting
# Display a preview of the summary data frame

Sorted_Popular_Items_bycount.head().style.format({"Item Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})


# In[55]:


# Sort the above table by total purchase value in descending order

Sorted_Popular_Items_bypurchasevalue = Popular_Items.sort_values(["Total Purchase Value"], ascending = False)
Sorted_Popular_Items_bypurchasevalue.head()


# In[56]:


# Optional: give the displayed data cleaner formatting
# Display a preview of the data frame

Sorted_Popular_Items_bypurchasevalue.head().style.format({"Item Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})


# In[ ]:




