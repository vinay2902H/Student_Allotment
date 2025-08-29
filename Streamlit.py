import streamlit as st
import pandas as pd

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="College Allotment Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------
# Load Data
# -------------------------
file_path = r"C:\Users\vinay\Documents\DS\College_seats\allotment_results.csv"
df = pd.read_csv(file_path)

# -------------------------
# Adaptive Styling (Light + Dark)
# -------------------------
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px !important;
        font-weight: bold;
        padding: 10px;
    }

    /* Light mode */
    .stApp[data-theme="light"] .title { color: #2C3E50; }
    .stApp[data-theme="light"] .result-card {
        background-color: #F8F9F9;
        color: #2C3E50;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    /* Dark mode */
    .stApp[data-theme="dark"] .title { color: #ECF0F1; }
    .stApp[data-theme="dark"] .result-card {
        background-color: #2C3E50;
        color: #ECF0F1;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        margin-top: 20px;
    }

    /* Input box styling */
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #3498DB;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Dashboard Title
# -------------------------
st.markdown('<div class="title">🎓 Student College Allotment Dashboard</div>', unsafe_allow_html=True)

# -------------------------
# Search Student
# -------------------------
student_id = st.text_input("🔍 Enter Student ID to Search:")

if student_id:
    result = df[df["UniqueID"].astype(str) == student_id]

    if not result.empty:
        st.success("✅ Student Found")

        # Display student details in card format
        for _, row in result.iterrows():
            st.markdown(f"""
                <div class="result-card">
                    <h3>👤 {row['Name']} ({row['UniqueID']})</h3>
                    <p><b>🧑 Gender:</b> {row['Gender']}</p>
                    <p><b>🪪 Caste:</b> {row['Caste']}</p>
                    <p><b>📊 Rank:</b> {row['Rank']}</p>
                    <p><b>🏫 Institution:</b> {row['Institution']}</p>
                    <p><b>🏷️ College ID:</b> {row['CollegeID']}</p>
                    <p><b>⭐ Preference Number:</b> {row['PrefNumber']}</p>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.error("❌ Student ID not found in records.")

# -------------------------
# Show All Data (Toggle)
# -------------------------
with st.expander("📋 Show Full Allocation Data"):
    st.dataframe(df, use_container_width=True)
