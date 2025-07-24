readme = '''
# 🌍 WanderMatch - Smart Travel Match App

**WanderMatch** helps users find the perfect travel destination based on their preferences like continent, season, and budget.

### 🔧 Built With:
- Python
- Streamlit
- Pandas
- GitHub + Streamlit Cloud for deployment

### 💡 Features:
- Dynamic filtering by Continent, Season & Budget
- Beautiful destination images
- Responsive, clean UI via Streamlit

### 🚀 Live Demo:
[Click to Try the App (after deployment)](https://your-app-link.streamlit.app)

---

### 📸 Screenshot Preview:

![Preview](https://upload.wikimedia.org/wikipedia/commons/5/5b/TanahLot_Bali.JPG)

'''
with open("README.md", "w") as f:
    f.write(readme)

files.download("README.md")

