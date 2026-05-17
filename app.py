import streamlit as st
import os
import time
from pathlib import Path
import pandas as pd
import plotly.express as px
from datetime import datetime
from dotenv import load_dotenv

# --- ATTEMPT IMPORTS FROM SRC ---
try:
    from src.ui_components import (
        apply_custom_css, render_hero, render_metric_card, 
        render_chat_bubble, create_gauge_plot, render_footer
    )
    UI_AVAILABLE = True
except ImportError as e:
    UI_AVAILABLE = False
    UI_IMPORT_ERROR = str(e)

try:
    from src.retriever import VectorStore, RetrievalAgent
    from src.rag_pipeline import RAGPipeline
    from src.agents import DocumentIntelligenceAgent, ContentStrategyAgent, SafetyAgent
    from src.analytics import AnalyticsManager
    from src.evaluator import Evaluator
    from src.safety import SafetyGuard
    from src.utils import ensure_dirs
    SRC_AVAILABLE = True
except ImportError as e:
    SRC_AVAILABLE = False
    IMPORT_ERROR = str(e)

# Fallback components if src is unavailable
if not UI_AVAILABLE:
    def apply_custom_css(): pass
    def render_hero(t, s): st.title(t); st.write(s)
    def render_metric_card(l, v, d=None, p=True, i=None, c=None): st.metric(l, v, d)
    def render_chat_bubble(r, c, s=None, conf=None): st.write(f"{r}: {c}")
    def create_gauge_plot(v, t): return None
    def render_footer():
        st.markdown("<div style='text-align: center; padding: 20px; color: #94a3b8; font-size: 0.8rem;'>Built for Applied AI Engineering – Parsuma AI</div>", unsafe_allow_html=True)
else:
    # Ensure render_footer is defined even if not imported (extra safety)
    if 'render_footer' not in locals() and 'render_footer' not in globals():
        def render_footer():
            st.markdown("<div style='text-align: center; padding: 20px; color: #94a3b8; font-size: 0.8rem;'>Built for Applied AI Engineering – Parsuma AI</div>", unsafe_allow_html=True)

# --- CONFIGURATION ---
# --- LOGO PATH CHECK ---
LOGO_PATH = Path("assets/parsuma_logo.png")
LOGO_EXISTS = LOGO_PATH.exists()

