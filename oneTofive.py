import plotly.graph_objects as go
import pandas as pd

# Load data from CSV
df = pd.read_csv('battery_data.csv')

# Voltage Visualization (Line Plot)
voltage_fig = go.Figure()
voltage_fig.add_trace(go.Scatter(
    y=df['Voltage'],
    mode='lines+markers',
    name='Voltage',
    line=dict(color='blue'),
    marker=dict(size=8)
))
voltage_fig.update_layout(
    title="Battery Cell Voltages",
    xaxis_title="Cell Index",
    yaxis_title="Voltage (V)"
)

# SOC Visualization (Line Plot)
soc_fig = go.Figure()
soc_fig.add_trace(go.Scatter(
    y=df['SOC'],
    mode='lines+markers',
    name='SOC',
    line=dict(color='green'),
    marker=dict(size=8)
))
soc_fig.update_layout(
    title="State of Charge",
    xaxis_title="Time",
    yaxis_title="SOC (%)"
)

# Temperature Visualization (Line Plot)
temp_fig = go.Figure()
temp_fig.add_trace(go.Scatter(
    y=df['Temperature'],
    mode='lines',
    name='Temperature',
    line=dict(color='red')
))
temp_fig.update_layout(
    title="Battery Temperature",
    xaxis_title="Time",
    yaxis_title="Temperature (°C)"
)

# Cell Voltage Range (Shaded Plot)
range_fig = go.Figure()
range_fig.add_trace(go.Scatter(
    x=list(range(1, len(df) + 1)),
    y=df['CellMinimumVoltage'],
    mode='lines',
    fill='tonexty',
    name='Min Voltage',
    line=dict(color='orange')
))
range_fig.add_trace(go.Scatter(
    x=list(range(1, len(df) + 1)),
    y=df['CellMaximumVoltage'],
    mode='lines',
    fill='tonexty',
    name='Max Voltage',
    line=dict(color='green')
))
range_fig.update_layout(
    title="Voltage Range of Cells",
    xaxis_title="Time",
    yaxis_title="Voltage (V)"
)

# ERRORStatus Visualization (Bar Chart)
error_fig = go.Figure()
error_fig.add_trace(go.Bar(
    y=df['ERRORStatus'],
    name='Error Status',
    marker_color='purple'
))
error_fig.update_layout(
    title="Error Status",
    xaxis_title="Time",
    yaxis_title="Error Code"
)

# Show all figures
voltage_fig.show()
soc_fig.show()
temp_fig.show()
range_fig.show()
error_fig.show()
