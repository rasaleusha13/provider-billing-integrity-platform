from fastapi import FastAPI, UploadFile, File
import pandas as pd
from sklearn.ensemble import IsolationForest

app = FastAPI(
    title="AI-Powered Provider Billing Integrity Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Provider Billing Integrity Platform Running"
    }

@app.post("/upload-claims")
async def upload_claims(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    df["anomaly"] = model.fit_predict(
        df[["billed_amount"]]
    )

    anomalies = df[df["anomaly"] == -1]

    return {
        "filename": file.filename,
        "total_claims": len(df),
        "anomalies_found": len(anomalies),
        "anomalous_claims": anomalies[
            ["claim_id", "provider_id", "billed_amount"]
        ].to_dict(orient="records")
    }