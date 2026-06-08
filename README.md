# AI-Powered Provider Billing Integrity Platform

## Overview

A healthcare revenue cycle analytics platform that identifies anomalous provider billing patterns and calculates provider risk scores using machine learning.

## Features

- Claims upload via CSV
- Billing anomaly detection
- Provider risk scoring
- FastAPI REST APIs
- Swagger API documentation

## Tech Stack

- Python
- FastAPI
- Pandas
- Scikit-Learn
- Isolation Forest

## API Endpoints

### POST /upload-claims

Upload claims data and detect anomalies.

### GET /provider-risk

Calculate provider risk scores based on anomalous billing behavior.

## Future Enhancements

- Revenue leakage detection
- Duplicate claim detection
- CPT code validation
- Claim denial prediction