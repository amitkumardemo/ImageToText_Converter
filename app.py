import streamlit as st
from PIL import Image
import pytesseract
import streamlit.components.v1 as components

# Set the Tesseract executable path (if necessary for Windows)
# Uncomment and set the path if running on Windows
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set page configuration
st.set_page_config(page_title="Image to Text Generator", layout="wide")

# Custom CSS for navbar, footer, and buttons
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

    /* Button styling */
    .icon-btn {
        background-color: #0e76a8;
        color: white;
        border: none;
        padding: 8px 16px;
        cursor: pointer;
        border-radius: 5px;
        font-size: 14px;
        margin-right: 5px;
    }

    .icon-btn:hover {
        background-color: #575757;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo
st.image("jb.png", width=250)  # Placeholder logo (replace with your logo URL)

# Navbar
st.markdown("""
<div class="navbar">
  <a href="#Home">Home</a>
  <a href="#About">About</a>
  <a href="https://techiehelpt.netlify.app/">BackToWebsite</a>
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

        # Display the file name
        st.write(f"File name: **{uploaded_file.name}**")

        # Extract text from the image using pytesseract
        st.write("Extracting text from image...")
        try:
            text = pytesseract.image_to_string(image)

            # Display the extracted text in a text area
            st.text_area("Extracted Text", text, height=300, key="text_area")

            # Add download button
            st.download_button(
                label="📥 Download Text",
                data=text,
                file_name="extracted_text.txt",
                mime="text/plain",
                key="download_button"
            )

            # Add copy button with JavaScript
            components.html(f"""
            <script>
            function copyToClipboard() {{
                const text = `{text.replace("`", "\\`")}`;
                navigator.clipboard.writeText(text).then(() => {{
                    alert('Text copied to clipboard!');
                }});
            }}
            </script>
            <button class="icon-btn" onclick="copyToClipboard()">📋 Copy Text</button>
            """, height=50, scrolling=False)

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
    <p>© 2024 Image to Text Generator | TechieHelp</p>
    <a href="https://www.linkedin.com/in/techiehelp" style="color:white; margin-right: 10px;">LinkedIn</a>
    <a href="https://www.twitter.com/techiehelp" style="color:white; margin-right: 10px;">Twitter</a>
    <a href="https://www.instagram.com/techiehelp2" style="color:white;">Instagram</a>
</div>
""", unsafe_allow_html=True)
