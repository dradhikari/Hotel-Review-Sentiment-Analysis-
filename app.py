import streamlit as st
import joblib
import pandas as pd

# Load the trained model.
model = joblib.load('model.pkl')

# # App layout.
st.set_page_config(page_title="Hotel Review Sentiment Analysis", layout="wide")

# Streamlit UI.
st.title("🏨 Hotel Review Sentiment Analyzer")

st.subheader("Analyze customer feedback for hotels")

# Hotel selection.
hotels_df = pd.DataFrame({
    'Hotel': [
        'Grandover Resort & Spa',
        'Marriott Greensboro Downtown',
        'Holiday Inn Greensboro Coliseum',
        'Sheraton Greensboro at Four Seasons',
        'Drury Inn & Suites Greensboro',
        'Hyatt Place Greensboro',
        'Hilton Garden Inn Greensboro',
        'Courtyard by Marriott Greensboro Airport',
        'Comfort Inn Greensboro',
        'SpringHill Suites by Marriott Greensboro'
    ],
    'Location': ['West', 'Downtown', 'Coliseum', 'Four Seasons', 'West', 
                'Downtown', 'East', 'Airport', 'East', 'West']
})

selected_hotel = st.selectbox("Select a hotel:", hotels_df['Hotel'])

#Rating and review input.
col1, col2 = st.columns(2)
with col1:
    rating = st.slider("Your rating (1-5 stars)", 1, 5, 3)
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("1 = Poor, 3 = Average, 5 = Excellent")


# Input
review = st.text_area(" ✍️ Enter your review:")

# Predict
if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review.")
    else:
        prediction = model.predict([review])[0]
        if prediction.lower() == "happy":
            st.success("😊 Sentiment: **Happy**")
        else:
            st.error("😞 Sentiment: **Not Happy**")


# st.metric("Predicted Sentiment",  )
st.write(f"Hotel: {selected_hotel}")

st.write(f"Rating: {'⭐' * rating}")

# # Add some space at the bottom.
st.markdown("<br><br>", unsafe_allow_html=True) 



