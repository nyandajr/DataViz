import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("mobile.csv")

# Title of the Streamlit app
st.title("Mobile Money Usage Analysis")

# Sidebar for filtering options (if needed)
st.sidebar.title("Filters")

# Visualization 1: Age Distribution
if st.sidebar.checkbox("Age Distribution"):
    st.subheader("Age Distribution")
    age_hist = plt.hist(data["Age"], bins=20, color='skyblue', alpha=0.7)
    plt.xlabel("Age")
    plt.ylabel("Count")
    st.pyplot(plt.gcf())  # Pass the current figure explicitly

# Visualization 2: Gender Distribution
if st.sidebar.checkbox("Gender Distribution"):
    st.subheader("Gender Distribution")
    gender_counts = data["Gender"].value_counts()
    st.bar_chart(gender_counts)

# Visualization 3: Employment Status
if st.sidebar.checkbox("Employment Status"):
    st.subheader("Employment Status")
    employment_status_counts = data["Government Employed"].value_counts()
    st.bar_chart(employment_status_counts)

# Visualization 4: Marital Status
if st.sidebar.checkbox("Marital Status"):
    st.subheader("Marital Status")
    marital_status_counts = data["Marital Status"].value_counts()
    st.bar_chart(marital_status_counts)

# Visualization 5: Monthly Mobile Money Transactions
if st.sidebar.checkbox("Monthly Mobile Money Transactions"):
    st.subheader("Monthly Mobile Money Transactions")
    fig, ax = plt.subplots()
    sns.histplot(data["Monthly Mobile Money Transaction"], bins=20, color='green', kde=True, ax=ax)
    ax.set_xlabel("Transaction Amount")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Visualization 6: Frequency of Mobile Money Usage
if st.sidebar.checkbox("Frequency of Mobile Money Usage"):
    st.subheader("Frequency of Mobile Money Usage")
    fig, ax = plt.subplots()
    sns.histplot(data["Frequency of Mobile Money Usage"], bins=10, color='orange', kde=True, ax=ax)
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# Additional Visualizations

# Visualization 7: Transaction Amount for Government Employed vs. Non-Government Employed
if st.sidebar.checkbox("Transaction Amount for Government Employed vs. Non-Government Employed"):
    st.subheader("Transaction Amount for Government Employed vs. Non-Government Employed")
    sns.set_style("whitegrid")
    fig, ax = plt.subplots()
    sns.boxplot(x="Government Employed", y="Monthly Mobile Money Transaction", data=data, palette="Set3", ax=ax)
    ax.set_xlabel("Employment Status")
    ax.set_ylabel("Transaction Amount")
    st.pyplot(fig)

# Visualization 8: Transaction Amount vs. Age
if st.sidebar.checkbox("Transaction Amount vs. Age"):
    st.subheader("Transaction Amount vs. Age")
    fig, ax = plt.subplots()
    sns.scatterplot(x="Age", y="Monthly Mobile Money Transaction", data=data, hue="Gender", palette="viridis", ax=ax)
    ax.set_xlabel("Age")
    ax.set_ylabel("Transaction Amount")
    st.pyplot(fig)



# Data Table
st.subheader("Dataset")
st.write(data)
