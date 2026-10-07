from fastapi import FastAPI
import os

app = FastAPI(title="SaaS Infrastructure Health API")

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "Chargebee SaaS Monitoring API",
        "region": os.getenv("AWS_REGION", "us-east-1"),
        "deployment_type": "AWS Native App Runner (No Container Setup)"
    }

@app.get("/metrics")
def get_metrics():
    return {
        "latency_ms": 12,
        "uptime": "99.99%",
        "active_nodes": 3
    }