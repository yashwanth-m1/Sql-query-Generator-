# AI SQL Query Generator 🤖

**Live Demo:** [AI SQL Query Generator on Streamlit](https://yashwanth-m1-sql-query-generator--app-fnfvr2.streamlit.app/)

## 📖 Project Overview
This project is an AI-powered web application that allows users to write natural language questions and instantly converts them into accurate SQL queries. It automatically executes the generated SQL query against a local SQLite database containing student records and displays the results in a clean, user-friendly interface.

## ✨ Features
* **Natural Language to SQL:** Uses the powerful Google Gemini AI to translate everyday English questions into precise SQL syntax.
* **Instant Execution:** Automatically runs the produced query against a built-in SQLite database and displays the retrieved data.
* **Interactive UI:** Built with Streamlit for a fast, responsive, and seamless user experience.
* **Database Feedback:** Clearly shows the structure of the database the user is querying and safely guards against API and database errors.

## 🛠️ Technology Stack
* **Frontend/Backend:** Python & [Streamlit](https://streamlit.io/)
* **AI Model:** [Google Gemini 2.5 Flash](https://ai.google.dev/) (via the modern `google-genai` SDK)
* **Database:** SQLite (`sqlite3`)

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yashwanth-m1/Sql-query-Generator-.git
cd Sql-query-Generator-
```

### 2. Install Dependencies
Make sure you have Python installed. Install the required libraries via `pip`:
```bash
pip install -r requirements.txt
```

### 3. Setup Your Google API Key
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
GOOGLE_API_KEY="your_api_key_here"
```

### 4. Initialize the Database
Before running the main app, you might need to create the database and insert sample records:
```bash
python sql.py
```
*(This script creates a table named `student` inside `student.db` and populates it with some dummy student data).*

### 5. Launch the Application
Start the Streamlit development server:
```bash
streamlit run app.py
```
The application will open automatically in your browser at `http://localhost:8501`.

---
*Created by Yashwanth*