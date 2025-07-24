import streamlit as st
import pandas as pd
import random

# Load dataset
df = pd.read_csv("places.csv")

# Title and description
st.title("🌍 WanderMatch")
st.subheader("Find your next dreamy travel destination!")

# User input
budget = st.selectbox("Select your budget", ["Low", "Medium", "High"])
climate = st.selectbox("Preferred climate", ["Cold", "Moderate", "Hot"])
activity = st.selectbox("What do you prefer?", ["Mountains", "Beaches", "Cultural", "Adventure", "Relaxation"])

# Filter dataset based on input
filtered = df[
    (df["Budget"].str.lower() == budget.lower()) &
    (df["Climate"].str.lower() == climate.lower()) &
    (df["Activity"].str.lower() == activity.lower())
]

# Recommendation logic
if not filtered.empty:
    st.success("We recommend the following places for you! 🎒✈️")
    
    # Show up to 3 random places
    num_to_show = min(3, len(filtered))
    recommendations = filtered.sample(n=num_to_show)

    for i, row in recommendations.iterrows():
        st.markdown(f"### 📍 {row['Place']}, {row['Country']}")
        st.markdown(f"*{row['Description']}*")
        if 'Image_URL' in row and pd.notnull(row['Image_URL']):
            st.image(row['Image_URL'], use_column_width=True)
else:
    st.error("Oops! No matching places found. Try different options.")
