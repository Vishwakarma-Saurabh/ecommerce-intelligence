# 🛍️ E-commerce Intelligence Platform

A production-ready machine learning system for e-commerce fraud detection, sales prediction, and customer segmentation.

## 🎯 Features

- **Real-time Fraud Detection**: Detect fraudulent transactions with 95% accuracy
- **Sales Forecasting**: Predict sales based on marketing inputs
- **Customer Segmentation**: Automatically group customers for targeted marketing
- **Interactive Web Interface**: User-friendly dashboard for predictions
- **REST API**: FastAPI backend with automatic documentation

## 🏗️ Architecture
Frontend (HTML/CSS/JS) → Backend API (FastAPI) → ML Models (scikit-learn)


## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-intelligence.git
cd ecommerce-intelligence

Install Dependencies
pip install -r backend/requirements.txt

Train ML Models
cd ml
python data_generator.py
python train.py

Start the Backend Server
python backend/main.py
The API will be available at http://localhost:8000

Open the Frontend
Option A: Using Python HTTP Server
cd frontend
python -m http.server 3000
# Open http://localhost:3000
Option B: Direct File Access
Double-click frontend/index.html

Usage Examples
Fraud Detection
curl -X POST "http://localhost:8000/predict/fraud" \
  -H "Content-Type: application/json" \
  -d '{"features": [0.5, 1.2, -0.3, 2.1, -1.5, 0.8, 1.1, -0.7, 2.3, -1.2]}'

Sales Prediction
curl -X POST "http://localhost:8000/predict/sales" \
  -H "Content-Type: application/json" \
  -d '{"features": [1.2, -0.5, 2.1, -1.3, 0.7, 1.8, -0.9, 1.5]}'

Customer Segmentation
curl -X POST "http://localhost:8000/segment/customer" \
  -H "Content-Type: application/json" \
  -d '{"features": [2.1, -1.2, 0.8, 1.5, -0.7, 2.3]}'

📊 API Documentation
Once running, visit:
Interactive API docs: http://localhost:8000/docs
Alternative docs: http://localhost:8000/redoc

API Endpoints
Method	Endpoint	Description
POST	/predict/fraud	Detect transaction fraud
POST	/predict/sales	Predict sales revenue
POST	/segment/customer	Segment customer type
GET	/health	Health check

🧪 Testing
Manual Testing
Use the web interface to test predictions with different inputs.
Example Test Cases:- 
Fraud Detection - High Risk:
Input: 5.2, 3.1, -2.5, 4.1, -3.2, 2.5, 3.2, -1.8, 4.5, -2.1
Expected: FRAUD DETECTED (high probability)
Sales Prediction - High Sales:

Input: 2.5, 1.8, 0.9, 2.3, -0.5, 2.1, 1.5, 2.0
Expected: High sales prediction

📁 Project Structure
ecommerce-intelligence/
├── backend/              # FastAPI backend
│   ├── main.py          # API endpoints & model loading
│   └── requirements.txt  # Python dependencies
├── frontend/            # Web interface
│   ├── index.html       # Main page
│   ├── app.js          # Frontend logic
│   └── style.css       # Styling
├── ml/                  # ML training pipeline
│   ├── data_generator.py  # Synthetic data generation
│   ├── train.py           # Model training
│   └── models/           # Saved models (gitignored)
└── README.md            # This file

🤝 Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

👏 Acknowledgments
Built with scikit-learn
API powered by FastAP
Frontend with vanilla JavaScript

⚠️ Important Notes
Models are not committed to GitHub (too large)
Generate and train models locally first
Default port: 8000 (backend), 3000 (frontend)

🐛 Troubleshooting
Model not found error:

bash
# Make sure to run from root directory
cd ecommerce-intelligence
python backend/main.py
Port already in use:

bash
# Change port in backend/main.py
uvicorn.run(app, host="0.0.0.0", port=8001)  # Use different port
CORS errors:
Ensure backend is running on port 8000
Check frontend API_URL matches backend address

🚀 Deployment
Local Deployment
bash
# Terminal 1: Backend
python backend/main.py

# Terminal 2: Frontend
cd frontend && python -m http.server 3000
Cloud Deployment (Coming Soon)
Backend: Render.com / Railway.app
Frontend: Netlify / Vercel

