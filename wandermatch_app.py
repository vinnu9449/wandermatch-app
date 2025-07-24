import streamlit as st

# App setup
st.set_page_config(page_title="WanderMatch", layout="centered")
st.title("🌍 WanderMatch: Your Personal Travel Buddy")
st.image("https://github.com/vinnu9449/wandermatch-app/raw/main/download.jpg", caption="WanderMatch Travel App")

# Intro
st.markdown("""
WanderMatch is a travel planning app that suggests perfect destinations based on your **budget**, **mood**, and **travel interests**. 🌏
""")

# User Inputs
st.header("✨ Tell us about your travel plans")

budget = st.selectbox("💰 Select your budget range", ["Low", "Medium", "High"])
destination_type = st.multiselect("📍 Preferred destination types", ["Beaches", "Mountains", "Cities", "Nature", "Historical"])
mood = st.radio("🧠 What’s your travel mood?", ["Relaxing", "Adventurous", "Romantic", "Cultural", "Fun with Friends"])

# Travel suggestions database (very simple logic-based example)
suggestions = {
    "Low": {
        "Relaxing": "🌿 Alleppey, Kerala – Houseboats, lagoons, and calm nature",
        "Adventurous": "🏞️ Rishikesh – River rafting and thrill on a budget",
        "Romantic": "🌸 Coorg – Misty hills and coffee plantations",
        "Cultural": "🏯 Hampi – UNESCO site with rich heritage",
        "Fun with Friends": "🚌 Goa (budget travel) – Beaches, forts, and nightlife"
    },
    "Medium": {
        "Relaxing": "🍃 Ooty – Tea gardens, lakes and cool breeze",
        "Adventurous": "🧗‍♂️ Manali – Trekking and snow adventure",
        "Romantic": "💞 Udaipur – The city of lakes and royal vibes",
        "Cultural": "🎭 Jaipur – Palaces, art, and Rajasthani culture",
        "Fun with Friends": "🎢 Lonavala – Waterfalls, treks and fun resorts"
    },
    "High": {
        "Relaxing": "🌊 Maldives – Private villas and turquoise waters",
        "Adventurous": "🏔️ Leh-Ladakh – Biker’s dream and sky-high peaks",
        "Romantic": "🏝️ Bora Bora – Blue lagoon paradise",
        "Cultural": "🎨 Kyoto, Japan – Temples, traditions and tea",
        "Fun with Friends": "🎉 Bali – Fun beaches, volcanoes and clubs"
    }
}

# Show Result
if st.button("🔍 Find My Destination"):
    recommendation = suggestions[budget][mood]
    st.success(f"✨ Based on your preferences, we recommend:\n\n{recommendation}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [vin](https://github.com/vinnu9449)")
