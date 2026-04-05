import streamlit as st
import requests
import pandas as pd

# -----------------------------
# CONFIG
# -----------------------------
API_BASE_URL = "http://127.0.0.1:8000"  # change when deployed

st.set_page_config(page_title="Data Insights Dashboard", layout="wide")

st.title("📊 Automated Data Insights Dashboard")
st.write("Upload your dataset and get instant analysis powered by FastAPI 🚀")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    # Preview dataset
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    # UPLOAD TO FASTAPI
    # -----------------------------
    if st.button("🚀 Run Analysis"):
        with st.spinner("Processing..."):

            files = {"file": uploaded_file.getvalue()}

            try:
                response = requests.post(f"{API_BASE_URL}/upload", files=files)

                if response.status_code == 200:
                    st.success("Data uploaded successfully!")

                    # -----------------------------
                    # GET ANALYSIS
                    # -----------------------------
                    analysis_res = requests.get(f"{API_BASE_URL}/analysis")

                    if analysis_res.status_code == 200:
                        data = analysis_res.json()

                        st.subheader("📈 Statistical Summary")
                        st.json(data.get("summary", {}))

                        st.subheader("🔗 Correlation Matrix")
                        st.json(data.get("correlation", {}))

                    else:
                        st.error("Error fetching analysis")

                    # -----------------------------
                    # VISUALIZATION
                    # -----------------------------
                    viz_res = requests.get(f"{API_BASE_URL}/visualization")

                    if viz_res.status_code == 200:
                        st.subheader("📊 Visualizations")
                        st.image(viz_res.content)

                    else:
                        st.warning("Visualization not available")

                else:
                    st.error("Upload failed")

            except Exception as e:
                st.error(f"Error: {str(e)}")

# -----------------------------
# SIDEBAR (EXTRA POLISH)
# -----------------------------
st.sidebar.title("⚙️ About Project")

st.sidebar.info("""
**Data Insights API**

🔹 Upload dataset  
🔹 Automated cleaning  
🔹 Statistical insights  
🔹 Correlation analysis  
🔹 Visual outputs  

Built using:
- FastAPI ⚡
- Pandas 🐼
- Streamlit 🎯
""")
