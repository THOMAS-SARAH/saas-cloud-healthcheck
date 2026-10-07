from fastapi import FastAPI
import os

app = FastAPI(title="SaaS Infrastructure Health API")

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "Chargebee SaaS Monitoring API",
        "deployment_platform": "Render Cloud Infrastructure",
        "auto_deploy": True
    }

@app.get("/metrics")
def get_metrics():
    return {
        "latency_ms": 12,
        "uptime": "99.99%",
        "active_nodes": 3
    }