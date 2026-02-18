# Voyage Analytics: Integrating MLOps in Travel Productionization of ML Systems

A full-stack travel planning application integrating ML models for flight price prediction, gender classification, and hotel recommendations. Built with Flask APIs, Docker containerization, Kubernetes orchestration, MLflow via DagsHub for experiment tracking, and a Streamlit frontend.

## 🚀 About / Business Context

 In the realm of travel and tourism, the intersection of data analytics and machine learning presents an opportunity to revolutionize the way travel experiences are curated and delivered. This capstone project revolves around a trio of datasets, users, flights, and hotels, each providing a unique perspective on travel patterns and preferences. The goal is to leverage these datasets to build and deploy sophisticated machine learning models serving a dual purpose, enhancing predictive capabilities in travel-related decision making and mastering the art of MLOps through hands-on application.

## 🏗️ Tech Stack & Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| Backend APIs | Flask | REST endpoints for ML inference |
| ML Models | Scikit-learn / Custom | Flight price prediction, gender classification, hotel recommendation |
| Experiment Tracking | MLflow + DagsHub | Model versioning, metrics, artifacts |
| Containerization | Docker | Portable deployments |
| Orchestration | Kubernetes | Scaling, pod management, port-forwarding |
| Frontend | Streamlit | Interactive travel planning UI |

## 📦 Quick Start

### Prerequisites
- Docker & Docker Compose
- Kubernetes (Minikube or cluster access)
- kubectl
- MLflow/DagsHub credentials

### 1. Clone & Environment
```bash
git clone <your-repo>
cd voyage-capstone
cp .env.example .env
# Update .env with DagsHub/MLflow tokens
```
### 2. MlFlow Tracking
    mlflow server --backend-store-uri <dagsHub-remote> --default-artifact-root <artifacts>

### 3. Flask API
```bash
flask run
```
You can use/test the apis through testing/api_testing.ipynb

### 4. Docker Build
    docker build -t <your_tag> .
    docker run -p 5000:5000 <your_tag>

Or use MY Uploaded image
    docker pull dkhan123/travel_apis:latest
    docker run -p 5000:5000 dkhan123/travel_apis:latest

### 5. Kubernetes Deploy
    # Apply manifests
    kubectl apply -f kubernetes/
    # Port-forward Flask API 
    kubectl port-forward deployment/travel-apis-deployment 5000:5000
    
### 6. Using Streamlit app
```bash
cd streamlit
streamlit run app.py
```
## 🌐 Access
* Flask API: http://localhost:5000

* Streamlit UI: http://localhost:8501

* MLflow UI: http://localhost:5001 or your DagsHub URI

## 🛠️ Development Workflow
1. Model Training: Use MLflow to log experiments → Push to DagsHub

2. API Development: Flask endpoints call models via MLflow models serve

3. Containerize: Dockerfile for API + models

4. Deploy: Kubernetes manifests with deployments/services

5. Frontend: Streamlit consumes API endpoints

## 📁 Project Structure
    voyage-capstone/
    ├── notebooks/        # EDA + Training scripts + MLflow runs
    ├── app.py            # Flask app (travel-apis-deployment)
    ├── streamlit/        # Frontend app
    ├── Dockerfile        # Dockerfile
    ├── kubernetes/       # Deployments, services
    ├── models/           # ML models from MlFlow
    ├──testing/           # for testing apis
    ├──data/              # datasets  
    ├──requirements.txt   # dependencies
    └── README.md



