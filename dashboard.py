import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
#  TITLE AND DESCRIPTION
# -----------------------------
st.set_page_config(page_title="📊 Data Dashboard", layout="wide")
st.title("📊 Interactive Data Dashboard (Mini Tableau)")
st.write("Upload a CSV file to explore your data interactively.")

# -----------------------------
#  FILE UPLOAD SECTION
# -----------------------------
uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # -----------------------------
    #  DATA PREVIEW
    # -----------------------------
    st.subheader("📋 Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    #  METRICS SECTION
    # -----------------------------
    st.subheader("📈 Key Metrics")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if numeric_cols:
        avg_val = df[numeric_cols[0]].mean()
        max_val = df[numeric_cols[0]].max()
        min_val = df[numeric_cols[0]].min()
        col1, col2, col3 = st.columns(3)
        col1.metric("Average", round(avg_val, 2))
        col2.metric("Maximum", round(max_val, 2))
        col3.metric("Minimum", round(min_val, 2))

    # -----------------------------
    #  VISUALIZATION SECTION
    # -----------------------------
    st.subheader("📊 Visualization")
    all_cols = df.columns.tolist()
    x_col = st.selectbox("Select X-axis:", all_cols)
    y_col = st.selectbox("Select Y-axis (numeric):", numeric_cols)
    chart_type = st.radio("Choose chart type:", ["Bar", "Line", "Scatter", "Pie"])

    if chart_type == "Bar":
        fig = px.bar(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
    elif chart_type == "Line":
        fig = px.line(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
    elif chart_type == "Pie":
        fig = px.pie(df, names=x_col, values=y_col, title=f"{chart_type} Chart")

    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    #  HEATMAP (BONUS)
    # -----------------------------
    st.subheader("🔥 Correlation Heatmap")
    corr = df.corr(numeric_only=True)
    heatmap = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale="Viridis")
    st.plotly_chart(heatmap, use_container_width=True)

    # -----------------------------
    #  FOOTER
    # -----------------------------
    st.markdown("---")
    st.caption("Developed by [Your Name] • Data Analytics Project")
