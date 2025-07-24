import streamlit as st

# App Title and Image
st.set_page_config(page_title="WanderMatch", layout="centered")
st.title("🌍 WanderMatch: Your Personal Travel Buddy")

# Show app banner image from GitHub
st.image("https://github.com/vinnu9449/wandermatch-app/raw/main/download.jpg", caption="WanderMatch Travel App")

# Description
st.markdown("""
WanderMatch is a travel planning app designed to match users with the perfect destination based on their mood, budget, and preferences. 
Discover hidden gems, plan within your budget, and travel smart!
""")

# Input Section
st.header("✨ Tell us about your travel plans")

budget = st.selectbox("Select your budget range", ["Low", "Medium", "High"])
destination_type = st.multiselect("What kind of destination do you prefer?", ["Beaches", "Mountains", "Cities", "Nature", "Historical"])
mood = st.radio("What’s your current travel mood?", ["Relaxing", "Adventurous", "Romantic", "Cultural", "Fun with Friends"])

# Matching Logic (placeholder)
if st.button("🔍 Find My Destination"):
    if budget == "Low":
        st.success("🌴 We recommend: **Hampi, India** – A low-budget historical adventure!")
    elif budget == "Medium":
        st.success("🏞️ We recommend: **Manali, India** – Breathtaking mountains and snow!")
    elif budget == "High":
        st.success("🌊 We recommend: **Maldives** – Luxurious beachside getaway!")
    else:
        st.warning("Please choose a budget to get suggestions.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [vin](https://github.com/vinnu9449)")

