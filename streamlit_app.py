# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create a title for the app
st.title("Simple Line Chart Visualization")

# Create a sidebar with a slider to control the number of points
st.sidebar.header("Settings")
n_points = st.sidebar.slider("Number of points", 10, 100, 20)

# Generate random data
x = np.arange(n_points)
y = np.random.rand(n_points)

# Create a line chart
fig, ax = plt.subplots()
ax.plot(x, y)

# Add title and labels
ax.set_title("Random Line Chart")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the chart in the Streamlit app
st.pyplot(fig)
