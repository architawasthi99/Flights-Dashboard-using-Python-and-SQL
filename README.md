# ✈️ Flight Analytics Dashboard

An interactive **Flight Analytics Dashboard** built using **Python, MySQL, and Streamlit**.

The application allows users to explore flight data, search flights based on source and destination, view important flight statistics through KPI cards, and analyze the dataset using interactive visualizations.

The project demonstrates practical implementation of **Python, SQL, MySQL database connectivity, CRUD operations, Streamlit, environment variables, data analysis, and Git/GitHub**.

---

## 📌 Project Overview

The Flight Analytics Dashboard converts raw flight data stored in a MySQL database into an interactive web-based dashboard.

Instead of manually writing SQL queries in MySQL Workbench, users can interact with the data through a Streamlit interface.

The application is organized into two major sections:

```text
Flight Analytics Dashboard
│
├── Check Flights
│   ├── Select Source
│   ├── Select Destination
│   └── View Flight Information
│
└── Analytics
    ├── KPI Cards
    ├── Airline Analysis
    ├── Airport Analysis
    ├── Price Analysis
    └── Route Analysis
✨ Features
✈️ Flight Search

Users can select a source and destination from dropdown menus.

Example:

Source        → Bangalore
Destination   → New Delhi

The selected route can then be used to retrieve and display relevant flight information.

📊 Analytics Dashboard

The Analytics section is designed to provide insights from the flight dataset.

Analytics include:

Total number of flights
Number of airlines
Number of airports
Average flight price
Airline-wise flight distribution
Busiest airports
Flight price analysis
Route analysis
Flight duration analysis
Number of stops analysis
📌 KPI Cards

KPI stands for Key Performance Indicator.

KPI cards display important summary information at the top of the dashboard.

Example:

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Total Flights  │ │   Airlines     │ │   Airports     │ │  Average Price │
│                │ │                │ │                │ │                │
│    10,683      │ │      12        │ │      40        │ │    ₹9,087      │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘
KPI Metrics
Total Flights
Total Airlines
Total Airports
Average Flight Price

The values are calculated dynamically from the MySQL database.

🏢 Airline Analysis

The dashboard can analyze the distribution of flights across different airlines.

Example:

Airlines
│
├── Jet Airways
├── IndiGo
├── Air India
├── SpiceJet
├── Vistara
└── GoAir

Possible analysis:

Number of flights by airline
Airline market distribution
Average price by airline
Average duration by airline
🛫 Airport Analysis

The project can analyze airports based on flight activity.

Possible metrics include:

Number of departures
Number of arrivals
Total airport activity
Busiest airports
Most frequently used airports
💰 Price Analysis

Flight prices can be analyzed based on different factors.

Possible analysis:

Average flight price
Minimum price
Maximum price
Price by airline
Price by route
Price based on number of stops
Price by travel date
🛣️ Route Analysis

Users can analyze different flight routes.

Example:

Bangalore → New Delhi
Mumbai → Delhi
Chennai → Kolkata
Delhi → Mumbai

Possible route-level metrics:

Number of flights
Average price
Cheapest price
Average duration
Number of non-stop flights
Number of one-stop flights
⏱️ Flight Duration Analysis

The dataset contains flight duration information.

The dashboard can analyze:

Average duration
Minimum duration
Maximum duration
Duration by airline
Duration by route
Duration based on number of stops
🛑 Stops Analysis

Flight routes can be analyzed based on the number of stops.

Examples:

Non-stop
1 Stop
2 Stops
3 Stops
4 Stops

This can be used to analyze relationships such as:

Stops ↔ Price
Stops ↔ Duration
Stops ↔ Airline
🗄️ Database

The project uses MySQL as the relational database.

The main table currently used by the dashboard is:

flights_cleaned
Current Dataset Columns
Airline
Date_of_Journey
Source
Destination
Route
Dep_Time
Duration
Total_Stops
Price
🏗️ Database Architecture
                MySQL
                  │
                  ▼
          ┌─────────────────┐
          │ flights_cleaned │
          └─────────────────┘
                  │
                  │ SQL Queries
                  ▼
          ┌─────────────────┐
          │   database.py   │
          └─────────────────┘
                  │
                  ▼
          ┌─────────────────┐
          │     app.py      │
          └─────────────────┘
                  │
                  ▼
             Streamlit
                  │
                  ▼
              Dashboard
🔄 Application Flow
                    User
                     │
                     ▼
             Streamlit Dashboard
                     │
                     ▼
                  app.py
                     │
                     ▼
                database.py
                     │
                     ▼
                  MySQL
                     │
                     ▼
             flights_cleaned
                     │
                     ▼
                SQL Results
                     │
                     ▼
             Streamlit Dashboard
How it works
The user opens the Streamlit application.
app.py creates a DB object.
database.py establishes the MySQL connection.
Streamlit requests data through database methods.
SQL queries are executed.
MySQL returns the required data.
Streamlit displays the results.
🛠️ Tech Stack
Technology	Purpose
Python	Application logic and data processing
Streamlit	Interactive web dashboard
MySQL	Relational database
mysql-connector-python	Python-MySQL connectivity
python-dotenv	Environment variable management
Pandas	Data analysis and processing
SQL	Database querying and analytics
Git	Version control
GitHub	Source code hosting
🐍 Python

Python is used for:

Application logic
Database connectivity
SQL execution
Data processing
Streamlit development
CRUD operations
🌐 Streamlit

Streamlit is used to build the interactive dashboard.

It provides:

Sidebar navigation
Selectboxes
KPI cards
Tables
Charts
Interactive filters
User interaction
🗄️ MySQL

MySQL is used to:

Store flight data
Query flight information
Perform CRUD operations
Calculate analytics
Filter and aggregate data
🔌 mysql-connector-python

Used to connect Python with MySQL.

import mysql.connector
🔐 python-dotenv

Used to load database credentials from the .env file.

from dotenv import load_dotenv

This keeps sensitive database credentials outside the source code.

📊 Pandas

Pandas can be used for:

Data cleaning
Data transformation
Data analysis
Data processing
📂 Project Structure
Flight-dashboard/
│
├── venv/
│
├── screenshots/
│
├── .env
├── .gitignore
├── README.md
│
├── app.py
├── database.py
│
├── create.py
├── read.py
├── update.py
├── delete.py
│
└── setup_database.py
