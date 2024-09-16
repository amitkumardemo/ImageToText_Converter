import streamlit as st
from PIL import Image
import pytesseract
import io
import base64

# Check if Tesseract is available
try:
    # If Tesseract is not installed or the path is incorrect, this line will raise an error
    pytesseract.get_tesseract_version()
except pytesseract.TesseractNotFoundError:
    st.error("Tesseract OCR not found. Please ensure Tesseract is installed and the path is set correctly.")
    st.stop()

# Set the Tesseract executable path (for Windows users)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Adjust the path based on your cloud environment

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
    
    /* Button Styling */
    .download-button {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        background-color: #0e76a8;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        cursor: pointer;
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
        
        # Display the uploaded image filename
        st.write(f"Uploaded Image: `{uploaded_file.name}`")
        
        # Extract text from the image using pytesseract
        st.write("Extracting text from image...")
        try:
            text = pytesseract.image_to_string(image)
            # Display the extracted text
            st.write("Extracted Text:")
            
            # Create a download link for the text
            def create_download_link(text, filename="extracted_text.txt"):
                b64 = base64.b64encode(text.encode()).decode()
                return f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="download-button">Download Text</a>'
            
            # Display the text area with a copy button
            col1, col2 = st.columns([10, 2])
            with col1:
                st.text_area("Text from Image", text, height=400)
            with col2:
                st.markdown(create_download_link(text), unsafe_allow_html=True)
                st.write(f'<a href="javascript:void(0);" onclick="navigator.clipboard.writeText(\'{text}\')" class="download-button">Copy Text</a>', unsafe_allow_html=True)
                
            # Display a message about data privacy
            st.write("Your data is not stored. Don't worry, you are safe.")

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
