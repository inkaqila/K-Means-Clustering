from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/proses", methods=["POST"])
def proses():
    file = request.files["file"]
    if not file:
        return redirect("/")
    
    df = pd.read_csv(file)
    
    # Contoh preprocessing & clustering
    X = df.select_dtypes(include=['int64', 'float64'])

    kmeans = KMeans(n_clusters=3, random_state=0)
    df['cluster'] = kmeans.fit_predict(X)

    # Save hasil ke csv
    df.to_csv("hasil_clustering.csv", index=False)

    # Simpan gambar-gambar
    # (cluster.png, elbow.png, silhouette.png) — 

    table_html = df.to_html(classes="data", index=False)
    return render_template("index.html", table=table_html)

@app.route("/download")
def download():
    return send_file("hasil_clustering.csv", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

    