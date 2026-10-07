# SaaS Infrastructure Health Check API

A lightweight, cloud-native REST microservice built with **FastAPI** and deployed using **Continuous Deployment (CD)** via **Render Cloud Infrastructure**.

---

## Live Demo & API Endpoints

- **Live Service URL:** `https://saas-cloud-healthcheck.onrender.com`
- **Root Health Check:** [`GET /`](https://saas-cloud-healthcheck.onrender.com)
- **Infrastructure Metrics:** [`GET /metrics`](https://saas-cloud-healthcheck.onrender.com/metrics)
- **Interactive Swagger Docs:** [`GET /docs`](https://saas-cloud-healthcheck.onrender.com/docs)

---

## Tech Stack & Cloud Architecture

- **Backend Framework:** FastAPI (Python 3)
- **Application Server:** Uvicorn
- **Cloud Hosting:** Render Cloud Platform
- **Deployment Pipeline:** Automated Continuous Deployment (CD) on `git push` to `main`
- **API Documentation:** OpenAPI / Swagger UI

---

## API Response Samples

### 1. `GET /` — System Status
```json
{
  "status": "healthy",
  "service": "Chargebee SaaS Monitoring API",
  "deployment_platform": "Render Cloud Infrastructure",
  "auto_deploy": true
}
