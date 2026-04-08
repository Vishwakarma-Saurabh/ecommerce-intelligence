const API_URL = 'http://localhost:8000';

function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(`${tabName}-tab`).classList.add('active');
    
    // Update active button
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
}

async function checkFraud() {
    const featuresText = document.getElementById('fraud-features').value;
    const features = featuresText.split(',').map(Number);
    
    if (features.length !== 10) {
        alert('Please enter exactly 10 numbers');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/predict/fraud`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features: features })
        });
        
        const result = await response.json();
        
        const resultDiv = document.getElementById('fraud-result');
        const fraudStatus = result.is_fraud ? '⚠️ FRAUD DETECTED' : '✅ SAFE TRANSACTION';
        const statusClass = result.is_fraud ? 'fraud' : 'safe';
        
        resultDiv.innerHTML = `
            <div class="result-card ${statusClass}">
                <h3>${fraudStatus}</h3>
                <p>Fraud Probability: ${(result.probability * 100).toFixed(1)}%</p>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: ${result.probability * 100}%"></div>
                </div>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        alert('Error connecting to API. Make sure backend is running.');
    }
}

async function predictSales() {
    const featuresText = document.getElementById('sales-features').value;
    const features = featuresText.split(',').map(Number);
    
    if (features.length !== 8) {
        alert('Please enter exactly 8 numbers');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/predict/sales`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features: features })
        });
        
        const result = await response.json();
        
        document.getElementById('sales-result').innerHTML = `
            <div class="result-card success">
                <h3>📊 Sales Prediction</h3>
                <p class="large-number">$${result.predicted_sales.toFixed(2)}</p>
                <p>Expected sales based on your marketing inputs</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        alert('Error connecting to API');
    }
}

async function segmentCustomer() {
    const featuresText = document.getElementById('segment-features').value;
    const features = featuresText.split(',').map(Number);
    
    if (features.length !== 6) {
        alert('Please enter exactly 6 numbers');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/segment/customer`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features: features })
        });
        
        const result = await response.json();
        
        const segmentIcons = {
            'High Value': '💎',
            'At Risk': '⚠️',
            'Bargain Hunter': '💰',
            'New Customer': '🌟'
        };
        
        document.getElementById('segment-result').innerHTML = `
            <div class="result-card success">
                <h3>${segmentIcons[result.segment_name]} Customer Segment: ${result.segment_name}</h3>
                <p>Segment ID: ${result.segment}</p>
                <p>Recommended: ${getRecommendation(result.segment_name)}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        alert('Error connecting to API');
    }
}

function getRecommendation(segment) {
    const recommendations = {
        'High Value': 'Send VIP offers and loyalty rewards',
        'At Risk': 'Send retention campaign with discount',
        'Bargain Hunter': 'Send flash sale notifications',
        'New Customer': 'Send welcome email with first purchase discount'
    };
    return recommendations[segment] || 'Standard marketing campaign';
}