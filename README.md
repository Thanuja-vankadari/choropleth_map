This repository contains a Python script that generates an interactive Choropleth map visualizing global installs by app category. The chart is restricted to display only between 6 PM IST and 8 PM IST.

Files Included

choropleth_map.py - The Python script to generate the Choropleth map.

choropleth_map.html - The output HTML file with the interactive map.

app_data.csv - Sample dataset (not included, provide your own dataset with the required columns).

Installation and Usage

Prerequisites

Ensure you have Python installed along with the following libraries:

pip install pandas plotly pytz

Running the Script

Place your dataset (app_data.csv) in the same directory as choropleth_map.py.

Run the script using:

python choropleth_map.py

If the current time is between 6 PM IST and 8 PM IST, the Choropleth map will be displayed and saved as choropleth_map.html.

If the script is run outside this time window, it will display a message indicating the map is not available.

Dataset Requirements

The dataset should be a CSV file with the following columns:

Category (string) - App category (filtered to exclude categories starting with 'A', 'C', 'G', or 'S').

Installs (numeric) - Number of installs (categories exceeding 1 million installs are highlighted).

Country (string) - Country where the installs occurred.
