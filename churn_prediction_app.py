import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Retail Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("📊 Retail Customer Churn")

    st.markdown("---")

    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("churn_prediction_app.py")

    if st.button("ℹ️ About", use_container_width=True):
        st.switch_page("pages/About.py")

    if st.button("💬 Feedback", use_container_width=True):
        st.switch_page("pages/Feedback.py")


    st.markdown("---")

    st.subheader("🤖 Model")

    st.write("Logistic Regression")

    st.metric(
        label="ROC-AUC",
        value="0.99"   # replace with your actual ROC-AUC
    )

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("Vimal Raj R")

    st.caption("Version 1.0")

model = joblib.load("churn_model.pkl")

# Cover Image
st.image("assets/cover.png", width="stretch")

st.title("📊 Retail Customer Churn Prediction")
st.subheader(
    "Predict customer churn risk using machine learning insights"
)

st.divider()

# -----------------------------
# Customer Profile
# -----------------------------

st.header("Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    age_group = st.selectbox(
        "Age Group",
        ['18-24','25-34','35-44','45-54','55+']
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ['Male','Female','Other']
    )

with col3:
    region = st.selectbox(
        "Region",
        ['North','South','East','West','Central']
    )

col4, col5 = st.columns(2)

with col4:
    customer_segment = st.selectbox(
        "Customer Segment",
        ['New','Returning','Loyal','VIP']
    )

with col5:
    preferred_channel = st.selectbox(
        "Preferred Channel",
        ['Online','Mobile App','In-Store']
    )

st.divider()

# -----------------------------
# Purchase Behaviour
# -----------------------------

st.header("Purchase Behaviour")

col1, col2 = st.columns(2)

with col1:
    purchase_frequency = st.slider(
        "Purchase Frequency",
        0,60,10
    )

    avg_order_value = st.number_input(
        "Average Order Value",
        min_value=20.0,
        max_value=400.0,
        value=100.0
    )

with col2:
    total_spent = st.number_input(
        "Total Spent",
        min_value=20.0,
        max_value=20000.0,
        value=1000.0
    )

    recency_days = st.number_input(
        "Recency Days",
        min_value=0,
        max_value=365,
        value=30
    )

st.divider()

# -----------------------------
# Engagement
# -----------------------------

st.header("Digital Engagement")

col1, col2 = st.columns(2)

with col1:

    website_visits = st.slider(
        "Website Visits",
        0,500,50
    )

    discount_usage_rate = st.slider(
        "Discount Usage Rate (%)",
        0.0,1.0,0.02
    )

with col2:

    email_open_rate = st.slider(
        "Email Open Rate (%)",
        0.0,1.0,0.02
    )

    cart_abandonment_rate = st.slider(
        "Cart Abandonment Rate (%)",
        0.0,1.0,0.2
    )

st.divider()

# -----------------------------
# Retention Metrics
# -----------------------------

st.header("Retention Metrics")

col1, col2 = st.columns(2)

with col1:
    loyalty_score = st.slider(
        "Loyalty Score",
        0,100,50
    )

with col2:
    engagement_score = st.slider(
        "Engagement Score",
        0,100,50
    )

st.divider()

if st.button("🚀 Predict Churn", use_container_width=True):

    input_df = pd.DataFrame({

        'age_group':[age_group],
        'gender':[gender],
        'region':[region],
        'customer_segment':[customer_segment],
        'preferred_channel':[preferred_channel],
        'purchase_frequency':[purchase_frequency],
        'avg_order_value':[avg_order_value],
        'total_spent':[total_spent],
        'recency_days':[recency_days],
        'website_visits':[website_visits],
        'discount_usage_rate':[discount_usage_rate],
        'email_open_rate':[email_open_rate],
        'cart_abandonment_rate':[cart_abandonment_rate],
        'loyalty_score':[loyalty_score],
        'engagement_score':[engagement_score]
    })

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.divider()
    st.header("Prediction Results")

    if probability >= 0.7:
        st.error("🔴 High Churn Risk")

    elif probability >= 0.4:
        st.warning("🟡 Medium Churn Risk")

    else:
        st.success("🟢 Low Churn Risk")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    c2.metric(
        "Retention Probability",
        f"{(1-probability):.2%}"
    )

    c3.metric(
        "Prediction",
        "Churn" if prediction==1 else "No Churn"
    )

    st.progress(float(probability))

    st.subheader("Recommended Action")

    if probability >= 0.7:
        st.write(
            "• Launch retention campaign\n"
            "• Offer loyalty incentives\n"
            "• Personalized outreach"
        )

    elif probability >= 0.4:
        st.write(
            "• Monitor engagement\n"
            "• Targeted promotions"
        )

    else:
        st.write(
            "• Maintain customer relationship"
        )

# Run this command - python -m streamlit run churn_prediction_app.py