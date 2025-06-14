# Tjenare 🖥️

**Tjenare** is my personal website and data project that combines web development with personal interests and quantified self data. It showcases training and health data from devices like WHOOP and COROS, visualized directly in the browser with custom dashboards and charts.

## 🔍 Features

- 💪 **Fitness Dashboards**: Visualizations of WHOOP and COROS training data using Chart.js
- 📊 **PostgreSQL Integration**: Backend fitness data pipeline stores processed health data in a database
- 🧶 **Personal Sections**: Pages dedicated to hobbies like drawing and baking
- 🌐 **Modern Web Stack**: Built with HTML, CSS, and JavaScript
- 🎨 **Custom Design**: Responsive UI with custom styling and navigation

## 📁 Project Structure

```
Tjenare/
├── assets/
│   ├── css/
│   ├── images/
│   ├── json/
├── data/  # Processed CSV data
├── pages/
│   ├── bake.html
│   ├── coros.html
│   ├── crochet.html
│   ├── draw.html
│   ├── index.html
│   ├── train.html
│   ├── watch.html
│   └── whoop.html
├── .gitignore
└── README.md
```


## 🧠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend/Data**: Python, Pandas, Jupyter Notebooks
- **Database**: PostgreSQL
- **Other Tools**: dbt, SQLAlchemy (for pipelines), fitparse

## ⚙️ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/tjenare.git

2. Open `index.html` in a browser to explore the site (I use the **Live server** extension in VS Code to view the website)

3. If using data visualizations:
    
    - Make sure your database is running  
    - Configure your pipeline and connect to PostgreSQL  
    - Export data to the `data/` folder for frontend use

## 🚀 Future Plans

- General work on the crochet and baking pages
- Add the data from my COROS watch
    - Automate the data pipeline
- Expand visualization options (e.g., maps from GPS data)