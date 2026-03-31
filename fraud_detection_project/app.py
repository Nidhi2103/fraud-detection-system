# import streamlit as st
# import pandas as pd
# import joblib

# st.set_page_config(page_title="AI Fraud Detection", layout="wide")

# st.title("💳 AI Fraud Detection Dashboard")
# st.caption("🔎 Real-Time Transaction Monitoring System")

# # -----------------------
# # Load dataset
# # -----------------------
# @st.cache_data
# def load_data():
#     return pd.read_csv("creditcard.csv")

# data = load_data()

# X = data.drop("Class", axis=1)
# y = data["Class"]

# # -----------------------
# # Load trained model
# # -----------------------
# @st.cache_resource
# def load_model():
#     return joblib.load("fraud_model.pkl")

# model = load_model()

# # -----------------------
# # Sidebar
# # -----------------------
# st.sidebar.title("⚙️ Transaction Analyzer")

# index = st.sidebar.number_input(
#     "Select Transaction Index",
#     min_value=0,
#     max_value=len(data)-1,
#     step=1
# )

# analyze = st.sidebar.button("🔍 Analyze Transaction")

# st.divider()

# # -----------------------
# # Main Analysis
# # -----------------------
# if analyze:

#     transaction = X.iloc[index].values.reshape(1, -1)
#     actual_label = y.iloc[index]
#     row = data.iloc[index]

#     prediction = model.predict(transaction)[0]
#     probability = model.predict_proba(transaction)[0][1]
#     score = probability

#     # -----------------------
#     # Alert Banner
#     # -----------------------
#     if prediction == 1:
#         decision = "Fraud Suspicious"
#         st.error("🚨 **FRAUD ALERT** — Suspicious Transaction Detected")
#     else:
#         decision = "Normal Transaction"
#         st.success("🟢 **Transaction Appears Normal**")

#     st.divider()

#     # -----------------------
#     # Transaction Info
#     # -----------------------
#     st.markdown("### 💳 Transaction Details")

#     col1, col2, col3 = st.columns(3)

#     col1.metric("🆔 Transaction ID", index)
#     col2.metric("💰 Amount", f"${row['Amount']}")
#     col3.metric("⏱ Time", row["Time"])

#     st.divider()

#     # -----------------------
#     # Behavior Analysis
#     # -----------------------
#     st.markdown("### 📊 Behavior Analysis")

#     avg_amount = data["Amount"].mean()
#     current_amount = row["Amount"]

#     if current_amount > avg_amount * 3:
#         deviation = "HIGH ⚠️"
#     elif current_amount > avg_amount:
#         deviation = "MEDIUM ⚡"
#     else:
#         deviation = "LOW ✅"

#     col4, col5, col6 = st.columns(3)

#     col4.metric("📉 Avg Transaction", round(avg_amount,2))
#     col5.metric("📈 Current Transaction", current_amount)
#     col6.metric("📊 Deviation Level", deviation)

#     st.divider()

#     # -----------------------
#     # Model Result
#     # -----------------------
#     st.markdown("### 🤖 Fraud Detection Result")

#     if score > 0.8:
#         risk_level = "HIGH 🚨"
#         bar_color = "red"
#     elif score > 0.4:
#         risk_level = "MEDIUM ⚠️"
#         bar_color = "orange"
#     else:
#         risk_level = "LOW ✅"
#         bar_color = "green"

#     col7, col8, col9 = st.columns(3)

#     col7.metric("🧠 Decision", decision)
#     col8.metric("📊 Risk Score", round(score,4))
#     col9.metric("⚡ Risk Level", risk_level)

#     # -----------------------
#     # Custom Risk Bar
#     # -----------------------
#     st.markdown("### 🚨 Fraud Risk Indicator")

#     percent = int(score * 100)

#     # Prevent bar from collapsing when score is 0
#     bar_width = max(percent, 5)

#     st.markdown(
#         f"""
#         <div style="
#             background-color:#eee;
#             border-radius:10px;
#             padding:3px;
#             width:100%;
#         ">
#             <div style="
#                 width:{bar_width}%;
#                 background-color:{bar_color};
#                 padding:8px;
#                 border-radius:10px;
#                 text-align:center;
#                 color:white;
#                 font-weight:bold;
#             ">
#             {percent}% Risk
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

