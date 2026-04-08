import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def train_all_models():
    
    # 1. Train Fraud Detector
    print("Training fraud detector...")
    fraud_data = pd.read_csv('fraud_data.csv')
    X_fraud = fraud_data.drop('is_fraud', axis=1)
    y_fraud = fraud_data['is_fraud']
    
    scaler_fraud = StandardScaler()
    X_fraud_scaled = scaler_fraud.fit_transform(X_fraud)
    
    fraud_model = RandomForestClassifier(n_estimators=100, random_state=42)
    fraud_model.fit(X_fraud_scaled, y_fraud)
    
    joblib.dump(fraud_model, 'models/fraud_model.pkl')
    joblib.dump(scaler_fraud, 'models/fraud_scaler.pkl')
    print("✅ Fraud model saved")
    
    # 2. Train Sales Predictor
    print("Training sales predictor...")
    sales_data = pd.read_csv('sales_data.csv')
    X_sales = sales_data.drop('sales', axis=1)
    y_sales = sales_data['sales']
    
    scaler_sales = StandardScaler()
    X_sales_scaled = scaler_sales.fit_transform(X_sales)
    
    sales_model = RandomForestRegressor(n_estimators=100, random_state=42)
    sales_model.fit(X_sales_scaled, y_sales)
    
    joblib.dump(sales_model, 'models/sales_model.pkl')
    joblib.dump(scaler_sales, 'models/sales_scaler.pkl')
    print("✅ Sales model saved")
    
    # 3. Train Customer Segmenter
    print("Training customer segmenter...")
    cust_data = pd.read_csv('customer_data.csv')
    
    scaler_cust = StandardScaler()
    X_cust_scaled = scaler_cust.fit_transform(cust_data)
    
    segment_model = KMeans(n_clusters=4, random_state=42, n_init=10)
    segment_model.fit(X_cust_scaled)
    
    joblib.dump(segment_model, 'models/segment_model.pkl')
    joblib.dump(scaler_cust, 'models/segment_scaler.pkl')
    print("✅ Segmentation model saved")
    
    print("\n🎉 All models trained successfully!")

if __name__ == "__main__":
    import os
    os.makedirs('models', exist_ok=True)
    train_all_models()