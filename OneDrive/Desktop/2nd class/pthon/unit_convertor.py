import streamlit as st

# 🎨 Styling for White Background & Clear Text
st.markdown("""
    <style>
        /* Page Background - White */
        .stApp { background-color: #ffffff !important; }
        [data-testid="stSidebar"] { background-color: #f8f9fa !important; border-right: 2px solid #ccc; }

        /* Google Fonts for Clear Text */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        /* Main Heading */
        .main-heading {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            padding: 15px;
            color: #333333;
            font-family: 'Roboto', sans-serif;
        }

        /* Category Title */
        .category-title {
            font-size: 20px;
            font-weight: 600;
            color: #007bff;
            text-align: center;
            padding: 10px;
            border-bottom: 2px solid #007bff;
            font-family: 'Poppins', sans-serif;
        }

        /* Section Headings */
        .section-heading {
            font-size: 28px; 
            font-weight: 600; 
            color: #ff5722; 
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 2px solid #ff5722;
            font-family: 'Poppins', sans-serif;
        }

        /* Sidebar Labels */
        .field-label {
            font-size: 18px; 
            font-weight: 500; 
            color: #333333; 
            padding-bottom: 5px;
            font-family: 'Poppins', sans-serif;
        }

        /* Results Styling */
        .result-text {
            color: #28a745; 
            font-size: 24px; 
            font-weight: 600; 
            text-align: center;
            font-family: 'Roboto', sans-serif;
        }

        /* Button Styling */
        div.stButton > button {
            background: #007bff;
            border-radius: 10px;
            color: white;
            font-weight: bold;
            padding: 10px 18px;
            border: none;
            transition: 0.3s ease;
            font-family: 'Poppins', sans-serif;
        }
        
        div.stButton > button:hover {
            background: #0056b3;
            box-shadow: 0 0 10px #007bff;
        }

    </style>
""", unsafe_allow_html=True)

# Main Heading
st.markdown('<h1 class="main-heading">🔢 Ultimate Unit Converter 🔢</h1>', unsafe_allow_html=True)

# Sidebar Category Title
st.sidebar.markdown('<h2 class="category-title">⚙ Select Conversion Type</h2>', unsafe_allow_html=True)

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000}
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
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
    else:
        return value

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462}
    return value * (weight_units[to_unit] / weight_units[from_unit])

conversion_type = st.sidebar.selectbox("", ["Temperature", "Length", "Weight"], key="conversion_type")

if conversion_type == "Length":
    st.markdown('<h2 class="section-heading">📏 Length Converter</h2>', unsafe_allow_html=True)
    from_unit = st.sidebar.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter"], key="length_from")
    to_unit = st.sidebar.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter"], key="length_to")
    value = st.sidebar.number_input("Enter Value", min_value=0.0, format="%.2f", key="length_value")
    if st.sidebar.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.markdown(f'<p class="result-text">✅ {value} {from_unit} = {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif conversion_type == "Temperature":
    st.markdown('<h2 class="section-heading">🌡 Temperature Converter</h2>', unsafe_allow_html=True)
    from_unit = st.sidebar.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    to_unit = st.sidebar.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    value = st.sidebar.number_input("Enter Value", min_value=-100.0, format="%.2f", key="temp_value")
    if st.sidebar.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.markdown(f'<p class="result-text">✅ {value}°{from_unit[0]} = {result:.2f}°{to_unit[0]}</p>', unsafe_allow_html=True)

elif conversion_type == "Weight":
    st.markdown('<h2 class="section-heading">⚖ Weight Converter</h2>', unsafe_allow_html=True)
    from_unit = st.sidebar.selectbox("From Unit", ["Gram", "Kilogram", "Pound"], key="weight_from")
    to_unit = st.sidebar.selectbox("To Unit", ["Gram", "Kilogram", "Pound"], key="weight_to")
    value = st.sidebar.number_input("Enter Value", min_value=0.0, format="%.2f", key="weight_value")
    if st.sidebar.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.markdown(f'<p class="result-text">✅ {value} {from_unit} = {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

st.markdown('<p style="color:#333; text-align:center;">🚀 Developed by Ambreen Naqvi</p>', unsafe_allow_html=True)
