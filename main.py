import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file into a DataFrame
df = pd.read_csv('movies.csv')

# 1. Histogram of IMDb Ratings
fig1 = px.histogram(df, x='imdb_rating', nbins=20, title='Distribution of IMDb Ratings')
fig1.update_traces(marker_color='skyblue')
fig1.update_layout(xaxis_title='IMDb Rating', yaxis_title='Number of Movies')

# 2. Bar Chart for Movie Certificates
certificate_counts = df['certificate'].value_counts().reset_index()
certificate_counts.columns = ['Certificate', 'Number of Movies']
fig2 = px.bar(certificate_counts, x='Certificate', y='Number of Movies', title='Number of Movies by Certificate')
fig2.update_traces(marker_color='lightcoral')
fig2.update_xaxes(categoryorder='total ascending')

# 3. Scatter Plot of IMDb Ratings vs. IMDb Votes
fig3 = px.scatter(df, x='imbd_votes', y='imdb_rating', title='IMDb Rating vs. IMDb Votes')
fig3.update_traces(marker=dict(size=5, opacity=0.5, color='green'))
fig3.update_xaxes(title='IMDb Votes')
fig3.update_yaxes(title='IMDb Rating')

# 4. Box Plot of IMDb Ratings by Certificate
fig4 = px.box(df, x='certificate', y='imdb_rating', title='IMDb Ratings by Certificate')
fig4.update_traces(marker_color='darkorange')

# 5. Pie Chart of Movie Certificate Distribution
certificate_distribution = df['certificate'].value_counts()
fig5 = px.pie(certificate_distribution, names=certificate_distribution.index, values=certificate_distribution.values, title='Movie Certificate Distribution')

# 6. Line Chart of Movie Release Year Trends
release_year_counts = df['year'].value_counts().reset_index()
release_year_counts.columns = ['Year', 'Number of Movies']
fig6 = px.line(release_year_counts, x='Year', y='Number of Movies', title='Movie Release Year Trends')
fig6.update_traces(marker_color='purple')

# 7. Heatmap
# Select the columns for the heatmap
columns_for_heatmap = ['imdb_rating', 'imbd_votes', 'year']

# Calculate the correlation matrix for the selected columns
correlation_matrix = df[columns_for_heatmap].corr()

# Create a heatmap
fig7 = px.imshow(correlation_matrix, x=columns_for_heatmap, y=columns_for_heatmap)

# Streamlit App
st.title("Movie Data Visualization")

# Display the Histogram of IMDb Ratings
st.plotly_chart(fig1)

# Display the Bar Chart for Movie Certificates
st.plotly_chart(fig2)

# Display the Scatter Plot of IMDb Ratings vs. IMDb Votes
st.plotly_chart(fig3)

# Display the Box Plot of IMDb Ratings by Certificate
st.plotly_chart(fig4)

# Display the Pie Chart of Movie Certificate Distribution
st.plotly_chart(fig5)

# Display the Line Chart of Movie Release Year Trends
st.plotly_chart(fig6)

# Display the Heatmap
st.plotly_chart(fig7)
