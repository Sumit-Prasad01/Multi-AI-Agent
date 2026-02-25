# 🤖 Multi AI Agent Platform

A **Multi-LLM AI Agent System** that allows users to dynamically:

-   Select which LLM to use
-   Define the role/persona of the LLM
-   Ask contextual questions based on the defined role
-   Deploy seamlessly using Docker & AWS Cloud Infrastructure

------------------------------------------------------------------------

## 🚀 Project Overview

This project is a production-ready Multi AI Agent platform built with:

-   **Python**
-   **FastAPI** (Backend API)
-   **Streamlit** (Frontend UI)
-   **Groq API** (LLM inference)
-   **Docker** (Containerization)
-   **Jenkins** (CI/CD Pipeline)
-   **SonarQube** (Code Quality & Static Analysis)
-   **AWS ECR** (Container Registry)
-   **AWS Fargate** (Serverless Container Deployment)

The system enables users to create customizable AI agents by selecting
the LLM and defining its behavior dynamically.

------------------------------------------------------------------------

## 🧠 Core Features

### 🔹 Multi‑LLM Support

Users can select from multiple LLM providers (e.g., Groq-supported
models).

### 🔹 Custom Role Definition

Users define the system prompt such as: - "You are a senior data
scientist" - "You are a DevOps engineer" - "You are a medical assistant"

### 🔹 Context-Aware Q&A

After role definition, users can ask questions, and responses are
generated based on the chosen LLM and defined role.

### 🔹 Production-Ready Backend

FastAPI handles: - Agent configuration - Prompt construction - LLM API
calls - Response streaming

### 🔹 Interactive Frontend

Streamlit UI enables: - LLM selection dropdown - Role definition input -
Real-time chat interface

### 🔹 CI/CD Pipeline

Jenkins automates: - Docker image build - SonarQube analysis - Push to
AWS ECR - Deployment to AWS Fargate

------------------------------------------------------------------------

## 🏗️ Architecture

    User → Streamlit UI → FastAPI Backend → Groq LLM API
                           ↓
                      Docker Container
                           ↓
                      Jenkins CI/CD
                           ↓
                     AWS ECR → AWS Fargate

------------------------------------------------------------------------

## 📂 Project Structure

    app/
    │── backend/          # FastAPI backend logic
    │── frontend/         # Streamlit UI
    │── core/             # Agent orchestration logic
    │── config/           # Settings & environment configs
    │── common/           # Logging & exception handling
    │── main.py           # Application entrypoint

    custom_jenkins/
    │── Dockerfile        # Jenkins build container

    Dockerfile            # Application container
    Jenkinsfile           # CI/CD pipeline definition
    requirements.txt      # Python dependencies
    setup.py              # Package setup
    .env                  # Environment variables

------------------------------------------------------------------------

## ⚙️ Environment Variables

Create a `.env` file:

    GROQ_API_KEY=your_groq_api_key
    AWS_ACCOUNT_ID=your_aws_account_id
    AWS_REGION=your_region
    ECR_REPOSITORY=your_repo_name

------------------------------------------------------------------------

## 🐳 Running Locally (Docker)

### 1️⃣ Build Image

    docker build -t multi-ai-agent .

### 2️⃣ Run Container

    docker run -p 8000:8000 multi-ai-agent

------------------------------------------------------------------------

## 🔁 CI/CD Pipeline Flow

1.  Developer pushes code to GitHub
2.  Jenkins triggers pipeline
3.  SonarQube performs static code analysis
4.  Docker image is built
5.  Image pushed to AWS ECR
6.  AWS Fargate pulls image & deploys container

------------------------------------------------------------------------

## ☁️ Deployment (AWS)

-   **Container Registry:** AWS ECR\
-   **Container Runtime:** AWS Fargate\
-   **Orchestration:** ECS Task Definition\
-   **Scaling:** Auto-scaling via ECS service

------------------------------------------------------------------------

## 🔐 Security Practices

-   Environment variables for secrets
-   Dockerized isolated runtime
-   CI/CD quality gates via SonarQube
-   IAM roles for AWS resource access

------------------------------------------------------------------------

## 📈 Future Improvements

-   Add support for OpenAI & HuggingFace models
-   Conversation memory storage (Redis / DB)
-   Role-based agent templates
-   Agent chaining & tool usage
-   Monitoring with Prometheus & Grafana

------------------------------------------------------------------------


