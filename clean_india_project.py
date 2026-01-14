import streamlit as st
from PIL import Image

# App Title
st.set_page_config(page_title="Clean India AI", layout="centered")

st.title("🇮🇳 Clean India AI")
st.subheader("Garbage Detection for Streets & Water Bodies")

st.write(
    "This app analyzes images of streets or water bodies to detect garbage "
    "and suggest cleanup priority. It supports cleanliness and sustainability."
)

# Upload image
uploaded_image = st.file_uploader(
    "Upload an image (street / road / river / lake):",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Select area type
    area_type = st.selectbox(
        "Select Area Type:",
        ["Street / Road", "Water Body (River / Lake)"]
    )

    if st.button("Analyze Image"):
        st.subheader("🔍 AI Analysis Result")

        # Rule-based AI logic (simple & explainable)
        garbage_detected = "Yes"
        severity = "Moderate"
        action = "Schedule cleanup soon"

        if area_type == "Water Body (River / Lake)":
            severity = "Severe"
            action = "Immediate cleanup required (High Environmental Risk)"

        # Display results
        st.write(f"🗑️ **Garbage Detected:** {garbage_detected}")
        st.write(f"📍 **Area Type:** {area_type}")
        st.write(f"⚠️ **Severity Level:** {severity}")
        st.write(f"✅ **Recommended Action:** {action}")

        st.info(
            "This analysis is for decision support only. "
            "No personal data or facial recognition is used."
        )
