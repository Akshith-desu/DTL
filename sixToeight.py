import plotly.graph_objects as go
import pandas as pd

# Load data from CSV
df_additional = pd.read_csv('distance_data.csv')

# Distance Travelled Visualization (Line Plot)
distance_fig = go.Figure()
distance_fig.add_trace(go.Scatter(
    x=df_additional['Runtime'],
    y=df_additional['DistanceTravelled'],
    mode='lines+markers',
    name='Distance Travelled',
    line=dict(color='blue'),
    marker=dict(size=8)
))
distance_fig.update_layout(
    title="Distance Travelled Over Time",
    xaxis_title="Runtime",
    yaxis_title="Distance Travelled (km)"
)

# Range Left Visualization (Line Plot)
range_left_fig = go.Figure()
range_left_fig.add_trace(go.Scatter(
    x=df_additional['Runtime'],
    y=df_additional['RangeLeft'],
    mode='lines+markers',
    name='Range Left',
    line=dict(color='green'),
    marker=dict(size=8)
))
range_left_fig.update_layout(
    title="Range Left Over Time",
    xaxis_title="Runtime",
    yaxis_title="Range Left (km)"
)

# Combined Visualization (Distance Travelled and Range Left)
combined_fig = go.Figure()
combined_fig.add_trace(go.Scatter(
    x=df_additional['Runtime'],
    y=df_additional['DistanceTravelled'],
    mode='lines+markers',
    name='Distance Travelled',
    line=dict(color='blue'),
    marker=dict(size=8),
    yaxis='y1'
))
combined_fig.add_trace(go.Scatter(
    x=df_additional['Runtime'],
    y=df_additional['RangeLeft'],
    mode='lines+markers',
    name='Range Left',
    line=dict(color='green'),
    marker=dict(size=8),
    yaxis='y2'
))
combined_fig.update_layout(
    title="Distance Travelled and Range Left Over Time",
    xaxis_title="Runtime",
    yaxis_title="Distance Travelled (km)",
    yaxis2=dict(
        title="Range Left (km)",
        overlaying="y",
        side="right"
    )
)

# Show all figures
distance_fig.show()
range_left_fig.show()
combined_fig.show()
