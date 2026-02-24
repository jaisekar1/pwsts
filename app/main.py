import streamlit as st
import pandas as pd
import os

from modules.data_loader import load_pcap
from modules.feature_engineering import generate_features
from modules.anomaly_models import (
    run_all_models,
    show_feature_importance
)
from modules.threat_intel import threat_lookup
from modules.visualization import render_dashboard
from modules.live_sniffer import start_sniffing


# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(layout="wide")
st.title("🛡 AI-Powered Network Traffic Intelligence Platform")

# Detect if running on Streamlit Cloud
is_cloud = os.getenv("STREAMLIT_SHARING_MODE") is not None


# -----------------------------------
# LIVE MONITORING
# -----------------------------------
st.header("🔴 Live Network Monitoring")

if st.button("Start Live Monitoring"):

    if is_cloud:
        st.warning("⚠ Live packet sniffing is not supported on Streamlit Cloud.")
        st.info("Please run the app locally to enable live network monitoring.")
    else:
        st.info("Capturing 100 packets...")

        try:
            live_df = start_sniffing(100)

            if not live_df.empty:
                st.success("Live Capture Completed")
                st.dataframe(live_df)
            else:
                st.warning("No packets captured.")
        except Exception as e:
            st.error(f"Live monitoring failed: {e}")

st.divider()


# -----------------------------------
# PCAP FILE UPLOAD
# -----------------------------------
st.header("📂 PCAP File Analysis")

uploaded = st.file_uploader("Upload PCAP File", type=["pcap"])

if uploaded:

    # Load raw packet data
    df = load_pcap(uploaded)

    st.subheader("Raw Packet Data")
    st.dataframe(df.head())

    # Feature Engineering
    features = generate_features(df)

    st.subheader("Engineered Features")
    st.dataframe(features.head())

    # Run All Models
    results = run_all_models(features)

    # Add Results to DataFrame (safe check)
    if "isolation_forest" in results:
        df["Anomaly_Label"] = results["isolation_forest"]

    if "kmeans" in results:
        df["Cluster_Label"] = results["kmeans"]

    # Threat Intelligence Lookup
    if "Source" in df.columns:
        df["Threat_Flag"] = df["Source"].apply(threat_lookup)

    # Dashboard Visualization
    render_dashboard(df, results)

    # -----------------------------------
    # Explainable AI Section
    # -----------------------------------
    st.header("📊 Explainable AI")

    if "random_forest_model" in results:
        if st.button("Show Feature Importance"):
            show_feature_importance(
                results["random_forest_model"],
                features
            )
