from fastapi import FastAPI, UploadFile, File
from sklearn.ensemble import IsolationForest
from services.risk_services import calculate_provider_risk
import pandas as pd

app = FastAPI(
    title="AI-Powered Provider Billing Integrity Platform",
    version="1.0.0"
)

claims_df = None


@app.get("/")
def home():
    return {
        "message": "Provider Billing Integrity Platform Running"
    }


@app.post("/upload-claims")
async def upload_claims(file: UploadFile = File(...)):

    global claims_df

    df = pd.read_csv(file.file)

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(
        df[["billed_amount"]]
    )

    claims_df = df

    anomalies = df[df["anomaly"] == -1]

    return {
        "filename": file.filename,
        "total_claims": len(df),
        "anomalies_found": len(anomalies),
        "anomalous_claims": anomalies[
            ["claim_id", "provider_id", "billed_amount"]
        ].to_dict(orient="records")
    }


@app.get("/provider-risk")
def provider_risk():

    global claims_df

    if claims_df is None:
        return {
            "message": "Upload claims first"
        }

    return calculate_provider_risk(claims_df)