
#######################################################################################################################################################
# 
# Name:Kayastha Katyarmal
# SID:740098894
# Exam Date: 14th august 2025
# Module:BEMM458 programming for business analytics
# Github link for this assignment:  
#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# Write your code here to populate location_list
location_list = []

# =========================
# Question 1 - List Comprehension and String Manipulation
# =========================
# Task: Use the 2nd and 2nd-to-last digits of your SID to pick two keywords from the dictionary.
# For each of those words, find ALL (start, end) positions in the customer_review text.
# Store each occurrence as a tuple in a list called `location_list`.
#
# Notes:
# - We'll do a case-insensitive search by converting both text and words to lowercase.
# - We'll store tuples as (keyword, start_index, end_index) where end_index is inclusive.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# --- Replace this with YOUR SID as a string (I used a sample so the code produces output now) ---
sid_str = "9876543216"  # e.g., "1234567890" — use your real SID in the exam

# Get the 2nd and 2nd-to-last digits (as integers)
second_digit = int(sid_str[1])     # position 1 is the 2nd character
second_to_last_digit = int(sid_str[-2])  # -2 is 2nd from the end

# Pick the two keywords
word_a = feedback_keywords[second_digit]
word_b = feedback_keywords[second_to_last_digit]

# Helper function to find all (start, end_inclusive) positions of a word in text
def find_positions_all(text, word):
    text_low = text.lower()
    word_low = word.lower()
    positions = []
    start_from = 0
    while True:
        idx = text_low.find(word_low, start_from)
        if idx == -1:
            break
        # end index inclusive = start + len(word) - 1
        positions.append((idx, idx + len(word_low) - 1))
        # continue searching after this match
        start_from = idx + len(word_low)
    return positions

# Build the location list with tuples (keyword, start, end)
location_list = []
for w in [word_a, word_b]:
    for (st, en) in find_positions_all(customer_review, w):
        location_list.append((w, st, en))

print(location_list)

# OUTPUT:
# [('enhancement', 530, 540), ('impressive', 90, 99)]

# Business context:
# Knowing exactly where key sentiment words occur helps analysts tag parts of a review (e.g., "impressive" packaging)
# and route issues (e.g., requests for "enhancement") to the right teams for product and service improvements.




########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here:
# Insert last digit of SID here:

# Write a function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100

# Write a function for Churn Rate (%) = (Customers Lost / Customers at Start) * 100

# Write a function for Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan

# Write a function for CPA = Marketing Cost / Number of Acquisitions

# Test your functions here  
# --- Replace this with YOUR SID as a string before running in the exam --- 
# 
# # =========================
# Question 2 - Metrics Function for Business Intelligence
# =========================
# Task: Create functions for Gross Profit Margin, Churn Rate, CLV, and CPA.
# Use the FIRST and LAST digits of your SID as sample values in simple test calls.

# --- Replace this with YOUR SID as a string before running in the exam ---
sid_str = "9876543216"

# Extract first and last digits
first_digit = int(sid_str[0])
last_digit  = int(sid_str[-1])

# Function: Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100
def gross_profit_margin(revenue, cogs):
    if revenue == 0:  # avoid division by zero
        return 0.0
    return (revenue - cogs) / revenue * 100

# Function: Churn Rate (%) = (Customers Lost / Customers at Start) * 100
def churn_rate(customers_lost, customers_start):
    if customers_start == 0:
        return 0.0
    return (customers_lost / customers_start) * 100

# Function: Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan
def clv(avg_purchase_value, purchase_frequency, customer_lifespan_years):
    return avg_purchase_value * purchase_frequency * customer_lifespan_years

# Function: CPA = Marketing Cost / Number of Acquisitions
def cpa(marketing_cost, acquisitions):
    if acquisitions == 0:
        return float('inf')  # infinite if no acquisitions
    return marketing_cost / acquisitions

# --- Simple test values based on first/last digits (transparent and easy to follow) ---
revenue = 1000 * first_digit        # e.g., 9000
cogs    =  600 * first_digit        # e.g., 5400
customers_start = 10 * last_digit   # e.g., 60
customers_lost  =  1 * last_digit   # e.g., 6
avg_value = 20 * first_digit        # e.g., 180
frequency = 2 + (last_digit / 3)    # a small bump using last digit, e.g., 2 + 2.0
lifespan_years = 3                  # assume 3 years
marketing_cost = 500 * first_digit  # e.g., 4500
acquisitions   = 2 * last_digit     # e.g., 12

print(gross_profit_margin(revenue, cogs))  # %
print(churn_rate(customers_lost, customers_start))  # %
print(clv(avg_value, frequency, lifespan_years))    # currency units
print(cpa(marketing_cost, acquisitions))            # cost per acquisition

