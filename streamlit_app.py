import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Data Insights Dashboard",
    layout="wide"
)

st.title("📊 Automated Data Insights Dashboard")
st.write("Upload your dataset and get instant automated analysis 🚀")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"],
    key="main_csv_upload"
)

# -----------------------------
# PROCESS FILE
# -----------------------------
if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # -----------------------------
    # DATA PREVIEW
    # -----------------------------
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # -----------------------------
    # BASIC INFO
    # -----------------------------
    st.subheader("📌 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # -----------------------------
    # DATA TYPES
    # -----------------------------
    st.subheader("🧠 Data Types")
    st.dataframe(df.dtypes.astype(str))

    # -----------------------------
    # MISSING VALUES
    # -----------------------------
    st.subheader("❌ Missing Values")
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) > 0:
        st.dataframe(missing)
    else:
        st.success("No missing values found!")

    # -----------------------------
    # STATISTICAL SUMMARY
    # -----------------------------
    st.subheader("📈 Statistical Summary")

    numeric_df = df.select_dtypes(include=['number'])

    if not numeric_df.empty:
        st.dataframe(numeric_df.describe())
    else:
        st.warning("No numeric columns found.")

    # -----------------------------
    # CORRELATION MATRIX
    # -----------------------------
    st.subheader("🔗 Correlation Matrix")

    if numeric_df.shape[1] > 1:

        correlation = numeric_df.corr()

        st.dataframe(correlation)

        # Heatmap
        fig, ax = plt.subplots(figsize=(10, 6))

        cax = ax.matshow(correlation)

        plt.xticks(range(len(correlation.columns)),
                   correlation.columns,
                   rotation=90)

        plt.yticks(range(len(correlation.columns)),
                   correlation.columns)

        fig.colorbar(cax)

        st.pyplot(fig)

    else:
        st.warning("Not enough numeric columns for correlation.")

    # -----------------------------
    # COLUMN-WISE ANALYSIS
    # -----------------------------
    st.subheader("📊 Column Analysis")

    selected_column = st.selectbox(
        "Select Column",
        df.columns
    )

    st.write(df[selected_column].value_counts().head(10))

    # -----------------------------
    # VISUALIZATION
    # -----------------------------
    st.subheader("📉 Visualization")

    if selected_column in numeric_df.columns:

        fig2, ax2 = plt.subplots()

        ax2.hist(df[selected_column].dropna(), bins=20)

        ax2.set_title(f"Distribution of {selected_column}")

        st.pyplot(fig2)

    else:

        value_counts = df[selected_column].value_counts().head(10)

        st.bar_chart(value_counts)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("⚙️ About Project")

st.sidebar.info("""
### Features

✅ CSV Upload  
✅ Automated Data Analysis  
✅ Missing Value Detection  
✅ Statistical Summary  
✅ Correlation Analysis  
✅ Interactive Charts  

### Built Using

- Streamlit 🎯
- Pandas 🐼
- Matplotlib 📊
""")