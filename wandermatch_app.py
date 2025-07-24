
import streamlit as st
import pandas as pd

st.set_page_config(page_title="WanderMatch", page_icon="🌍", layout="centered")
st.title("🌴 WanderMatch: AI-Powered Vacation Recommender")
st.markdown("Find your perfect destination based on your mood and budget 💖")

# Dataset
data = {
    'Destination': ['Goa', 'Manali', 'Udaipur', 'Rishikesh', 'Pondicherry', 'Leh-Ladakh', 'Munnar', 'Andaman Islands', 'Coorg', 'Jaipur'],
    'Mood': ['Chill', 'Adventure', 'Romantic', 'Spiritual', 'Chill', 'Adventure', 'Romantic', 'Chill', 'Romantic', 'Cultural'],
    'Budget': ['Medium', 'Medium', 'Low', 'Low', 'Medium', 'High', 'Low', 'High', 'Low', 'Low'],
    'Image_URL': [
        'https://upload.wikimedia.org/wikipedia/commons/d/d1/Palolem_Beach%2C_Goa.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/d/db/Manali_City_View.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/d/d4/Lake_Pichola_Udaipur.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/3/33/Parmarth_Niketan_Ashram_Rishikesh.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/f/f1/Pondicherry_Beach.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/4/4f/Ladakh_-_Pangong_lake.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e0/Munnar_hillstation_kerala.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/8/84/Andaman_Nicobar_Islands.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/f/f4/Coorg_scenery.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/4/4e/Amber_Fort%2C_Jaipur.jpg'
    ]
}

df = pd.DataFrame(data)

# Sidebar
st.sidebar.header("Tell us about you 😄")
selected_mood = st.sidebar.selectbox("What's your travel mood?", sorted(df['Mood'].unique()))
selected_budget = st.sidebar.selectbox("What's your budget?", sorted(df['Budget'].unique()))

# Filter
filtered = df[(df['Mood'] == selected_mood) & (df['Budget'] == selected_budget)]

# Display
if not filtered.empty:
    st.success(f"🎯 Found {len(filtered)} match(es) for you!")
    for index, row in filtered.iterrows():
        st.subheader(f"🌍 {row['Destination']}")
        st.image(row['Image_URL'], use_column_width=True, caption=f"Perfect for a {row['Mood']} trip")
        st.markdown(f"💰 Budget: **{row['Budget']}**")
        st.markdown("---")
else:
    st.warning("Oops! No match found. Try changing your mood or budget 💭")