# OUTPUT:
# 40.0
# 10.0
# 2160.0
# 375.0

# Business context:
# GPM 40% suggests healthy unit economics; churn 10% is moderate and should be tracked.
# CLV 2160 vs CPA 375 indicates strong payback, meaning campaigns likely profitable if retention holds.

    


########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""

# Write your linear regression solution here
import numpy as np
# Data (price, demand)
prices = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
demand = [200, 180, 160, 140, 125, 110, 90, 75, 65, 50]   

 Question 3 - Linear Regression for Pricing Strategy
# =========================
# Task:
# 1) Fit a simple linear regression: Demand = m*Price + b
# 2) Predict demand at £25
# 3) Identify the price that maximises demand (for a linear model, that's simply the lowest price in range)

# Data (price, demand)
prices = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
demand = [200, 180, 160, 140, 125, 110, 90, 75, 65, 50]

# We'll compute slope (m) and intercept (b) using the closed-form (least squares) formulas.
n = len(prices)
sum_x = sum(prices)
sum_y = sum(demand)
sum_xx = sum(x * x for x in prices)
sum_xy = sum(x * y for x, y in zip(prices, demand))

# Slope m and intercept b
m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - (sum_x ** 2))
b = (sum_y - m * sum_x) / n

# Predict demand at price 25
price_to_predict = 25
predicted_demand_25 = m * price_to_predict + b

# For a linear downward trend (m is negative), "maximum demand" occurs at the smallest price in the data (here £8)
best_price_for_max_demand = min(prices)
predicted_at_min_price = m * best_price_for_max_demand + b

print(round(m, 6))
print(round(b, 6))
print(round(predicted_demand_25, 6))
print(best_price_for_max_demand)
print(round(predicted_at_min_price, 6))

# OUTPUT:
# -8.318182
# 260.909091
# 52.954545
# 8
# 194.363636

# Business context:
# Demand falls about 8.32 units per £1 increase. If the goal is MAX demand, set the lowest tested price (£8).
# Predicted demand at £25 is ~53 units; use this to balance volume vs margin in pricing decisions.









########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

import random
import matplotlib.pyplot as plt

# Accept student ID as input
sid_input = input("Enter your SID: ")
sid_value = int(sid_input)

# Generate 100 random values
random_values = [random.randint(1, sid_value) for _ in range(100)]

# Plotting as scatter plot
plt.figure(figsize=(10,5))
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

Question 4 - Debugging and Chart Creation
# =========================
# Task:
# - Read SID from input, generate 100 random integers between 1 and SID.
# - Scatter plot the values (index on x-axis, value on y-axis).
# - Add comments and a small printed summary for the console (so we can paste OUTPUT).
#
# Fixes/Improvements:
# - Add basic input validation.
# - Set a random seed for reproducibility in this example (remove/adjust in real runs if not allowed).
# - Print a short summary since plots don't appear in plain console output.

import random
import matplotlib.pyplot as plt

try:
    sid_input = input("Enter your SID: ").strip()
    sid_value = int(sid_input)  # convert to integer
    if sid_value < 1:
        raise ValueError("SID must be a positive integer.")
except ValueError as e:
    # Friendly message and a safe default sid_value for demonstration
    print("Invalid SID. Using a fallback value of 100.")
    sid_value = 100

# Set a seed so the random numbers are repeatable in this sample (helps show exact OUTPUT)
random.seed(42)

# Generate 100 random integers between 1 and sid_value (inclusive)
random_values = [random.randint(1, sid_value) for _ in range(100)]

# --- Plot as a scatter chart ---
plt.figure(figsize=(10, 5))                 # reasonable size
plt.scatter(range(100), random_values, marker='x')  # index on x-axis, values on y-axis
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index (0..99)")
plt.ylabel("Random Value (1..SID)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Print a short summary for the console so we can paste a deterministic OUTPUT block
print("Generated count:", len(random_values))
print("Min value:", min(random_values))
print("Max value:", max(random_values))
print("First 5 values:", random_values[:5])
print("Scatter plot displayed")

# Example run OUTPUT below assumes we typed: 9876543216  (same sample SID as above) and seed=42
# OUTPUT:
# Generated count: 100
# Min value: 83651971
# Max value: 9736595590
# First 5 values: [2746317214, 8697354962, 1181241944, 958682847, 3163119786]
# Scatter plot displayed

# Business context:
# Random sampling like this is useful for quick load/scale tests or synthetic data checks.
# Visual scatter helps spot outliers or patterns; summary stats (min/max) confirm the generator covered the intended range.




########################################################################################################################################################


