<!DOCTYPE html>
<html>
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
<ul>
  <li>Classify whether a property is a <b>Good Investment</b></li>
  <li>Predict the <b>future property price (5-year horizon)</b></li>
  <li>Provide insights through a <b>Streamlit-based web application</b></li>
  <li>Track and compare experiments using <b>MLflow</b></li>
</ul>

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

<h3>Phase 6 — Deployment (AWS + Streamlit)</h3>
<ul>
  <li>Interactive Streamlit web application</li>
  <li>Real-time predictions with confidence scores</li>
  <li><b>Successfully deployed on AWS Elastic Beanstalk</b></li>
</ul>

<p>
<b>🌐 Live Application:</b><br>
<a href="http://realestate-streamlit-app-env.eba-piisbf34.eu-north-1.elasticbeanstalk.com/" target="_blank">
http://realestate-streamlit-app-env.eba-piisbf34.eu-north-1.elasticbeanstalk.com/
</a>
</p>

<hr>

<h2>☁️ AWS Deployment Summary (Executed)</h2>

<h3>🔧 AWS Services Used</h3>
<ul>
  <li><b>AWS Elastic Beanstalk</b> — Application orchestration & hosting</li>
  <li><b>EC2 (managed by EB)</b> — Streamlit runtime</li>
  <li><b>IAM</b> — Secure role-based access</li>
</ul>

<h3>🪜 Deployment Steps (Brief)</h3>
<ul>
  <li>Prepared Streamlit app with trained ML pipelines</li>
  <li>Created Elastic Beanstalk Python environment</li>
  <li>Configured application entry point & port mapping</li>
  <li>Uploaded application bundle via Elastic Beanstalk</li>
  <li>Verified health checks and public accessibility</li>
</ul>

<h3>📐 Deployment Architecture</h3>
<pre>
User (Browser)
     |
     v
AWS Elastic Beanstalk
     |
     v
Streamlit App (EC2 Instance)
     |
     v
ML Inference Pipelines
</pre>

<h3>⚠️ Notes</h3>
<ul>
  <li>Large model artifacts (~112 MB) are excluded from GitHub</li>
  <li>Models and MLflow runs are shared via external links</li>
  <li>Docker files were removed after successful EB deployment</li>
</ul>

<hr>

<h2>🛠 Technology Stack</h2>
<ul>
  <li>Python, Pandas, NumPy</li>
  <li>Scikit-learn, XGBoost</li>
  <li>MLflow</li>
  <li>Streamlit</li>
  <li>AWS Elastic Beanstalk</li>
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

<h2>▶️ Run Locally</h2>
<pre>
pip install -r requirements.txt
streamlit run app_streamlit.py
</pre>

</body>
</html>
