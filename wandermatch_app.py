import streamlit as st
import pandas as pd
from PIL import Image
import os

# App Title
st.set_page_config(page_title="Travel Recommendation App", layout="wide")
st.title("🌍 Find Your Perfect Travel Destination!")
st.markdown("Discover destinations based on your **mood** and **budget** ✨")

# Load data
df = pd.read_csv("places.csv")

# Sidebar filters
st.sidebar.header("Filter Options 🎯")
selected_mood = st.sidebar.selectbox("Choose your mood", df["Mood"].unique())
selected_budget = st.sidebar.selectbox("Choose your budget", df["Budget"].unique())

# Filter DataFrame
filtered_df = df[
    (df["Mood"].str.lower() == selected_mood.lower()) &
    (df["Budget"].str.lower() == selected_budget.lower())
]

# Display Results
if not filtered_df.empty:
    st.subheader(f"Results for mood **{selected_mood}** and budget **{selected_budget}**")
    for index, row in filtered_df.iterrows():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            img_path = os.path.join("images", row["Image"])
            if os.path.exists(img_path):
                st.image(img_path, caption=row["Place"], use_container_width=True)
            else:
                st.warning("Image not found.")
        
        with col2:
            st.markdown(f"### 📍 {row['Place']}")
            st.markdown(f"💬 {row['Description']}")
            st.markdown(f"🧳 Budget: **{row['Budget']}** | 🌈 Mood: **{row['Mood']}**")
            st.markdown("---")
else:
    st.error("❌ No destinations found. Try changing your mood or budget.")
