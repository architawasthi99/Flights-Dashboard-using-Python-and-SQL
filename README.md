# ✈️ Flight Dashboard

An interactive **Flight Data Analysis Dashboard** built using **Python, SQL, MySQL, Pandas, and Streamlit**.

The project focuses on analyzing flight data stored in a MySQL database and presenting meaningful insights through an interactive Streamlit dashboard.

---

## 📌 Project Overview

The Flight Dashboard analyzes flight-related data to understand patterns in:

* ✈️ Airlines
* 🛫 Source and destination
* 💰 Ticket prices
* ⏱️ Flight duration
* 🔄 Number of stops
* 🕐 Departure and arrival times
* 📅 Journey dates
* 🛩️ Flight routes

SQL is used for querying and analyzing the data stored in **MySQL**, while Python is used for data processing and visualization. **Streamlit** is used to build the interactive dashboard.

---

## 🛠️ Tech Stack

| Technology             | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| Python                 | Data processing and application development |
| SQL                    | Data analysis and querying                  |
| MySQL                  | Database                                    |
| MySQL Connector/Python | Python–MySQL connection                     |
| Pandas                 | Data manipulation and analysis              |
| Matplotlib             | Data visualization                          |
| Seaborn                | Statistical visualization                   |
| Streamlit              | Interactive dashboard                       |
| Jupyter Notebook       | Exploratory data analysis                   |
| Git & GitHub           | Version control                             |

> **Note:** This project does not use SQLAlchemy. Python connects to MySQL using `mysql-connector-python`.

---

## 📊 Dataset

The dataset used in this project is the **Plane Ticket Price** dataset available on Kaggle.

🔗 **Dataset:**
https://www.kaggle.com/datasets/ibrahimelsayed182/plane-ticket-price

The dataset contains **10,683 flight records and 11 columns**.

### Dataset Columns

| Column            | Description                   |
| ----------------- | ----------------------------- |
| `Airline`         | Name of the airline           |
| `Date_of_Journey` | Date of the journey           |
| `Source`          | Starting location             |
| `Destination`     | Destination location          |
| `Route`           | Flight route                  |
| `Dep_Time`        | Departure time                |
| `Arrival_Time`    | Arrival time                  |
| `Duration`        | Total flight duration         |
| `Total_Stops`     | Number of stops               |
| `Additional_Info` | Additional flight information |
| `Price`           | Ticket price                  |

---

## 🗄️ Database

MySQL is used as the database for storing and querying the flight data.

Example database:

```sql
CREATE DATABASE flight_db;
```

Example table:

```sql
CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    airline VARCHAR(100),
    date_of_journey DATE,
    source VARCHAR(100),
    destination VARCHAR(100),
    route VARCHAR(255),
    dep_time VARCHAR(50),
    arrival_time VARCHAR(50),
    duration VARCHAR(50),
    total_stops VARCHAR(50),
    additional_info VARCHAR(255),
    price DECIMAL(10,2)
);
```

---

## 🔌 Python–MySQL Connection

The project uses **MySQL Connector/Python** to connect Python with MySQL.

Example:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="flight_db"
)

print("Connected to MySQL successfully!")
```

---

## 📈 SQL Analysis

SQL queries are used to extract insights from the database.

Example:

```sql
SELECT
    airline,
    COUNT(*) AS total_flights
FROM flights
GROUP BY airline
ORDER BY total_flights DESC;
```

Other analysis includes:

* Total number of flights
* Flights by airline
* Flights by source
* Flights by destination
* Average ticket price
* Minimum and maximum ticket price
* Average flight duration
* Flights by number of stops
* Most common routes
* Airline-wise pricing
* Source and destination analysis

---

## 🐍 Python & Pandas

Python and Pandas are used for:

* Data loading
* Data cleaning
* Data transformation
* Exploratory Data Analysis
* Processing SQL results
* Preparing data for visualization

Example:

```python
import pandas as pd

query = "SELECT * FROM flights"

df = pd.read_sql(query, conn)

print(df.head())
```

---

## 📊 Streamlit Dashboard

The final dashboard is built using **Streamlit**.

### Dashboard Features

#### 🔢 Key Metrics

* Total Flights
* Total Airlines
* Average Ticket Price
* Average Flight Duration
* Total Routes

#### 🎛️ Filters

Users can filter the dashboard by:

* Airline
* Source
* Destination
* Number of Stops
* Price Range

#### 📉 Visualizations

The dashboard will include visualizations such as:

* Flights by Airline
* Flights by Source
* Flights by Destination
* Average Price by Airline
* Price Distribution
* Flight Duration Analysis
* Stops Analysis
* Popular Routes

---

## 📂 Project Structure

```text
Flight-dashboard/
│
├── data/
│   └── flights.csv
│
├── notebooks/
│   └── flight_analysis.ipynb
│
├── sql/
│   └── queries.sql
│
├── crud.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Flight-dashboard.git
```

```bash
cd Flight-dashboard
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
pandas
numpy
mysql-connector-python
streamlit
matplotlib
seaborn
jupyter
```

---

### 4. Create the MySQL Database

Open MySQL Workbench and run:

```sql
CREATE DATABASE flight_db;
```

Then create the required table and import the dataset.

---

### 5. Configure MySQL Connection

Update the database credentials in your Python file:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="flight_db"
)
```

**Never upload your actual database password to GitHub.**

---

### 6. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 🔐 Security

Do not commit sensitive information such as:

* MySQL passwords
* API keys
* `.env` files
* Streamlit secrets

Add the following to `.gitignore`:

```text
venv/
__pycache__/
*.pyc
.env
.streamlit/secrets.toml
```

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Understand and clean flight data.
2. Store structured data in MySQL.
3. Practice SQL queries and aggregations.
4. Connect Python with MySQL.
5. Analyze data using Pandas.
6. Create meaningful visualizations.
7. Build an interactive dashboard using Streamlit.
8. Practice Git and GitHub workflow.

---

## 🔮 Future Improvements

* [ ] Add more interactive filters
* [ ] Add advanced route analysis
* [ ] Add price prediction
* [ ] Add flight search functionality
* [ ] Add more dashboard pages
* [ ] Add interactive maps
* [ ] Deploy the Streamlit application
* [ ] Add automated data updates
* [ ] Improve dashboard UI/UX

---

## 👨‍💻 Author

**Archit Awasthi**

GitHub:
https://github.com/architawasthi99

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐.
