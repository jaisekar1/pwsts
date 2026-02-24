
def generate_features(df):
    df["Length_Squared"] = df["Length"] ** 2
    df["Protocol_Flag"] = df["Protocol"] % 2
    df["Traffic_Score"] = df["Length"] * df["Protocol"]
    return df[["Length", "Protocol", "Length_Squared", "Protocol_Flag", "Traffic_Score"]]
