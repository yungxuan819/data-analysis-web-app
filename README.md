# 📊 Data Analysis Web App

A no-code **data analysis web app** built with Python and Streamlit. Upload any CSV file and instantly explore, clean, filter, and visualize your dataset — no coding required.

🔗 **Live App: [yxdataanalysiswebapp.streamlit.app](https://yxdataanalysiswebapp.streamlit.app/)**

---

## 📁 Project Structure

```
data-analysis-web-app/
│
├── DAWebApp.py        # Main Streamlit app
├── requirements.txt   # Python dependencies
└── README.md
```

---

## ✨ Features

### 📂 Upload & Preview
- Upload any CSV dataset directly in the browser
- Preview the first rows (**Head**) or last rows (**Tail**) of the dataset

### 📋 Dataset Overview
- View the **data type** of each column
- Check the **number of rows and columns** via an interactive radio selector
- Generate a full **summary statistics** table (mean, std, min, max, etc.) for all columns

### 🔍 Data Quality Checks
- **Missing values** — detects whether any null values exist, highlights affected rows, and shows a count
- **Duplicate detection** — identifies duplicate rows and gives the option to remove them interactively

### 🔎 Data Filtering
- Filter the dataset by selecting any column and choosing a specific value to display matching rows

### 📈 Visualizations
- **Bar Chart** — select X and Y axis columns; automatically validates compatible column types
- **Scatter Plot** — plot any two columns against each other
- **Histogram** — visualize value distributions with an adjustable bin slider
- **Correlation Heatmap** — shows correlations between all numeric columns with annotated colour-coded values

---

## 🚀 Getting Started

### Run Locally

```bash
git clone https://github.com/yungxuan819/data-analysis-web-app.git
cd data-analysis-web-app
pip install -r requirements.txt
streamlit run DAWebApp.py
```

Then open your browser at `http://localhost:8501`.

### Or Use the Live App

No setup needed — just visit **[yxdataanalysiswebapp.streamlit.app](https://yxdataanalysiswebapp.streamlit.app/)** and upload your CSV.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web app framework |
| pandas | Data loading, cleaning & filtering |
| seaborn | Statistical visualizations |
| matplotlib | Plot rendering |
| plotly | Interactive charting |
