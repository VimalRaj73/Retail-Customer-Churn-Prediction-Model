import streamlit as st

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
    
st.title("ℹ️ About Project")

st.write("""
### Retail Customer Churn Prediction

This project predicts customer churn using
Machine Learning techniques.

### Model
- Logistic Regression

### Features
- Demographics
- Purchase Behaviour
- Engagement Metrics
- Loyalty Metrics

### Technologies
- Python
- Streamlit
- Scikit-Learn
- Pandas
- SHAP
""")