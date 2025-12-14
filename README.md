<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Real Estate Investment Advisor</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; }
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
This project builds an end-to-end <b>Machine Learning system</b> that helps real estate investors
decide whether a property is a <b>Good Investment</b> and estimates its <b>price after 5 years</b>.
</p>

<hr>

<h2>🎯 Problem Statement</h2>
<div class="box">
<ul>
  <li>Classify whether a property is a <b>Good Investment</b></li>
  <li>Predict the <b>Future Property Price (5 years)</b></li>
  <li>Provide a user-friendly <b>Streamlit web app</b></li>
  <li>Track experiments using <b>MLflow</b></li>
</ul>
</div>

<hr>

<h2>🧠 Project Phases</h2>

<h3>Phase 1 — Data Understanding & EDA</h3>
<ul>
  <li>Dataset inspection (shape, types, missing values)</li>
  <li>Price & size distribution analysis</li>
  <li>Location-based trends (city, locality, state)</li>
  <li>Impact of amenities, transport, schools, hospitals</li>
  <li>Correlation analysis</li>
</ul>

<h3>Phase 2 — Feature Engineering</h3>
<ul>
  <li>Recomputed <code>Price_per_SqFt</code></li>
  <li>Density scores (School, Hospital)</li>
  <li>Transport score mapping</li>
  <li>Infrastructure & efficiency features</li>
  <li>Rule-based <b>Investment Score</b></li>
</ul>

<h3>Phase 3 — Target Creation</h3>
<ul>
  <li><b>Classification:</b> Good_Investment (rule-based)</li>
  <li><b>Regression:</b> Future_Price_5Y using compound growth</li>
</ul>

<h3>Phase 4 — Modeling</h3>
<ul>
  <li>Logistic Regression</li>
  <li>Random Forest</li>
  <li>XGBoost (best performing)</li>
  <li>Stratified Cross-Validation</li>
</ul>

<h3>Phase 5 — Experiment Tracking</h3>
<ul>
  <li>Metrics logging with MLflow</li>
  <li>Model comparison & selection</li>
  <li>Artifact storage</li>
</ul>

<h3>Phase 6 — Deployment</h3>
<ul>
  <li>Streamlit web application</li>
  <li>Real-time prediction & confidence scores</li>
</ul>

<hr>

<h2>🛠 Tech Stack</h2>
<ul>
  <li>Python, Pandas, NumPy</li>
  <li>Scikit-learn, XGBoost</li>
  <li>MLflow</li>
  <li>Streamlit</li>
</ul>

<hr>

<h2>📦 Large Artifacts</h2>
<p>
Trained models and MLflow logs are hosted externally due to GitHub size limits.
</p>
<ul>
  <li><a href="models.md">Models Download Guide</a></li>
  <li><a href="mlruns.md">MLflow Artifacts Guide</a></li>
</ul>

<hr>

<h2>▶️ How to Run</h2>
<pre>
pip install -r requirements.txt
streamlit run app_streamlit.py
</pre>
<hr>

<h2>☁️ AWS Deployment Architecture (Planned / Partial)</h2>

<p>
The project was designed with cloud deployment in mind.  
While the final submission uses local deployment, the architecture is fully compatible with AWS.
</p>

<h3>🔧 Intended AWS Stack</h3>
<ul>
  <li><b>AWS EC2</b> — Hosting the Streamlit application</li>
  <li><b>AWS S3</b> — Storing trained model artifacts</li>
  <li><b>AWS IAM</b> — Secure access control</li>
  <li><b>AWS CloudWatch</b> — Monitoring logs & performance</li>
</ul>

<h3>📐 Deployment Architecture</h3>
<pre>
User (Browser)
     |
     v
Streamlit App (EC2)
     |
     +-- Load ML Models (S3 / Local)
     |
     +-- Prediction Engine
</pre>

<h3>⚠️ Current Status</h3>
<ul>
  <li>AWS deployment was tested locally and partially configured</li>
  <li>Final submission uses local deployment due to time & cost constraints</li>
  <li>Docker & Elastic Beanstalk files were intentionally removed to keep the repository clean</li>
</ul>

<h3>💡 Why AWS Was Not Fully Used</h3>
<ul>
  <li>AWS free-tier limitations for long-running ML apps</li>
  <li>Large model size (~112MB)</li>
  <li>Streamlit Cloud / local deployment is more suitable for academic evaluation</li>
</ul>

<h3>🚀 Cloud-Ready Design</h3>
<p>
Despite local execution, the application is production-ready and can be deployed on AWS
with minimal configuration changes.
</p>


</body>
</html>
