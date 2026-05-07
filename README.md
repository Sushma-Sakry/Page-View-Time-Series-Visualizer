# Page View Time Series Visualizer

This project is part of the Data Analysis with Python certification from freeCodeCamp.

The project focuses on analyzing and visualizing time series data using Python libraries such as Pandas, Matplotlib, and Seaborn. The dataset contains the daily page views of the freeCodeCamp forum from May 2016 to December 2019.

## Project Objectives

The main objectives of this project are:

- Import and clean time series data
- Analyze page view trends over time
- Visualize daily forum traffic
- Compare monthly and yearly growth patterns
- Identify seasonal trends and data distribution

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Google Colab

## Dataset Information

The dataset contains:
- Date
- Daily page views

The data represents the number of visits to the freeCodeCamp forum between 2016 and 2019.

## Data Cleaning

The dataset was cleaned by removing:
- the top 2.5% of page view values
- the bottom 2.5% of page view values

This helps remove extreme outliers that can distort visualizations.

## Visualizations Created

### 1. Line Plot

The line chart shows the daily freeCodeCamp forum page views over time.

Purpose:
- visualize overall growth trends
- identify spikes and traffic patterns

File:
- `line_plot.png`

### 2. Bar Plot

The bar chart displays the average daily page views for each month grouped by year.

Purpose:
- compare monthly growth across years
- analyze yearly traffic progression

File:
- `bar_plot.png`

### 3. Box Plots

Two box plots were created:
- Year-wise Box Plot (Trend)
- Month-wise Box Plot (Seasonality)

Purpose:
- analyze distribution of page views
- identify trends and seasonal behavior
- observe outliers and variability

File:
- `box_plot.png`

## Files Included

- `time_series_visualizer.py` → Main project code
- `fcc-forum-pageviews.csv` → Dataset used for analysis
- `line_plot.png` → Line chart visualization
- `bar_plot.png` → Bar chart visualization
- `box_plot.png` → Box plot visualizations
