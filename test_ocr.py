import streamlit as st
from mistralai import Mistral
import os

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Mistral Smart OCR",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Custom CSS for Attractive UI ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #2e4057; font-family: 'Helvetica Neue', sans-serif; }
    div.stButton > button {
        background: linear-gradient(to right, #4b6cb7, #182848);
        color: white; border: none; padding: 10px 24px;
        border-radius: 8px; font-size: 18px; font-weight: bold;
        width: 100%; transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02); box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stFileUploader {
        border: 2px dashed #4b6cb7; border-radius: 10px;
        padding: 20px; background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. Sidebar (Settings & Info) ---
with st.sidebar:
    st.image("https://mistral.ai/images/logo_hubc88c4ece131b91c7cb751f414740531_48462_256x256_fit_q75_h2_box_2.webp", width=60)
    st.title("⚙️ Settings")
    st.markdown("---")
    
    # --- SECURE API KEY HANDLING (FIXED FOR LOCAL RUN) ---
    default_key = ""
    
    try:
        # Hum try karenge secrets file dhoondhne ki
        # Agar local computer par file nahi mili, toh error aayega jise hum 'except' mein pakad lenge
        if "MISTRAL_API_KEY" in st.secrets:
            default_key = st.secrets["MISTRAL_API_KEY"]
    except (FileNotFoundError, Exception):
        # Agar koi error aaya (matlab hum local laptop par hain bina secrets file ke), toh ignore karo
        pass
    
    # User Input (Agar cloud se key mil gayi toh hidden rahegi, nahi toh user daal sakta hai)
    api_key = st.text_input("API Key", value=default_key, type="password", help="Enter your Mistral API Key here.")
    
    st.markdown("---")
    st.info("💡 **Tip:** Upload a clear image for the best results.")
    st.write("Made with ❤️ using Mistral AI")

# --- 4. Main Header ---
st.title("🧠 Mistral Intelligent OCR")
st.markdown("##### Transform your images into editable text instantly (Global Access).")
st.markdown("---")

# --- 5. Main Content Area ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg', 'webp', 'pdf'])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Preview", use_container_width=True)
        st.success(f"File '{uploaded_file.name}' loaded successfully!")

with col2:
    st.subheader("📄 Extracted Result")
    
    if uploaded_file is None:
        st.info("👈 Please upload an image from the left panel to start.")
    else:
        if st.button("✨ Extract Text Now"):
            
            if not api_key:
                st.error("⚠️ API Key is missing! Please enter it in the sidebar.")
            else:
                try:
                    progress_text = "Analyzing document structure..."
                    my_bar = st.progress(0, text=progress_text)
                    
                    with st.spinner("Mistral AI is reading your file..."):
                        
                        client = Mistral(api_key=api_key)
                        
                        # Update Progress
                        my_bar.progress(30, text="Uploading to secure server...")

                        # 1. Upload
                        mistral_file = client.files.upload(
                            file={
                                "file_name": uploaded_file.name,
                                "content": uploaded_file.getvalue(), 
                            },
                            purpose="ocr"
                        )
                        
                        my_bar.progress(60, text="Processing OCR...")

                        # 2. Get URL
                        signed_url = client.files.get_signed_url(file_id=mistral_file.id)

                        # 3. Process
                        ocr_response = client.ocr.process(
                            model="mistral-ocr-latest",
                            document={
                                "type": "image_url",
                                "image_url": signed_url.url
                            }
                        )
                        
                        my_bar.progress(100, text="Done!")
                        my_bar.empty()
                        
                        # --- Result Display ---
                        markdown_text = ocr_response.pages[0].markdown
                        
                        st.success("Extraction Complete! 🎉")
                        
                        tab1, tab2 = st.tabs(["👁️ Formatted View", "📝 Raw Text / Copy"])
                        
                        with tab1:
                            st.markdown("### Preview")
                            st.markdown(markdown_text)
                            
                        with tab2:
                            st.text_area("Copy content:", value=markdown_text, height=400)
                            
                            st.download_button(
                                label="📥 Download as Text File",
                                data=markdown_text,
                                file_name=f"ocr_result_{uploaded_file.name}.txt",
                                mime="text/plain"
                            )

                except Exception as e:
                    st.error(f"❌ Error Occurred: {str(e)}")