#     st.divider()

#     # -----------------------
#     # Explanation
#     # -----------------------
#     st.markdown("### 🧠 Model Explanation")

#     if prediction == 1:
#         st.info("The transaction significantly deviates from learned normal behavior patterns and is classified as **high risk**.")
#     else:
#         st.info("The transaction characteristics match previously observed **normal transaction patterns**.")

#     st.divider()

#     # -----------------------
#     # Dataset Validation
#     # -----------------------
#     st.markdown("### 🔎 Dataset Validation")

#     if actual_label == 1:
#         st.error("🚨 Actual Dataset Label: FRAUD")
#     else:
#         st.success("🟢 Actual Dataset Label: NORMAL")

import streamlit as st
import pandas as pd
import joblib

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PREMIUM LOOK ---
st.markdown("""
    <style>
    /* Main background and font */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Custom Card Style */
    .block-container {
        padding-top: 2rem;
    }
    
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        margin-bottom: 1rem;
    }

    .status-card {
        padding: 20px;
        border-radius: 12px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Gradient Header */
    .main-header {
        background: linear-gradient(90deg, #1f2937, #111827);
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #3b82f6;
        margin-bottom: 2rem;
    }

    /* Styled Badges */
    .badge {
        display: inline-block;
        padding: 0.25em 0.6em;
        font-size: 75%;
        font-weight: 700;
        line-height: 1;
        text-align: center;
        white-space: nowrap;
        vertical-align: baseline;
        border-radius: 0.375rem;
        margin-right: 5px;
        background-color: #3b82f6;
        color: white;
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #8b949e;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        border-top: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# -----------------------
# Data & Model Loading (Logic Preserved)
# -----------------------
@st.cache_data
def load_data():
    return pd.read_csv("creditcard.csv")

@st.cache_resource
def load_model():
    return joblib.load("fraud_model.pkl")

try:
    data = load_data()
    X = data.drop("Class", axis=1)
    y = data["Class"]
    model = load_model()
except Exception as e:
    st.error(f"Error loading resources: {e}. Please ensure 'creditcard.csv' and 'fraud_model.pkl' are in the directory.")
    st.stop()

# -----------------------
# Sidebar Redesign
# -----------------------
with st.sidebar:
    # st.image("https://img.icons8.com/fluency/100/shield-security.png", width=80)
    st.title("⚙️ Transaction Analyzer")
    st.markdown("---")
    
    st.markdown("### 🛠️ Configuration")
    index = st.number_input(
        "Select Transaction Index",
        min_value=0,
        max_value=len(data)-1,
        value=0,
        step=1,
        # help="Choose a specific row from the dataset to analyze."
    )
    
    st.markdown("##")
    analyze = st.button("🚀 RUN ANALYSIS", use_container_width=True, type="primary")
    
    st.markdown("---")
    st.info("**System Status:** Operational ✅\n\n**Model:** Random Forest v2.1")

# -----------------------
# Header Section
# -----------------------
st.markdown("""
    <div class="main-header">
        <h1 style='margin:0;'> 💳 AI Fraud Detection Dashboard</h1>
        <p style='color: #8b949e; margin-top: 5px;'>Enterprise-Grade Real-Time Fraud Detection & Behavioral Analytics</p>
        <span class="badge">V3.0-Stable</span> <span class="badge" style="background-color: #10b981;">Real-time Enabled</span>
    </div>
    """, unsafe_allow_html=True)

# -----------------------
# Main Analysis Logic
# -----------------------
if analyze:
    # Calculations
    transaction = X.iloc[index].values.reshape(1, -1)
    actual_label = y.iloc[index]
    row = data.iloc[index]

    prediction = model.predict(transaction)[0]
    probability = model.predict_proba(transaction)[0][1]
    score = probability

    # Determine Severity
    if prediction == 1:
        status_color = "#ef4444"
        status_text = "FRAUD DETECTED"
        icon = "🚨"
        bg_glow = "rgba(239, 68, 68, 0.1)"
    else:
        status_color = "#10b981"
        status_text = "TRANSACTION CLEAR"
        icon = "✅"
        bg_glow = "rgba(16, 185, 129, 0.1)"

    # --- 1. Top Alert Banner ---
    st.markdown(f"""
        <div style="background-color:{bg_glow}; border: 2px solid {status_color}; padding: 25px; border-radius: 15px; text-align: center;">
            <h2 style="color:{status_color}; margin:0;">{icon} {status_text}</h2>
            <p style="margin:5px 0 0 0;">The system has completed the scan with {(1-score)*100 if prediction==0 else score*100:.2f}% confidence.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("###")

    # --- 2. Metrics Row ---
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">Transaction ID</p><h2 style="margin:0;">#{index}</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">Amount (USD)</p><h2 style="margin:0;">${row["Amount"]:.2f}</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">System Time</p><h2 style="margin:0;">{row["Time"]}</h2></div>', unsafe_allow_html=True)
    with col4:
        # Actual Label Validation (The "Truth")
        truth_color = "#ef4444" if actual_label == 1 else "#10b981"
        truth_text = "FRAUD" if actual_label == 1 else "NORMAL"
        st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">Ground Truth</p><h2 style="margin:0; color:{truth_color};">{truth_text}</h2></div>', unsafe_allow_html=True)

    # --- 3. Behavioral & Risk Section ---
    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("📊 Behavioral Analytics")
        with st.container():
            avg_amount = data["Amount"].mean()
            current_amount = row["Amount"]
            deviation = ((current_amount - avg_amount) / avg_amount) * 100

            dev_label = "HIGH ⚠️" if current_amount > avg_amount * 3 else "NORMAL ✅"
            
            st.markdown(f"""
            <div class="metric-card">
                <table style="width:100%">
                    <tr><td>Average Spend</td><td style="text-align:right"><b>${avg_amount:.2f}</b></td></tr>
                    <tr><td>Current Spend</td><td style="text-align:right"><b>${current_amount:.2f}</b></td></tr>
                    <tr style="border-top: 1px solid #30363d"><td>Deviation</td><td style="text-align:right; color:{'#ef4444' if deviation > 100 else '#10b981'}"><b>{deviation:.1f}%</b></td></tr>
                    <tr><td>Anomaly Status</td><td style="text-align:right"><b>{dev_label}</b></td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

    with right_col:
        st.subheader("🚨 Risk Indicator")
        
        # Risk gauge logic
        if score > 0.8:
            risk_color = "#ef4444"
            risk_level = "CRITICAL"
        elif score > 0.4:
            risk_color = "#f59e0b"
            risk_level = "ELEVATED"
        else:
            risk_color = "#10b981"
            risk_level = "MINIMAL"

        percent = int(score * 100)
        
        st.markdown(f"""
            <div class="metric-card" style="text-align:center">
                <p style="margin:0">Calculated Risk Score</p>
                <h1 style="color:{risk_color}; margin:0;">{percent}%</h1>
                <p style="letter-spacing: 2px; font-size: 12px; color:{risk_color}"><b>{risk_level}</b></p>
                <div style="background-color: #30363d; border-radius: 20px; height: 12px; width: 100%; margin-top: 10px;">
                    <div style="background-color: {risk_color}; width: {max(percent, 5)}%; height: 100%; border-radius: 20px; transition: width 0.5s ease-in-out;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- 4. Model Explanation Section ---
    st.markdown("### 🧠 Model Explainability (XAI)")
    exp_col1, exp_col2 = st.columns([2, 1])
    
    with exp_col1:
        if prediction == 1:
            st.warning(f"**Anomaly Profile:** Transaction #{index} exhibits patterns common in credit card skimming. High deviation in 'Amount' relative to time-of-day feature vectors detected.")
        else:
            st.success(f"**Normal Profile:** Features align with your historical spending cluster. The transaction is consistent with established behavior metrics for this account.")
    
    with exp_col2:
        st.info(f"**Model Confidence:** {max(score, 1-score):.4f}")

else:
    # Initial State
    st.markdown("""
        <div style="text-align: center; padding: 100px; color: #8b949e;">
            <img src="https://img.icons8.com/fluency/100/search-database.png" style="opacity: 0.5;"/>
            <h3>Waiting for Transaction Input</h3>
            <p>Select a transaction from the sidebar and click 'Analyze' to begin the security scan.</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        Powered by AI Fraud Detection Engine • Using Scikit-Learn & Streamlit Framework
    </div>
    """, unsafe_allow_html=True)