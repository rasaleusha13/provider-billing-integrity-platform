def calculate_provider_risk(df):

    provider_summary = []

    for provider_id, group in df.groupby("provider_id"):

        total_claims = len(group)

        anomalous_claims = len(
            group[group["anomaly"] == -1]
        )

        risk_score = (
            anomalous_claims / total_claims
        ) * 100

        if risk_score >= 50:
            risk_level = "HIGH"
        elif risk_score >= 20:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        provider_summary.append({
            "provider_id": provider_id,
            "total_claims": total_claims,
            "anomalous_claims": anomalous_claims,
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level
        })

    return provider_summary