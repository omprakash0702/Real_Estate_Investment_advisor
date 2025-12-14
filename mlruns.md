<!DOCTYPE html>
<html>

<body>

<h1>📊 MLflow Experiment Tracking</h1>

<div class="info">
MLflow is used to track experiments, metrics, and model artifacts during training.
</div>

<h2>📥 Download MLflow Logs</h2>
<p>
<a href="https://drive.google.com/drive/folders/1qXvQ_VPyH3lFK9Yc00CFCO7P-77IWuT5?usp=drive_link">🔗 Google Drive Link</a>
</p>

<h2>📂 Folder Structure</h2>
<pre>
mlruns/
└── experiments/
    ├── metrics/
    ├── params/
    └── artifacts/
</pre>

<h2>📈 What is Tracked?</h2>
<ul>
  <li>Accuracy, Precision, Recall, ROC-AUC</li>
  <li>RMSE, MAE, R²</li>
  <li>Confusion matrices</li>
  <li>Feature importance plots</li>
</ul>

<h2>▶️ How to View</h2>
<pre>
mlflow ui
</pre>
<p>Then open <code>http://localhost:5000</code></p>

<h2>🎯 Why MLflow?</h2>
<ul>
  <li>Experiment reproducibility</li>
  <li>Model comparison</li>
  <li>Production-ready ML workflow</li>
</ul>

</body>
</html>
