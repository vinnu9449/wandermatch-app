import streamlit as st
import pandas as pd
import random
from PIL import Image

# Set page config
st.set_page_config(page_title="WanderMatch - Plan Your Dream Trip", layout="centered")

# Custom header
st.markdown("<h1 style='text-align: center; color: #0099ff;'>🌍 WanderMatch: Your Travel Buddy</h1>", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("places.csv")

# Sidebar inputs
st.sidebar.header("✨ Personalize Your Trip")
budget = st.sidebar.selectbox("Select your budget level:", ["Low", "Medium", "High"])
interest = st.sidebar.multiselect("What do you enjoy?", ["Beach", "Mountains", "City", "Heritage", "Wildlife"])

# Button to generate recommendations
if st.sidebar.button("🎒 Show Me My Places!"):
    st.subheader("🌟 Top Destination Matches for You:")

    filtered_df = df[(df['budget'].str.lower() == budget.lower())]

    if interest:
        filtered_df = filtered_df[filtered_df['type'].isin(interest)]

    if not filtered_df.empty:
        top_recommendations = filtered_df.sample(n=min(3, len(filtered_df)))

        for _, row in top_recommendations.iterrows():
            st.markdown(f"### {row['name']}, {row['country']}")
            st.markdown(f"**Type:** {row['type']}  |  **Budget:** {row['budget']}")
            st.markdown(f"📍 {row['description']}")
            st.image(row['image'], width=600)
            st.markdown("---")
    else:
        st.warning("🙁 Sorry, we couldn’t find any destinations matching your preferences. Try adjusting your options!")

else:
    st.markdown("💡 Use the sidebar to get personalized travel suggestions!")

# Footer
st.markdown("<br><hr><center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)
