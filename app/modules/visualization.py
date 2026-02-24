import streamlit as st
import plotly.express as px


def render_dashboard(df, results):

    st.header("📊 Security Dashboard")

    # Add Isolation Forest Results
    if "isolation_forest" in results:
        df["Anomaly"] = results["isolation_forest"]

    if "kmeans" in results:
        df["Cluster"] = results["kmeans"]

    # -----------------------------------
    # Traffic Overview
    # -----------------------------------
    st.subheader("Traffic Overview")
    st.dataframe(df.describe(), width="stretch")

    # -----------------------------------
    # Anomaly Distribution
    # -----------------------------------
    if "Anomaly" in df.columns:
        fig = px.histogram(
            df,
            x="Anomaly",
            title="Anomaly Distribution"
        )
        st.plotly_chart(fig, width="stretch")

    # -----------------------------------
    # Cluster Distribution
    # -----------------------------------
    if "Cluster" in df.columns:
        fig2 = px.histogram(
            df,
            x="Cluster",
            title="Cluster Distribution"
        )
        st.plotly_chart(fig2, width="stretch")

    # -----------------------------------
    # Model Evaluation Metrics
    # -----------------------------------
    if "evaluation_metrics" in results:
        st.subheader("📈 Model Evaluation Metrics")
        st.write(results["evaluation_metrics"])
