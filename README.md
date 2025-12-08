# 🎬 Movie Search App (OMDb API + Streamlit)

A modern **Movie Search Web Application** built using **Python**, **Streamlit**, and the **OMDb API**.  
Enter any movie title and the app displays key details such as poster, year, genre, IMDb rating, and plot summary — wrapped in a clean card-based UI.

---

## 🚀 Features

- 🔍 Search movies by title
- 🎞 Displays:
  - Poster
  - Title & Release Year
  - Genre
  - IMDb Rating
  - Plot Summary
- 🎨 Modern UI with card layout and responsive design
- ⚠ Error handling for invalid or blank search input
- 🔐 Secure API key management using `.env` file

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| Streamlit | Web UI |
| OMDb API | Movie data |
| Requests | API communication |
| python-dotenv | Secure API key handling |

---

## 📦 Project Structure

```bash
MovieSearchApp/
│── main.py # Main Streamlit app
│── .env # Stores OMDB_API_KEY (ignored in Git)
└── README.md
```

---

## 🔐 Environment Setup (.env)

- Create a `.env` file in project root and add:

```bash
env
OMDB_API_KEY=your_api_key_here
```

---

## ▶ How to Run the App

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/tejaskapse1902/movie-search-app-streamlit.git
cd movie-search-app-streamlit
```

### **2️⃣ Install dependencies**

```bash
pip install streamlit requests python-dotenv
```

### **3️⃣ Run the app**

```bash
streamlit run main.py
```

- The app will open in your browser (default: http://localhost:8501)

---

## 🖥 Screenshots

![outputs](/images/1.png)
![outputs](/images/2.png)
![outputs](/images/3.png)
![outputs](/images/4.png)

---

## 🌱 Future Enhancements

- ⭐ Star-rating visualization UI
- 🎭 Multi-movie search results (s= instead of t=)
- 📚 Add "Favorites" / watchlist storage
- ☁ Deployment on Streamlit Cloud

---

## 🤝 Contributing
- Pull requests are welcome. For major changes, please open an issue first.

---

## 🧑‍💻 Author

- Tejas Kapse
- Python Developer — Automation | Streamlit | APIs
- - 🔗 GitHub: https://github.com/tejaskapse1902
- - 🔗 LinkedIn: https://www.linkedin.com/in/tejas-kapse/
- - 📩 Email: tejaskapse19@gmail.com

---