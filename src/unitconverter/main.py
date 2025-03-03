import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f5f5f5;
        }
        .result-box {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<h1 style="color: #000000; text-align: center; font-size: 70px; font-weight: bold; margin-bottom: 10px;">Multi-Unit Converter ⚡</h1>', unsafe_allow_html=True)

# Conversion dictionaries
conversions = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
    },
    "Time": {
        "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400
    },
    "Speed": {
        "Meters/Second": 1, "Kilometers/Hour": 3.6, "Miles/Hour": 2.23694, "Feet/Second": 3.28084
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 1e-6, "Square Mile": 3.861e-7, "Acre": 0.000247105
    },
    "Volume": {
        "Cubic Meter": 1, "Liter": 1000, "Milliliter": 1e6, "Gallon (US)": 264.172
    }
}

# Category selection
st.markdown('<h3 style="color: #000000; font-size: 22px; font-weight: bold; margin-top: 20px;">🔍 Select Conversion Category</h3>', unsafe_allow_html=True)
category = st.selectbox("", list(conversions.keys()))

# Unit selection with columns
st.markdown('<h3 style="color: #000000; font-size: 22px; font-weight: bold; margin-top: 20px;">🔄 Select Units</h3>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
units = list(conversions[category].keys())
from_unit = col1.selectbox("From Unit", units)
to_unit = col2.multiselect("Convert To", units, default=[units[0]])

# Input value
st.markdown('<h3 style="color: #000000; font-size: 22px; font-weight: bold; margin-top: 20px;">✏️ Enter Value</h3>', unsafe_allow_html=True)
value = st.number_input("", value=0.0, step=0.1, format="%.2f")

# Conversion logic
result = {}
if category == "Temperature":
    for unit in to_unit:
        result[unit] = conversions[category][unit](conversions[category][from_unit](value))
else:
    base_value = value / conversions[category][from_unit]
    for unit in to_unit:
        result[unit] = base_value * conversions[category][unit]

# Display results with a stylish box
st.markdown('<h3 style="color: #000000; font-size: 22px; font-weight: bold; margin-top: 20px;">✅ Conversion Results:</h3>', unsafe_allow_html=True)
for unit, res in result.items():
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {res:.2f} {unit}</div>", unsafe_allow_html=True)

