Streamlit Web Application for Weather Data

Overview
This Streamlit Web Application provides an interactive interface for visualizing global weather data. It integrates with a Flask REST API to serve cleaned weather data and displays real-time weather updates streamed via Apache Kafka. The application consists of two main sections a data dashboard and live data updates.

Features
1. Data Dashboard
   - Displays the cleaned global weather dataset.
   - Includes filters to refine data by date, region, and other relevant metrics.
   - Visualizes key weather metrics for better insights.

2. Live Data Updates
   - Shows real-time weather updates streamed from Kafka.
   - Features dynamic plots that visualize temperature, humidity, and other parameters as they are updated.

Prerequisites
Before running the Streamlit Web Application, ensure you have the following set up
- Python 3.7 or higher
- Flask installed and running with the REST API serving the cleaned weather data
- Apache Kafka set up to stream live weather data

Installation
1. Clone the Repository
   git clone https://github.com/MohitGill10/WeatherAppProject.git
   cd WeatherAppProject

2. Set Up a Virtual Environment (recommended)
   python -m venv venv

3. Activate the Virtual Environment
   On Windows
   venvScriptsactivate
   On macOSLinux
   source venvbinactivate

4. Install Required Packages
   pip install streamlit requests

Running the Application
1. Start the Flask API
   Open a terminal and navigate to the project directory, then run
   python app.py

2. Run the Streamlit App
   In a new terminal, run
   streamlit run streamlit_app.py
   This will start the Streamlit server, and you can access the application in your web browser at httplocalhost8501.

How to Use the Application
Data Dashboard
- Use the filters to view the weather data according to specific dates or regions.
- Visualizations will update dynamically based on the applied filters.

Live Data Updates
- View real-time weather updates as data is streamed from Kafka.
- The plots will refresh automatically, providing users with the latest weather information.