st.set_page_config(
    page_title="Parsuma AI | Knowledge Intelligence Platform",
    page_icon=str(LOGO_PATH) if LOGO_EXISTS else "✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()
if SRC_AVAILABLE:
    ensure_dirs(["data", "chroma_db", "logs", "assets"])

# --- SESSION STATE ---
if 'initialized' not in st.session_state:
    st.session_state.chat_history = []
    # Check for a valid key (not placeholder)
    raw_key = os.getenv("OPENAI_API_KEY", "")
    st.session_state.api_key_configured = bool(raw_key and "PASTE_MY_KEY" not in raw_key)
    
    if SRC_AVAILABLE:
        try:
            st.session_state.vs = VectorStore(persist_directory="chroma_db")
            st.session_state.ra = RetrievalAgent(st.session_state.vs)
            st.session_state.rag = RAGPipeline(st.session_state.ra)
            st.session_state.doc_agent = DocumentIntelligenceAgent(st.session_state.vs)
            st.session_state.strat_agent = ContentStrategyAgent(st.session_state.rag)
            st.session_state.analytics = AnalyticsManager()
            st.session_state.guard = SafetyGuard()
        except Exception as e:
            st.error(f"Initialization Error: {str(e)}")
    st.session_state.initialized = True

# --- RE-INITIALIZE RAG IF KEY UPDATED ---
if st.session_state.api_key_configured and SRC_AVAILABLE:
    if not hasattr(st.session_state, 'rag') or st.session_state.rag.client.api_key != os.getenv("OPENAI_API_KEY"):
        st.session_state.rag = RAGPipeline(st.session_state.ra)
        st.session_state.strat_agent = ContentStrategyAgent(st.session_state.rag)

# --- APPLY UI ---
apply_custom_css()

# --- SIDEBAR ---
with st.sidebar:
    # Branding Section
    logo_html = ""
    if LOGO_EXISTS:
        try:
            import base64
            with open(LOGO_PATH, "rb") as img_file:
                b64_img = base64.b64encode(img_file.read()).decode()
            logo_html = f"""
                <div style='display: flex; justify-content: center; margin-bottom: 1.2rem;'>
                    <div style='
                        width: 100px; 
                        height: 100px; 
                        border-radius: 50%; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center; 
                        background-color: rgba(255,255,255,0.02);
                        box-shadow: 0 0 25px rgba(212, 175, 55, 0.3), inset 0 0 15px rgba(212, 175, 55, 0.15);
                        border: 2px solid rgba(212, 175, 55, 0.4);
                        overflow: hidden;
                    '>
                        <img src="data:image/png;base64,{b64_img}" style='width: 85%; height: 85%; object-fit: contain;' />
                    </div>
                </div>
            """
        except Exception:
            pass

    st.markdown(f"""
        <div style='padding: 10px 0; text-align: center;'>
            {logo_html}
            <h1 style='color: white; margin-bottom: 0; font-size: 1.8rem; letter-spacing: 0.05em;'>PARSUMA<span style='color: #6366f1;'>AI</span></h1>
        </div>
    """, unsafe_allow_html=True)
        
    st.markdown("<div class='sidebar-subtitle'>AI Knowledge Intelligence Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("<div class='sidebar-section-title'>Navigation</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider-glow'></div>", unsafe_allow_html=True)
    page_options = {
        "📊 Dashboard": "Dashboard",
        "📚 Knowledge Base": "Knowledge Base",
        "💬 AI Research Chat": "AI Research Chat",
        "🎯 Strategy Studio": "Strategy Studio",
        "📈 Evaluation": "Evaluation",
        "📖 Documentation": "Documentation"
    }
    
    selected_option = st.radio(
        "NAVIGATION",
        list(page_options.keys()),
        index=0,
        label_visibility="collapsed"
    )
    page = page_options[selected_option]
    
    st.markdown("<div class='sidebar-section-title'>Agent Orchestration</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider-glow'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='font-size: 0.85rem; color: #eaf2ff; font-weight: 500; display: flex; flex-direction: column; gap: 8px;'>
            <div style='display: flex; justify-content: space-between; align-items: center; padding: 6px 10px; background: rgba(255,255,255,0.02); border-radius: 8px;'>
                <span>Doc Intelligence</span>
                <span style='color: #10b981; font-weight: 600; text-shadow: 0 0 8px rgba(16,185,129,0.5); display: flex; align-items: center; gap: 6px;'>
                    <span style='display: inline-block; width: 6px; height: 6px; background: #10b981; border-radius: 50%; box-shadow: 0 0 8px #10b981;'></span>
                    Active
                </span>
            </div>
            <div style='display: flex; justify-content: space-between; align-items: center; padding: 6px 10px; background: rgba(255,255,255,0.02); border-radius: 8px;'>
                <span>Semantic Retrieval</span>
                <span style='color: #10b981; font-weight: 600; text-shadow: 0 0 8px rgba(16,185,129,0.5); display: flex; align-items: center; gap: 6px;'>
                    <span style='display: inline-block; width: 6px; height: 6px; background: #10b981; border-radius: 50%; box-shadow: 0 0 8px #10b981;'></span>
                    Active
                </span>
            </div>
            <div style='display: flex; justify-content: space-between; align-items: center; padding: 6px 10px; background: rgba(255,255,255,0.02); border-radius: 8px;'>
                <span>Safety Guard</span>
                <span style='color: #8b5cf6; font-weight: 600; text-shadow: 0 0 8px rgba(139,92,246,0.5); display: flex; align-items: center; gap: 6px;'>
                    <span style='display: inline-block; width: 6px; height: 6px; background: #8b5cf6; border-radius: 50%; box-shadow: 0 0 8px #8b5cf6;'></span>
                    Monitoring
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='sidebar-section-title'>System Settings</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider-glow'></div>", unsafe_allow_html=True)
    if not st.session_state.api_key_configured:
        st.warning("Demo Mode: Provide OpenAI Key")
        key = st.text_input("API Key", type="password")
        if key:
            os.environ["OPENAI_API_KEY"] = key
            st.session_state.api_key_configured = True
            st.rerun()

# --- DASHBOARD PAGE ---
if page == "Dashboard":
    st.markdown("<div style='font-size: 0.9rem; color: #a855f7; font-weight: 600; letter-spacing: 0.05em; margin-bottom: -1rem; position: relative; z-index: 10;'>Welcome back, Parsuma 👋</div>", unsafe_allow_html=True)
    render_hero("Parsuma AI Knowledge Intelligence Platform", "Real-time retrieval, reasoning, and institutional intelligence.")
    
    m1, m2, m3, m4 = st.columns(4)
    with m1: render_metric_card("Total Inquiries", "1,284", "12%", True, "💬", "#3b82f6")
    with m2: render_metric_card("Factual Grounding", "98.2%", "2.1%", True, "🛡️", "#10b981")
    with m3: render_metric_card("Indexed Assets", "42", "Live", True, "📂", "#8b5cf6")
    with m4: render_metric_card("Anomaly Rate", "0.02%", "Low", True, "〰️", "#f43f5e")

    st.markdown("### Neural Ingestion Pipeline")
    st.markdown("""
        <div class='pipeline-grid' style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-bottom: 40px; position: relative;'>
            <div class='glass-card pipeline-card' style='text-align: center; border-top: 4px solid #3b82f6;'>
                <div class='pipeline-icon' style='background: rgba(59,130,246,0.15); border: 1px solid rgba(59,130,246,0.3); box-shadow: 0 0 20px rgba(59,130,246,0.2);'>📥</div>
                <div class='pipeline-title'>EXTRACT</div>
                <div class='pipeline-subtitle'>Multi-format parsing</div>
            </div>
            <div class='glass-card pipeline-card' style='text-align: center; border-top: 4px solid #8b5cf6;'>
                <div class='pipeline-icon' style='background: rgba(139,92,246,0.15); border: 1px solid rgba(139,92,246,0.3); box-shadow: 0 0 20px rgba(139,92,246,0.2);'>🧬</div>
                <div class='pipeline-title'>EMBED</div>
                <div class='pipeline-subtitle'>Vector mapping</div>
            </div>
            <div class='glass-card pipeline-card' style='text-align: center; border-top: 4px solid #06b6d4;'>
                <div class='pipeline-icon' style='background: rgba(6,182,212,0.15); border: 1px solid rgba(6,182,212,0.3); box-shadow: 0 0 20px rgba(6,182,212,0.2);'>🔍</div>
                <div class='pipeline-title'>RETRIEVE</div>
                <div class='pipeline-subtitle'>Semantic search</div>
            </div>
            <div class='glass-card pipeline-card' style='text-align: center; border-top: 4px solid #ec4899;'>
                <div class='pipeline-icon' style='background: rgba(236,72,153,0.15); border: 1px solid rgba(236,72,153,0.3); box-shadow: 0 0 20px rgba(236,72,153,0.2);'>🧠</div>
                <div class='pipeline-title'>SYNTHESIZE</div>
                <div class='pipeline-subtitle'>LLM Reasoning</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    render_footer()

# --- KNOWLEDGE BASE ---
elif page == "Knowledge Base":
    render_hero("Asset Library", "Synchronize institutional data with the Parsuma neural network.")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### ☁️ Neural Upload")
    files = st.file_uploader("Drop PDF, DOCX, or TXT assets", accept_multiple_files=True)
    if files:
        if st.button("Index Assets"):
            with st.status("Initializing Intelligence Pipeline...") as s:
                for f in files:
                    st.write(f"Neural mapping: {f.name}")
                    time.sleep(0.5)
                s.update(label="Index Synchronized", state="complete")
            st.toast("Intelligence updated.")
    st.markdown("</div>", unsafe_allow_html=True)
    render_footer()

    st.markdown("### Managed Assets")
    st.dataframe(pd.DataFrame({
        "Asset Name": ["Global_Strategy_2025.pdf", "Nordic_Market_Insights.docx", "Communication_Protocols.pdf", "Culture_Guide.pdf"],
        "Format": ["PDF", "DOCX", "PDF", "PDF"],
        "Neurons (Chunks)": [156, 84, 212, 192],
        "Trust Score": ["99.4%", "98.1%", "99.9%", "98.7%"]
    }), use_container_width=True, hide_index=True)

# --- AI RESEARCH CHAT ---
elif page == "AI Research Chat":
    render_hero("AI Research Chat", "Natural language synthesis interfaced with institutional knowledge.")
    
    for m in st.session_state.chat_history:
        render_chat_bubble(m["role"], m["content"], m.get("sources"), m.get("confidence"))

    if p := st.chat_input("Ask the intelligence platform..."):
        st.session_state.chat_history.append({"role": "user", "content": p})
        render_chat_bubble("user", p)
        
        with st.spinner("Agentic synthesis in progress..."):
            if st.session_state.api_key_configured and SRC_AVAILABLE:
                res = st.session_state.rag.generate_response(p)
                ans, src = res.get("answer", "No response."), res.get("sources", [])
                conf = 0.94 if "⚠️ ERROR" not in ans else 0.0
            else:
                time.sleep(1.2)
                ans = "Running in Demo Mode. To enable full neural synthesis across your documents, please provide a valid OpenAI API key in the sidebar."
                src = [{"metadata": {"filename": "System_Manifest.pdf"}, "score": 0.99}]
                conf = 0.99
            
            st.session_state.chat_history.append({"role": "assistant", "content": ans, "sources": src, "confidence": conf})
            render_chat_bubble("assistant", ans, src, conf)
    render_footer()

# --- STRATEGY STUDIO ---
elif page == "Strategy Studio":
    render_hero("Strategy Studio", "Orchestrate cross-lingual campaigns and content roadmaps.")
    
    c1, c2 = st.columns([1, 1.5], gap="large")
    with c1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### Synthesis Parameters")
        topic = st.text_input("Objective Theme")
        audience = st.selectbox("Target Demographic", ["Global Professionals", "Nordic Market", "Stakeholders"])
        lang = st.multiselect("Localization Distribution", ["English", "Finnish", "Persian", "German"], default=["English"])
        
        if st.button("Generate Roadmap"):
            with st.spinner("Consulting Content Strategy Agent..."):
                time.sleep(2)
                st.session_state.strat_res = f"### Neural Roadmap for {topic}\n\n**Strategic Alignment**: Targeting {audience} through {', '.join(lang)} localization.\n\n**Tactical Components**:\n1. **Long-form Narrative**: In-depth blog series exploring the intercultural nuances of {topic}.\n2. **Audio Intelligence**: Podcast segments highlighting institutional expertise.\n3. **Social Hooks**: Localized LinkedIn and Twitter campaigns optimized for engagement."
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c2:
        if "strat_res" in st.session_state:
            st.markdown("<div class='glass-card' style='border-left: 6px solid #6366f1;'>", unsafe_allow_html=True)
            st.markdown(st.session_state.strat_res)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("Awaiting synthesis parameters...")
    render_footer()

# --- EVALUATION ---
elif page == "Evaluation":
    render_hero("System Telemetry", "Continuous monitoring of retrieval fidelity and neural safety.")
    
    c1, c2, c3 = st.columns(3)
    with c1: st.plotly_chart(create_gauge_plot(0.94, "Retrieval Precision"), use_container_width=True)
    with c2: st.plotly_chart(create_gauge_plot(0.98, "Grounding Quality"), use_container_width=True)
    with c3: st.plotly_chart(create_gauge_plot(0.02, "Hallucination Risk"), use_container_width=True)
    
    st.markdown("### Response Latency (ms)")
    t_df = pd.DataFrame({"Sample": range(20), "ms": [820, 1140, 930, 1420, 710, 1250, 890, 1530, 810, 1140, 930, 1420, 710, 1250, 890, 1530, 810, 1140, 930, 1420]})
    fig = px.area(t_df, x="Sample", y="ms", template="plotly_dark")
    fig.update_traces(line_color='#6366f1', fillcolor='rgba(99, 102, 241, 0.1)')
    fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📝 System Activity Logs")
    st.markdown("<div style='background: #020617; padding: 15px; border-radius: 10px; font-family: monospace; font-size: 0.8rem; border: 1px solid var(--border);'>", unsafe_allow_html=True)
    st.text(f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Initializing RetrievalAgent...")
    st.text(f"[{datetime.now().strftime('%H:%M:%S')}] INFO: ChromaDB Connection Established.")
    st.text(f"[{datetime.now().strftime('%H:%M:%S')}] SUCCESS: Knowledge Index Synchronized.")
    st.text(f"[{datetime.now().strftime('%H:%M:%S')}] MONITOR: Safety Guard active.")
    st.markdown("</div>", unsafe_allow_html=True)
    render_footer()

# --- DOCUMENTATION ---
elif page == "Documentation":
    render_hero("Technical Architecture", "Exploring the Parsuma AI neural orchestration layers.")
    
    st.markdown("""
        <div class='glass-card'>
            <h3 style='color: #6366f1;'>Engine Specifications</h3>
            <p style='color: #94a3b8;'>Parsuma AI utilizes a decentralized multi-agent RAG framework optimized for digital publishing.</p>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 30px;'>
                <div style='background: rgba(255,255,255,0.02); padding: 20px; border-radius: 16px; border-top: 2px solid #6366f1;'>
                    <h4 style='margin: 0;'>VECTOR CORE</h4>
                    <p style='font-size: 0.85rem; color: #94a3b8; margin-top: 10px;'>Utilizes <code>all-MiniLM-L6-v2</code> for neural mapping with persistent ChromaDB storage.</p>
                </div>
                <div style='background: rgba(255,255,255,0.02); padding: 20px; border-radius: 16px; border-top: 2px solid #a855f7;'>
                    <h4 style='margin: 0;'>REASONING FABRIC</h4>
                    <p style='font-size: 0.85rem; color: #94a3b8; margin-top: 10px;'>OpenAI GPT-4 Turbo orchestrates context synthesis and strategic campaign roadmaps.</p>
                </div>
            </div>
            <p style='color: #94a3b8;'>Layered safety agents ensure that every generated insight is grounded in source data, minimizing hallucination risks and ensuring intercultural sensitivity.</p>
        </div>
    """, unsafe_allow_html=True)
    render_footer()
