import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.markdown("# Consumer Behavior and Shopping Habits Dataset:")
st.write("E-Commerce Transaction Trends: A Comprehensive Dataset:")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('shopping_behavior_updated.csv')
    return df

df = load_data()

# Sidebar - Dashboard options
st.sidebar.title('Dashboard Options')
dashboard_selectbox = st.sidebar.selectbox(
    'Select Dashboard View:',
    ('Key Metrics', 'Product Preferences', 'Sales Trend', 'Customer Analysis')
)

# Main cont
st.title('Retail Consumer Behavior Analysis')

# Dashboard view
if dashboard_selectbox == 'Key Metrics':
    st.header('Key Metrics')
    total_sales = df['Purchase Amount (USD)'].sum()
    avg_purchase_amount = df['Purchase Amount (USD)'].mean()
    st.subheader('Total Sales: ${:.2f}'.format(total_sales))
    st.subheader('Average Purchase Amount: ${:.2f}'.format(avg_purchase_amount))

# Interactive 3D scatter plot for customer demographics
    fig = go.Figure(data=[go.Scatter3d(
        
        x=df['Age'],
        y=df['Gender'],
        z=df['Purchase Amount (USD)'],
        mode='markers',
        marker=dict(
            size=10,
            color=df['Purchase Amount (USD)'],
            colorscale='Viridis',
            opacity=0.8
        )
    )])

    fig.update_layout(scene=dict(
        xaxis_title='Age',
        yaxis_title='Gender',
        zaxis_title='Purchase Amount (USD)'
    ))

    st.plotly_chart(fig)

# Product preferences view
elif dashboard_selectbox == 'Product Preferences':
    st.header('Product Preferences')

    # Bar chart for distribution of purchases by product category
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']

    # Custom color palette
    colors = px.colors.qualitative.Vivid

    fig = px.bar(category_counts, x='Count', y='Category', orientation='h',
                labels={'x': 'Count', 'y': 'Category'}, title='Purchases by Product Category',
                color='Category', color_discrete_sequence=colors)
    fig.update_yaxes(categoryorder='total ascending')  # Sort categories by total count
    st.plotly_chart(fig)


# Sales trend view
elif dashboard_selectbox == 'Sales Trend':
    st.header('Sales Trend')

    # Generate sample sales data
    months = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
    sales_data = np.random.randint(1000, 5000, size=len(months))
    sales_over_time = pd.DataFrame({'Date': months, 'Total Sales': sales_data})

    # Extract month and year for creating a new variable
    sales_over_time['Month'] = sales_over_time['Date'].dt.month

    # Create 3D line plot
    fig = go.Figure(data=[go.Scatter3d(x=np.zeros_like(sales_over_time['Total Sales']), 
                        y=sales_over_time['Total Sales'], 
                        z=sales_over_time['Month'], 
                        mode='lines',
                line=dict(color='purple', width=5))])

    fig.update_layout(scene=dict(xaxis_title='Constant Value',
                                yaxis_title='Total Sales',
                                zaxis_title='Month'))
    
    st.plotly_chart(fig)


# Customer analysis view
elif dashboard_selectbox == 'Customer Analysis':
    st.header('Customer Analysis')

    # Generate a synthetic dataset for demonstration purposes
    # Replace this with your actual dataset
    df = pd.DataFrame({
        'Age': np.random.randint(18, 65, size=1000),
        'Purchase Amount (USD)': np.random.normal(50, 20, size=1000),  # Example purchase amount data
        'Gender': np.random.choice(['Male', 'Female'], size=1000)
    })

    # Create a color map for gender
    color_map = {'Male': 'green', 'Female': 'yellow'}

    # Create a shape map for gender
    shape_map = {'Male': 'square', 'Female': 'circle'}

    # Create 3D scatter plot
    fig = px.scatter_3d(df, x='Age', y='Purchase Amount (USD)', z=np.zeros(len(df)),
                        color='Gender', color_discrete_map=color_map,
                        symbol='Gender', symbol_map=shape_map,
                        opacity=0.7, title='Age vs. Purchase Amount',
                        labels={'Age': 'Age', 'Purchase Amount (USD)': 'Purchase Amount (USD)'})

    # Update layout
    fig.update_layout(scene=dict(
        xaxis_title='Age',
        yaxis_title='Purchase Amount (USD)',
        zaxis_title=''),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    st.plotly_chart(fig)