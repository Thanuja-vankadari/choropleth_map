import pandas as pd
import plotly.express as px
from datetime import datetime
import pytz

# Load dataset (update with the correct file path)
df = pd.read_csv("app_data.csv")

# Filter categories that do not start with 'A', 'C', 'G', or 'S'
df = df[~df['Category'].str.startswith(('A', 'C', 'G', 'S'))]

# Identify top 5 categories by total installs
top_categories = df.groupby('Category')['Installs'].sum().nlargest(5).index

df_filtered = df[df['Category'].isin(top_categories)]

# Aggregate installs by country and category
df_grouped = df_filtered.groupby(['Country', 'Category']).agg({'Installs': 'sum'}).reset_index()

# Check current time in IST
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist).time()
allowed_start = datetime.strptime("18:00", "%H:%M").time()
allowed_end = datetime.strptime("20:00", "%H:%M").time()

if allowed_start <= current_time <= allowed_end:
    # Create Choropleth map
    fig = px.choropleth(
        df_grouped, 
        locations='Country', 
        locationmode='country names', 
        color='Installs',
        hover_name='Category',
        title='Global Installs by Category (Top 5)',
        color_continuous_scale='Viridis'
    )
    
    # Highlight categories where installs exceed 1 million
    df_grouped['Highlight'] = df_grouped['Installs'].apply(lambda x: 'High' if x > 1_000_000 else 'Low')
    fig.update_traces(marker=dict(line=dict(width=1, color='black')))
    
    # Show the figure
    fig.show()
    
    # Save plot as HTML
    fig.write_html("choropleth_map.html")
else:
    print("Graph is only available between 6 PM IST and 8 PM IST.")
