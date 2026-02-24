import streamlit as st
import plotly.express as px

def render_dashboard(df, results):

    st.header("📊 Security Dashboard")

    # Add Isolation Forest Results
    if "isolation_forest" in results:
        df["Anomaly"] = results["isolation_forest"]

    if "kmeans" in results:
        df["Cluster"] = results["kmeans"]

    # Show basic stats
    st.subheader("Traffic Overview")
    st.write(df.describe())

    # Anomaly Distribution
    if "Anomaly" in df.columns:
        fig = px.histogram(df, x="Anomaly", title="Anomaly Distribution")
        st.plotly_chart(fig, use_container_width=True)

    # Cluster Distribution
    if "Cluster" in df.columns:
        fig2 = px.histogram(df, x="Cluster", title="Cluster Distribution")
        st.plotly_chart(fig2, use_container_width=True)

    # Show Evaluation Metrics
    if "evaluation_metrics" in results:
        st.subheader("📈 Model Evaluation Metrics")
        st.write(results["evaluation_metrics"])