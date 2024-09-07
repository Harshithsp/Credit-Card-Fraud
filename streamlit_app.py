import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Streamlit app title
st.title("Credit Card Fraud Detection")

# Upload the dataset
uploaded_file = st.file_uploader("Choose a credit card transactions file", type=["xlsx", "xls"])

# Define the feature engineering steps
def preprocess_data(df):
    # Remove non-numeric columns or rows with non-numeric values
    df = df.apply(pd.to_numeric, errors='coerce')
    
    # Fill or drop NaN values (you can also handle them differently if you prefer)
    df = df.dropna()

    # Feature scaling
    scaler = StandardScaler()
    df[['scaled_Amount', 'scaled_Time']] = scaler.fit_transform(df[['Amount', 'Time']])

    # Perform PCA for dimensionality reduction
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(df[['scaled_Amount', 'scaled_Time'] + [f'V{i}' for i in range(1, 29)]])
    df['PCA1'] = pca_result[:, 0]
    df['PCA2'] = pca_result[:, 1]

    return df

# Fraud detection function
def detect_fraud(df, model):
    features = ['scaled_Amount', 'scaled_Time'] + [f'V{i}' for i in range(1, 29)]
    df['anomaly'] = model.predict(df[features])
    df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)
    return df[df['anomaly'] == 1]

# Display fraud results if file is uploaded
if uploaded_file is not None:
    try:
        # Read the Excel file using pandas
        new_transactions = pd.read_excel(uploaded_file)
        
        # Preprocess the data
        new_transactions = preprocess_data(new_transactions)
        
        # Show preview of the dataset
        st.write("Dataset preview:")
        st.dataframe(new_transactions.head())
        
        # Train the Isolation Forest on the normal transactions
        features = ['scaled_Amount', 'scaled_Time'] + [f'V{i}' for i in range(1, 29)]
        normal_transactions = new_transactions[new_transactions['Class'] == 0]
        iso_forest = IsolationForest(contamination=0.0017, random_state=42)
        iso_forest.fit(normal_transactions[features])

        # Detect fraud
        frauds = detect_fraud(new_transactions, iso_forest)
        
        # Show detected fraudulent transactions
        st.write("Detected fraudulent transactions:")
        st.dataframe(frauds)
    except Exception as e:
        st.error(f"Error loading the file: {e}")
else:
    st.info("Please upload a valid Excel file (.xlsx or .xls).")

