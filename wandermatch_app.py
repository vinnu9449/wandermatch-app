import streamlit as st
import pandas as pd
from PIL import Image

# Page settings
st.set_page_config(page_title="WanderMatch", page_icon="🌍", layout="centered")

# Load image
image = Image.open("travel_banner.png")
st.image(image, use_column_width=True)

# Title and description
st.title("🌍 WanderMatch: Find Your Travel Soulmate")
st.markdown("Welcome to **WanderMatch**, the fun way to match your travel style with a perfect destination!")

# Load destination data
df = pd.read_csv("wander_data.csv")

# User preferences
st.sidebar.header("🎯 Choose your preferences")
climate = st.sidebar.selectbox("Preferred Climate", df['Climate'].unique())
budget = st.sidebar.slider("Budget (USD)", 200, 3000, 1500)
interest = st.sidebar.selectbox("Your Interest", df['Interest'].unique())

# Filter destinations
filtered_df = df[(df['Climate'] == climate) & 
                 (df['Cost'] <= budget) & 
                 (df['Interest'] == interest)]

# Show results
if not filtered_df.empty:
    st.success(f"✨ We found {len(filtered_df)} destination(s) for you!")
    for _, row in filtered_df.iterrows():
        st.subheader(row['Destination'])
        st.markdown(f"**Country:** {row['Country']}  \n"
                    f"**Climate:** {row['Climate']}  \n"
                    f"**Estimated Cost:** ${row['Cost']}  \n"
                    f"**Interest:** {row['Interest']}")
        st.markdown("---")
else:
    st.warning("Oops! No destinations match your choices. Try changing your filters.")
