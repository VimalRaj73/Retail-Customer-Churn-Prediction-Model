import streamlit as st
import pandas as pd
import os

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

st.title("💬 Feedback")

name = st.text_input("Name")

rating = st.slider(
    "Rating",
    1,
    5,
    5
)

feedback = st.text_area("Feedback")

if st.button("Submit"):

    row = pd.DataFrame({
        "Name":[name],
        "Rating":[rating],
        "Feedback":[feedback]
    })

    if os.path.exists("feedback.csv"):
        row.to_csv(
            "feedback.csv",
            mode="a",
            header=False,
            index=False
        )
    else:
        row.to_csv(
            "feedback.csv",
            index=False
        )

    st.success("Feedback submitted successfully!")