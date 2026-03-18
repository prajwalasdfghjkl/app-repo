from flask import Flask
import os

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
ENV = os.environ.get("ENV", "staging")

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>GitOps Demo</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #0f172a; color: #e2e8f0; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: #1e293b; border-radius: 16px; padding: 40px 60px; text-align: center; box-shadow: 0 0 40px rgba(99,102,241,0.3); }}
            h1 {{ color: #818cf8; font-size: 2.5rem; margin-bottom: 8px; }}
            .badge {{ display: inline-block; padding: 6px 18px; border-radius: 999px; font-size: 0.9rem; margin: 6px; }}
            .env {{ background: #065f46; color: #6ee7b7; }}
            .version {{ background: #1e1b4b; color: #a5b4fc; }}
            p {{ color: #94a3b8; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>GitOps Pipeline</h1>
            <p>Deployed via ArgoCD on EKS</p>
            <span class="badge env">ENV: {ENV}</span>
            <span class="badge version">VERSION: {APP_VERSION}</span>
            <p>Automated · Self-Healing · Git-Driven</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {{"status": "healthy", "version": APP_VERSION, "env": ENV}}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
