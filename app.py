import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model
model = joblib.load("notebooks/real_estate_price_model.pkl")

st.set_page_config(page_title="Real Estate Price Estimator by hardikjha", layout="centered")

st.title("🏡 Real Estate Price Estimator")

st.markdown("by hardikjha")
st.markdown("Enter the specifications of the house you want")

# 📥 User inputs
zipcode = st.selectbox("Zipcode", [
    98001, 98002, 98003, 98004, 98005, 98006, 98007, 98008, 98010, 98011,
    98014, 98019, 98022, 98023, 98024, 98027, 98028, 98029, 98030, 98031,
    98032, 98033, 98034, 98038, 98039, 98040, 98042, 98045, 98052, 98053,
    98055, 98056, 98058, 98059, 98065, 98070, 98072, 98074, 98075, 98077,
    98092, 98102, 98103, 98105, 98106, 98107, 98108, 98109, 98112, 98115,
    98116, 98117, 98118, 98119, 98122, 98125, 98126, 98133, 98136, 98144,
    98146, 98148, 98155, 98166, 98168, 98177, 98178, 98188, 98198, 98199
])  # Or load unique zipcodes from training data

sqft_living = st.slider("Living Area (sqft)", 300, 10000, 1500)
sqft_lot = st.slider("Lot Area (sqft)", 500, 100000, 5000)
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1.0, 6.0, 2.0, step=0.25)
floors = st.number_input("Floors", 1.0, 4.0, 1.0, step=0.5)
waterfront = st.selectbox("Waterfront", ["No", "Yes"])
view = st.slider("View Score (0-4)", 0, 4, 0)
condition = st.slider("Condition (1-5)", 1, 5, 3)
grade = st.slider("Grade (1-13)", 1, 13, 7)
sqft_above = st.slider("Sqft Above", 300, 10000, 1500)
sqft_basement = st.slider("Sqft Basement", 0, 5000, 0)
house_age = st.slider("House Age", 0, 115, 20)
is_renovated = st.selectbox("Has Been Renovated?", ["No", "Yes"])
lat = st.number_input("Latitude", value=47.5112)
long = st.number_input("Longitude", value=-122.257)
sqft_living15 = st.slider("Sqft Living (Neighbors Avg)", 400, 6000, 1500)
sqft_lot15 = st.slider("Sqft Lot (Neighbors Avg)", 500, 50000, 5000)


# 🧮 Convert inputs to numeric
waterfront = 1 if waterfront == "Yes" else 0
is_renovated = 1 if is_renovated == "Yes" else 0

# 📊 Create input DataFrame
input_data = pd.DataFrame([{
    "zipcode": zipcode,
    "sqft_living": sqft_living,
    "sqft_lot": sqft_lot,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "floors": floors,
    "waterfront": waterfront,
    "view": view,
    "condition": condition,
    "grade": grade,
    "sqft_above": sqft_above,
    "sqft_basement": sqft_basement,
    "house_age": house_age,
    "is_renovated": is_renovated,
    "lat": lat,
    "long": long,
    "sqft_living15": sqft_living15,
    "sqft_lot15": sqft_lot15
}])


# 🧠 Predict button
if st.button("Estimate Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Price: ${prediction:,.0f}")