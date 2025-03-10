# 📊 Building an Efficient Query System for Multiple CSV Files with LangChain and Groq  

## 🚀 Overview  
This project enables **natural language querying of CSV files** using **LangChain** and **Groq API**.  
Users can upload CSV files and ask **plain English questions**, which are dynamically converted into **Pandas commands** and executed on the dataset.  

## ✨ Features  
✅ **Multi-CSV Support** – Users can upload and analyze multiple CSV files.  
✅ **AI-Powered Querying** – Uses **LangChain** and **Groq API** to convert text queries into executable **Pandas commands**.  
✅ **Data Insights & Visualization** – Supports **aggregations, filtering, and visualizations (histograms, plots, etc.)**.  
✅ **Streamlit UI** – User-friendly interface with drag-and-drop file uploads.  

## 🛠️ Tech Stack  
- **Python** 🐍  
- **Pandas** 🏷️  
- **LangChain** 🧠  
- **Groq API** 🤖  
- **Streamlit** 🎨  

## 📸 Screenshots  
*(Add screenshots here if needed)*  

## 🔧 Installation & Setup  

### 1️⃣ Clone the repository  

```git clone https://github.com/yourusername/Query-System-CSV.git```
```cd Query-System-CSV```

### 2️⃣ Create a virtual environment

```python -m venv venv```

```source venv/bin/activate   # On macOS/Linux```

```venv\Scripts\activate      # On Windows```

### 4️⃣ Set up environment variables

``` Create a .env file in the project root and add: ```

```GROQ_API_KEY=your_groq_api_key```

### 5️⃣ Run the application

```streamlit run app.py```


## 🚀 Usage

### 1️⃣ Upload a CSV file via the Streamlit UI.

### 2️⃣ Ask questions like:

```"Show the first 10 rows of the dataset."```

```"What is the average price of cars by make?"```

```"Create a histogram of car prices."```

### 3️⃣ View results & insights instantly!


## 📌 Future Enhancements

### ✅ Support for multiple CSVs in a single query.
### ✅ Improved query parsing for complex operations.
### ✅ Enhanced data visualizations with Matplotlib and Seaborn.

This project is licensed under the **MIT License**.
 
