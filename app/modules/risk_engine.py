def calculate_risk(anomaly_score, blacklist_flag, frequency):

    risk = 0

    if anomaly_score == -1:
        risk += 50

    if blacklist_flag == "Blacklisted":
        risk += 40

    if frequency > 100:
        risk += 10

    if risk >= 70:
        return "High"
    elif risk >= 40:
        return "Medium"
    else:
        return "Low"