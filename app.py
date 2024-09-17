import streamlit as st
from PIL import Image
import pytesseract
import pyperclip

# Set the Tesseract executable path (if necessary for Windows)
# Uncomment and set the path if running on Windows
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Display the file name instead of the full image
        st.write(f"File name: {uploaded_file.name}")

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Extract text from the image using pytesseract
        st.write("Extracting text from image...")
        try:
            text = pytesseract.image_to_string(image)
            # Display the extracted text
            st.write("Extracted Text:")
            st.text_area("Text from Image", text, height=400, key="text_area")

            # Add copy and download functionality
            st.markdown("""
            <div style="text-align: right;">
                <button onclick="navigator.clipboard.writeText(document.getElementById('text_area').value)">Copy</button>
                <a href="data:text/plain;charset=utf-8," + encodeURIComponent(document.getElementById('text_area').value) download="extracted_text.txt">
                    <button>Download</button>
                </a>
            </div>
            """, unsafe_allow_html=True)
        except pytesseract.TesseractNotFoundError:
            st.error("Tesseract OCR not found. Please ensure Tesseract is installed and the path is set correctly.")

        st.write("Your data is not stored. Don't worry, you are safe.")

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
