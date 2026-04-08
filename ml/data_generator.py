import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_regression, make_blobs

def generate_all_data():
    
    # Fraud data
    X_fraud, y_fraud = make_classification(n_samples=5000, n_features=10, weights=[0.95], random_state=42)
    fraud_df = pd.DataFrame(X_fraud, columns=[f'feature_{i}' for i in range(10)])
    fraud_df['is_fraud'] = y_fraud
    fraud_df.to_csv('fraud_data.csv', index=False)
    
    # Sales data
    X_sales, y_sales = make_regression(n_samples=5000, n_features=8, random_state=42)
    sales_df = pd.DataFrame(X_sales, columns=[f'feature_{i}' for i in range(8)])
    sales_df['sales'] = np.abs(y_sales * 1000)
    sales_df.to_csv('sales_data.csv', index=False)
    
    # Customer data
    X_cust, _ = make_blobs(n_samples=2000, n_features=6, centers=4, random_state=42)
    cust_df = pd.DataFrame(X_cust, columns=[f'feature_{i}' for i in range(6)])
    cust_df.to_csv('customer_data.csv', index=False)
    
    print("✅ Data generated: fraud_data.csv, sales_data.csv, customer_data.csv")

if __name__ == "__main__":
    generate_all_data()