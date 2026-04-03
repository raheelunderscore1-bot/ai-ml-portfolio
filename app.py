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

st.title("Strategic AI & ML Portfolio")
st.subheader("Bridging Multi-modal AI with Real-World Engineering")
st.divider()

# --- THE DATA: YouTube Integrated Gallery ---
projects = [
    {
        "title": "🩸 AI Dialysis Monitoring Dashboard",
        "desc": "Predictive IoT monitoring for Home Based Dialysis using Gemini for tube/effluent analysis.",
        "video_url": "https://youtu.be/3wQp4kaYsLY",  # Web Demo
        "mobile_url": "https://youtube.com/shorts/xIXFXgAVYgo", # Mobile Demo
        "pdf_url": "https://drive.google.com/uc?export=download&id=1XbSi1FgqxCDw6dVDAx1_i7EyN0fyFfJy"
    },
    {
        "title": "⚡ Smart Grid Renforcement Learning Agent Dashboard",
        "desc": "Reinforcement Learning agent for real-time load balancing and grid operational stability.",
        "video_url": "https://youtu.be/lmHrAaCyPMI",
        "mobile_url": "https://youtube.com/shorts/eVePrmvHsg4",
        "pdf_url": "https://drive.google.com/uc?export=download&id=1z5rtlmHFogwD1brJDScsY-H64GMYC4zS"
    },
    {
        "title": "🚦 AI Traffic Intelligence Dashboard",
        "desc": "Neural-network driven traffic flow optimization with multi-platform monitoring.",
        "video_url": "https://youtu.be/t5YxLzRqIwc",
        "mobile_url": "https://youtube.com/shorts/2LqqTSjDyLo",
        "pdf_url": "https://drive.google.com/uc?export=download&id=1shMA0Pw2pAwxQMcLDJq8AgTEQqIjAXSl"
    },
    {
        "title": "👁️ Image Detector Bot (Engineering)",
        "desc": "Automated R&D documentation agent for hardware component identification and logging.",
        "video_url": "https://youtu.be/XbMW9z8iKRI",
        "mobile_url": None,
        "pdf_url": "https://drive.google.com/uc?export=download&id=1Uyto7uLO2JF8mOrO7Urtk1NReQe0f-XP"
    },
    {
        "title": "🍕 Restaurant Conversational Agent",
        "desc": "AI-powered chatbot handling complex ordering logic and dietary constraints.",
        "video_url": "https://youtu.be/IIun1jKb3eU",
        "mobile_url": "https://youtube.com/shorts/ITjbL6MNqP4",
        "pdf_url": "https://drive.google.com/uc?export=download&id=1O23KgGMIfyn6Itl-32DH_KA1DvXdcmTB"
    },
    {
        "title": "🌤️ Weather Companion Chatbot",
        "desc": "Agentic AI using function calling to provide real-time weather strategy and advice.",
        "video_url": "https://youtu.be/YsQFedWlBkM",
        "mobile_url": "https://youtube.com/shorts/_64TdTpEP3M",
        "pdf_url": "https://drive.google.com/uc?export=download&id=1y3gT1ITCXHhdHxfJ96eWjQu9jRQhWZFS"
    },
    {
        "title": "💳 AI based Customer Buying Behavior Profiling",
        "desc": "ML pipeline for segmenting credit card users into actionable behavioral profiles.",
        "video_url": "https://youtu.be/v9JjRRtWukw",
        "mobile_url": None,
         "pdf_url": "https://drive.google.com/uc?export=download&id=16f-Q3CZrPEZMUu4miIQWUNEBZuCNKpv3"
    },
    {
        "title": "🐈 Cat-Dog Image Classifier",
        "desc": "Neural Network model deployment via GitHub + Google Drive for pet detection.",
        "video_url": "https://youtu.be/8t-CMmsrmUA",
        "mobile_url": None,
        "pdf_url": "https://drive.google.com/uc?export=download&id=1v8H_XSZZbcC17XfhkRMKfoYv2x_kJmJf"
    },
    {
        "title": "🤖 GPT-Like Chatbot",
        "desc": "Full-stack LLM assistant implementation using the Gemini API.",
        "video_url": "https://youtu.be/gvDqwheu94Q",
        "mobile_url": None,
        "pdf_url": "https://drive.google.com/uc?export=download&id=1Q1SOiHH7aYRmp48ECeYflk4yqrVSIkZr"
    }
]

# --- THE FINAL CONSOLIDATED RENDERER ---
for p in projects:
    # 1. Create the Split: Video on Left (1.5), Info/Button on Right (1)
    col_vid, col_info = st.columns([1.5, 1])
    
    with col_vid:
        # Main Web Demo
        st.video(p['video_url'])
        
        # Add a sub-column for the Mobile/Shorts demo if it exists
        if p.get('mobile_url'):
            with st.expander("📱 View Mobile Interface Demo"):
                st.video(p['mobile_url'])
    
    with col_info:
        # 2. Project Title and Description
        st.markdown(f"<h2 class='project-header'>{p['title']}</h2>", unsafe_allow_html=True)
        st.write(p['desc'])
        
        # 3. Action Buttons
        if p.get('pdf_url'):
            st.link_button("📄 Download Technical One-Pager", p['pdf_url'], use_container_width=True)
        
        # 4. Badges and Disclaimers
        if p.get('mobile_url'):
            st.success("✅ Mobile & Web Optimized")
            
        st.caption("🔒 Source code available upon request (Proprietary/Medical IP)")

    # 5. Clean Divider between projects
    st.divider()

# --- 4. FOOTER / CONTACT ---
st.sidebar.header("About the Developer - (Raheel)")
st.sidebar.info("Focused on the intersection of AI, ML & Automation.")
st.sidebar.write("visionary313@gmail.com")
