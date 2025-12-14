<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Real Estate Investment Advisor</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.65; }
    h1, h2, h3 { color: #2c3e50; }
    ul { margin-left: 20px; }
    code { background: #f4f4f4; padding: 2px 6px; border-radius: 4px; }
    .box { background: #f9f9f9; padding: 15px; border-left: 5px solid #3498db; }
  </style>
</head>

<body>

<h1>🏡 Real Estate Investment Advisor</h1>
<h3>Predicting Property Profitability & Future Value</h3>

<p>
This project presents an end-to-end <b>Machine Learning–based decision support system</b>
designed to help real estate investors evaluate whether a property is a 
<b>Good Investment</b> and to estimate its <b>price after 5 years</b>.
</p>

<hr>

<h2>🎯 Problem Statement</h2>
<div class="box">
<ul>
  <li>Classify whether a property is a <b>Good Investment</b></li>
  <li>Predict the <b>future property price (5-year horizon)</b></li>
  <li>Provide insights through a <b>Streamlit-based web application</b></li>
  <li>Track and compare experiments using <b>MLflow</b></li>
</ul>
</div>

<hr>

<h2>🧠 Project Phases</h2>

<h3>Phase 1 — Data Understanding & Exploratory Data Analysis (EDA)</h3>
<ul>
  <li>Dataset inspection (shape, data types, missing values)</li>
  <li>Price and size distribution analysis</li>
  <li>Location-based analysis (state, city, locality)</li>
  <li>Impact analysis of amenities, transport, schools, and hospitals</li>
  <li>Correlation analysis among numerical features</li>
</ul>

<h3>Phase 2 — Feature Engineering</h3>
<ul>
  <li>Recalculated <code>Price_per_SqFt</code> for consistency</li>
  <li>School and hospital density scores</li>
  <li>Public transport accessibility scoring</li>
  <li>Infrastructure and efficiency-related features</li>
  <li>Rule-based <b>Investment Score</b> formulation</li>
</ul>

<h3>Phase 3 — Target Variable Creation</h3>
<ul>
  <li><b>Classification:</b> <code>Good_Investment</code> (rule-based label)</li>
  <li><b>Regression:</b> <code>Future_Price_5Y</code> using compound growth logic</li>
</ul>

<h3>Phase 4 — Model Development</h3>
<ul>
  <li>Logistic Regression (baseline, interpretable)</li>
  <li>Random Forest (non-linear ensemble)</li>
  <li>XGBoost (best-performing model)</li>
  <li>Stratified cross-validation for robust evaluation</li>
</ul>

<h3>Phase 5 — Experiment Tracking & Model Selection</h3>
<ul>
  <li>Metric logging using MLflow</li>
  <li>Model performance comparison</li>
  <li>Artifact and experiment management</li>
</ul>

<h3>Phase 6 — Application Deployment</h3>
<ul>
  <li>Interactive Streamlit web application</li>
  <li>Real-time predictions with confidence scores</li>
</ul>

<hr>

<h2>🛠 Technology Stack</h2>
<ul>
  <li>Python, Pandas, NumPy</li>
  <li>Scikit-learn, XGBoost</li>
  <li>MLflow</li>
  <li>Streamlit</li>
</ul>

<hr>

<h2>📦 Large Artifacts</h2>
<p>
Due to GitHub file size limitations, trained models and MLflow artifacts are hosted externally.
</p>
<ul>
  <li><a href="models.md">📦 Models Download Guide</a></li>
  <li><a href="mlruns.md">📊 MLflow Artifacts Guide</a></li>
</ul>

<hr>

<h2>▶️ How to Run the Application</h2>
<pre>
pip install -r requirements.txt
streamlit run app_streamlit.py
</pre>

<hr>

<h2>☁️ AWS Deployment Architecture (Planned / Partial)</h2>

<p>
The system was designed with cloud deployment in mind.  
While the final submission uses local deployment, the architecture is fully compatible with AWS services.
</p>

<h3>🔧 Intended AWS Stack</h3>
<ul>
  <li><b>AWS EC2</b> — Hosting the Streamlit application</li>
  <li><b>AWS S3</b> — Storage for trained model artifacts</li>
  <li><b>AWS IAM</b> — Secure access and permission management</li>
  <li><b>AWS CloudWatch</b> — Application and system monitoring</li>
</ul>

<h3>📐 High-Level Deployment Architecture</h3>
<pre>
User (Browser)
     |
     v
Streamlit App (EC2)
     |
     +-- Load Trained Models (S3 / Local)
     |
     +-- Prediction Engine
</pre>

<h3>⚠️ Current Deployment Status</h3>
<ul>
  <li>AWS deployment was explored and partially configured</li>
  <li>Final submission uses local execution to avoid AWS cost and free-tier limitations</li>
  <li>Docker and Elastic Beanstalk files were intentionally removed to keep the repository clean</li>
</ul>

<h3>💡 Rationale for Local Deployment</h3>
<ul>
  <li>AWS free-tier constraints for long-running applications</li>
  <li>Large trained model size (~112 MB)</li>
  <li>Local/Streamlit deployment is more suitable for academic evaluation</li>
</ul>

<h3>🚀 Cloud-Ready Design</h3>
<p>
Despite being executed locally, the project follows production-grade practices and can be
deployed on AWS with minimal configuration changes.
</p>

</body>
</html>
