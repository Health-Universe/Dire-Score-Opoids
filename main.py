import streamlit as st

# Define function to calculate DIRE score
def calculate_dire_score(diagnosis, intractability, risk, efficacy):
    dire_score = diagnosis + intractability + risk + efficacy
    return dire_score

st.title("DIRE Score for Opioid Treatment")

# User input for Diagnosis score
diagnosis = st.slider("Diagnosis Score (1-7)", min_value=1, max_value=7)

# User input for Intractability score
intractability = st.slider("Intractability Score (1-11)", min_value=1, max_value=11)

# User input for Risk score
risk = st.slider("Risk Score (1-9)", min_value=1, max_value=9)

# User input for Efficacy score
efficacy = st.slider("Efficacy Score (1-9)", min_value=1, max_value=9)

# Calculate DIRE score
if st.button("Calculate DIRE Score"):
    dire_score = calculate_dire_score(diagnosis, intractability, risk, efficacy)
    st.success(f"The DIRE score is: {dire_score}")
