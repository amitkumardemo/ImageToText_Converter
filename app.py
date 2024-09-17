import streamlit as st
from PIL import Image
import pytesseract
import pyperclip
import io

# Set the Tesseract executable path (for Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set page configuration
st.set_page_config(page_title="Image to Text Generator", layout="wide")

# Custom CSS for navbar and footer
st.markdown("""
    <style>
    /* Style for Navbar */
    .navbar {
        background-color: #0e76a8;
        overflow: hidden;
    }
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
    }
    .navbar a:hover {
        background-color: #575757;
        color: white;
    }
    
    /* Footer Styling */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #0e76a8;
        color: white;
        text-align: center;
        padding: 10px;
    }
    
    /* Icon styling */
    .icon {
        cursor: pointer;
        font-size: 20px;
        color: #0e76a8;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo
st.image("https://via.placeholder.com/150", width=150)  # Placeholder logo (replace with your logo URL)

# Navbar
st.markdown("""
<div class="navbar">
  <a href="#home">Home</a>
  <a href="#about">About</a>
  <a href="https://github.com/your-repo" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)

# Add navigation to different sections
menu = ["Home", "About"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Home":
    # Home Page
    st.title("Image to Text Generator")
    st.write("Upload an image and extract the text using Optical Character Recognition (OCR).")

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Get the file name
        file_name = uploaded_file.name

        # Display the file name
        st.write(f"Uploaded File: {file_name}")

        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Extract text from the image using pytesseract
        st.write("Extracting text from image...")
        try:
            text = pytesseract.image_to_string(image)

            # Display the extracted text with icons
            text_area_key = f"text_area_{file_name}"
            col1, col2 = st.columns([8, 2])
            with col1:
                st.text_area("Text from Image", text, height=400, key=text_area_key)
            with col2:
                # Copy button
                if st.button("📋 Copy Text", key="copy_button"):
                    pyperclip.copy(text)
                    st.success("Text copied to clipboard!")

                # Download button
                if st.download_button(
                    label="📥 Download Text",
                    data=text,
                    file_name="extracted_text.txt",
                    mime="text/plain",
                    key="download_button"
                ):
                    st.success("Text downloaded successfully!")

        except pytesseract.TesseractNotFoundError:
            st.error("Tesseract OCR not found. Please ensure Tesseract is installed and the path is set correctly.")

elif choice == "About":
    # About Page
    st.title("About Image to Text Generator")
    st.write("""
    This tool allows you to upload an image and extract the text contained in the image using Optical Character Recognition (OCR).
    The project uses the Python library `pytesseract` to handle OCR and `Pillow` for image processing.
    
    **Features**:
    - Upload an image in JPG, PNG, or JPEG format.
    - Extract text from the image.
    - Simple and easy-to-use interface.

    **Technology Stack**:
    - Streamlit (for building the web app)
    - pytesseract (for OCR)
    - Pillow (for image handling)
    """)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2024 Image to Text Generator | Developed by Your Name</p>
    <a href="https://www.linkedin.com" style="color:white; margin-right: 10px;">LinkedIn</a>
    <a href="https://www.twitter.com" style="color:white; margin-right: 10px;">Twitter</a>
    <a href="https://github.com/your-repo" style="color:white;">GitHub</a>
</div>
""", unsafe_allow_html=True)
