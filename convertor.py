# Project 01: Unit Converter using Python and Streamlit

import streamlit as st

# Apply Custom Styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        color: white;
        text-align: center;
        font-size: 36px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: background 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
        cursor: pointer;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.3);
        color: blue;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: black;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1>🔣🌡️ Unit Converter using Python and Streamlit ⚖️</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of **Length, Weight, and Temperature**.")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", min_value=0.0, value=0.0, step=0.1)

# Layout for unit selection
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Yards", "Inches", "Nautical Miles"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Yards", "Inches", "Nautical Miles"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilograms", "Grams", "Pounds", "Ounces", "Tons", "Stones"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilograms", "Grams", "Pounds", "Ounces", "Tons", "Stones"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 1000.0,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Yards": 0.9144,
        "Inches": 0.0254,
        "Nautical Miles": 1852.0,
    }
    try:
        return value * length_units[from_unit] / length_units[to_unit]
    except KeyError:
        return None  # Handle invalid unit selection

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Tons": 907.185,
        "Stones": 6.35029,
    }
    try:
        return value * weight_units[from_unit] / weight_units[to_unit]
    except KeyError:
        return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    try:
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    except:
        return None  # Handle invalid unit selection

# Button for conversion
if st.button("🔄 Convert"):
    result = None

    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    # Display the result
    if result is not None:
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    else:
        st.error("Please select valid units for conversion.")

# Footer
st.markdown("<div class='footer'>Designed & Developed by Nida Iqbal</div>", unsafe_allow_html=True)
