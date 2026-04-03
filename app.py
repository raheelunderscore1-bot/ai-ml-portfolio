import streamlit as st

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="AI Engineering Portfolio", layout="wide")

# Custom CSS for spacing and button styling
st.markdown("""
    <style>
    .project-header { color: #1E3A8A; margin-bottom: 5px; }
    .stVideo { border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    hr { margin-top: 2rem; margin-bottom: 2rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Strategic AI & Medical Technology Portfolio")
st.subheader("Bridging Multi-modal AI with Real-World Engineering")
st.divider()

# --- 2. THE DATA (Replace YOUR_ID with your Google Drive direct link IDs) ---
projects = [
    {
        "title": "🩸 AI based Grid Management",
        "desc": "Predictive IoT monitoring for Peritoneal Dialysis using Gemini 3 Flash Vision for tube/effluent analysis.",
        "video_url": "https://drive.google.com/uc?export=download&id=1DFfIFmdBV4XbLGzjmapjzaxmDfKf4hW8",
        "pdf_url": "https://drive.google.com/uc?export=download&id=1z5rtlmHFogwD1brJDScsY-H64GMYC4zS"
    },
    {
        "title": "🩸 AI Dialysis Monitoring Dashboard",
        "desc": "Predictive IoT monitoring for Peritoneal Dialysis using Gemini 3 Flash Vision for tube/effluent analysis.",
        "video_url": "https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID_1",
        "pdf_url": "https://drive.google.com/uc?export=download&id=YOUR_PDF_ID_1"
    },
{
        "title": "🩸 AI Dialysis Monitoring Dashboard",
        "desc": "Predictive IoT monitoring for Peritoneal Dialysis using Gemini 3 Flash Vision for tube/effluent analysis.",
        "video_url": "https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID_1",
        "pdf_url": "https://drive.google.com/uc?export=download&id=YOUR_PDF_ID_1"
    },
    {
        "title": "👁️ Image Detector Bot (Engineering)",
        "desc": "Automated R&D documentation agent that identifies hardware components and generates technical logs.",
        "video_url": "https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID_2",
        "pdf_url": "https://drive.google.com/uc?export=download&id=YOUR_PDF_ID_2"
    },
    {
        "title": "💳 Customer Buying Behavior AI",
        "desc": "K-Means clustering pipeline that segments 8,000+ credit card users into actionable behavioral profiles.",
        "video_url": "https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID_3",
        "pdf_url": "https://drive.google.com/uc?export=download&id=YOUR_PDF_ID_3"
    },
    {
        "title": "🍕 Restaurant Conversational Agent",
        "desc": "Trained Gemini model for hospitality, handling multi-turn orders and dietary constraints.",
        "video_url": "https://drive.google.com/uc?export=download&id=YOUR_VIDEO_ID_4",
        "pdf_url": "https://drive.google.com/uc?export=download&id=YOUR_PDF_ID_4"
    }
]

# --- 3. THE GALLERY RENDERER ---
for p in projects:
    # Create the Split: Video on Left (60%), Info/Button on Right (40%)
    col_vid, col_info = st.columns([1.5, 1])
    
    with col_vid:
        st.video(p['video_url'])
    
    with col_info:
        st.markdown(f"<h2 class='project-header'>{p['title']}</h2>", unsafe_allow_html=True)
        st.write(p['desc'])
        
        # Action Buttons
        st.link_button("📄 Download Technical One-Pager", p['pdf_url'], use_container_width=True)
        st.caption("🔒 Source code available upon request (Proprietary/Medical IP)")

    st.divider()

# --- 4. FOOTER / CONTACT ---
st.sidebar.header("About the Developer")
st.sidebar.info("Focused on the intersection of AI Automation and Medical Device Safety.")
st.sidebar.write("📍 Based in Lahore, Pakistan")
