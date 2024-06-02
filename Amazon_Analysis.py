import streamlit as st
import pandas as pd
st.title("Amazon Analysis Sale")
st.header('Delivered to Buyer -Analysis')

data=pd.read_csv('Shipped - Delivered to Buyer.csv')
# st.dataframe(data)

col1,col2,col3=st.columns(3)

with col1:
    total_revenue=int(data['Total Amount'].sum())
    st.metric(label='Total Revenue', value=total_revenue)

with col2:
    total_order=len(data['Order ID'].unique())
    st.metric(label='Total orders',value=total_order)


with col3:
    total_qty=data['Qty'].sum()
    st.metric(label='Quantity Sales',value=total_qty)


col4,col5,col6=st.columns(3)

with col4:
    total_city=len(data['ship-city'].unique())-1
    st.metric(label='City',value=total_city)


with col5:
    total_state=len(data['ship-state'].unique())-1
    st.metric(label='State',value=total_state)    
# st.header('Choose Delivery Status')

# st.selectbox()
