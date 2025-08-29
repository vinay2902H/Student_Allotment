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
file_path = "allotment_results.csv"
df = pd.read_csv(file_path)

# -------------------------
# Custom CSS
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
    .badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        margin: 3px;
        font-size: 14px;
        color: white;
        font-weight: 500;
    }
    .blue { background-color: #3498DB; }
    .green { background-color: #2ECC71; }
    .orange { background-color: #E67E22; }
    .purple { background-color: #9B59B6; }
    .card {
        padding: 20px;
        border-radius: 15px;
        margin-top: 15px;
        background: linear-gradient(135deg, #f8f9f9, #ecf0f1);
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
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

        row = result.iloc[0]

        # Student Card with Badges
        st.markdown(f"""
            <div class="card">
                <h3>👤 {row['Name']} ({row['UniqueID']})</h3>
                <span class="badge blue">Gender: {row['Gender']}</span>
                <span class="badge green">Caste: {row['Caste']}</span>
                <span class="badge orange">Rank: {row['Rank']}</span>
                <span class="badge purple">College ID: {row['CollegeID']}</span>
            </div>
        """, unsafe_allow_html=True)

        # Tabs for Details
        tabs = st.tabs(["📊 Rank & Performance", "🏫 College Details", "📋 Full Profile"])
        with tabs[0]:
            rank = int(row['Rank'])
            max_rank = int(df['Rank'].max())
            progress = 1 - (rank / max_rank)
            st.progress(progress)
            st.write(f"📊 Rank Position: **{rank} out of {max_rank}**")

        with tabs[1]:
            st.write(f"🏫 Institution: **{row['Institution']}**")
            st.write(f"⭐ Preference Number: **{row['PrefNumber']}**")

        with tabs[2]:
            st.write(f"👤 Name: {row['Name']}")
            st.write(f"🧑 Gender: {row['Gender']}")
            st.write(f"🪪 Caste: {row['Caste']}")
            st.write(f"📊 Rank: {row['Rank']}")
            st.write(f"🏫 Institution: {row['Institution']}")
            st.write(f"🏷️ College ID: {row['CollegeID']}")
            st.write(f"⭐ Preference Number: {row['PrefNumber']}")

    else:
        st.error("❌ Student ID not found in records.")

# -------------------------
# Show All Data (Leaderboard with Highlight)
# -------------------------
with st.expander("📋 Show Full Allocation Data (Leaderboard)"):
    def highlight_student(s):
        return ['background-color: #ffeaa7' if str(s.UniqueID) == student_id else '' for _ in s]

    st.dataframe(df.style.apply(highlight_student, axis=1), use_container_width=True)
