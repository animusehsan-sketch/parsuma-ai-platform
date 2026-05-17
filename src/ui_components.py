import streamlit as st
import plotly.graph_objects as go
from typing import Any, List, Dict

def apply_custom_css():
    """Apply an ultra-premium, modern AI SaaS styling to the Streamlit app."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;800&display=swap');
        
        :root {
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.5);
            --secondary: #8b5cf6;
            --secondary-glow: rgba(139, 92, 246, 0.4);
            --bg-dark: #0f172a;
            --card-bg: rgba(30, 41, 59, 0.6);
            --border: rgba(255, 255, 255, 0.12);
            --text-main: #f8fafc;
            --text-muted: #cbd5e1;
            --accent-glow: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
        }

        .stApp, [data-testid="stAppViewContainer"] {
            background: radial-gradient(ellipse at right 20%, rgba(139, 92, 246, 0.15) 0%, rgba(59, 130, 246, 0.1) 40%, #0f172a 80%) !important;
            background-color: #0f172a !important;
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
        }
        
        [data-testid="stHeader"] {
            background: transparent !important;
        }

        .block-container {
            padding-top: 5rem !important;
            padding-bottom: 5rem !important;
            padding-left: 5rem !important;
            padding-right: 5rem !important;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-top: 3rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }

        /* Sidebar Customization */
        [data-testid="stSidebar"] {
            background-color: rgba(15, 23, 42, 0.95);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3);
        }
        
        /* Typography */
        h1, h2, h3, .outfit {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            letter-spacing: -0.03em;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            line-height: 1.1;
        }
        
        .hero-subtitle {
            color: var(--text-muted);
            font-size: 1.25rem;
            font-weight: 400;
            margin-bottom: 3rem;
            max-width: 800px;
        }

        /* Premium Glass Card */
        .glass-card {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 24px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(16px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .glass-card:hover {
            border-color: rgba(139, 92, 246, 0.3);
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4), 0 0 40px rgba(139, 92, 246, 0.15);
            transform: translateY(-5px);
        }

        .metric-glass {
            background: rgba(30, 41, 59, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 0 0 30px rgba(139, 92, 246, 0.1);
        }
        
        .metric-glass:hover {
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4), 0 0 40px rgba(139, 92, 246, 0.25);
            border-color: rgba(139, 92, 246, 0.5);
        }

        /* Sidebar Branding */
        .sidebar-logo {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1rem;
        }
        
        .sidebar-subtitle {
            text-align: center;
            font-size: 0.8rem;
            color: #cbd5e1;
            font-weight: 500;
            letter-spacing: 0.02em;
            margin-bottom: 2rem;
        }

        .sidebar-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            margin: 1.5rem 0;
        }

        /* Radio Navigation */
        div[data-testid="stRadio"] div[role="radiogroup"] {
            gap: 0.5rem;
        }
        div[data-testid="stRadio"] label {
            background: rgba(255,255,255,0.02);
            border-radius: 12px;
            padding: 0.5rem 1rem;
            transition: all 0.2s;
            cursor: pointer;
        }
        div[data-testid="stRadio"] label:hover {
            background: rgba(255,255,255,0.08);
        }
        /* Custom highlight for active radio, trying to target checked without breaking Streamlit */
        div[data-testid="stRadio"] label[data-checked="true"], 
        div[data-testid="stRadio"] label:has(input:checked) {
            background: linear-gradient(135deg, rgba(59,130,246,0.3) 0%, rgba(139,92,246,0.3) 100%) !important;
            border-left: 4px solid #8b5cf6;
        }

        /* Pipeline Cards */
        .pipeline-card {
            padding: 2.5rem 1.5rem;
            background: rgba(30, 41, 59, 0.8);
            border-radius: 24px;
            backdrop-filter: blur(20px);
            position: relative;
            z-index: 2;
        }
        .pipeline-icon {
            width: 70px;
            height: 70px;
            margin: 0 auto 1.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
            border-radius: 50%;
            transition: all 0.3s ease;
        }
        .pipeline-card:hover .pipeline-icon {
            transform: scale(1.15);
        }
        .pipeline-title {
            font-weight: 800;
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            color: var(--text-main);
            letter-spacing: 0.05em;
            margin-bottom: 0.4rem;
        }
        .pipeline-subtitle {
            font-size: 0.85rem;
            color: var(--text-muted);
        }
        
        @media (max-width: 1024px) {
            .pipeline-grid { grid-template-columns: repeat(2, 1fr) !important; }
        }
        @media (max-width: 640px) {
            .pipeline-grid { grid-template-columns: 1fr !important; }
        }

        /* Metric Dashboard Cards */
        .metric-card {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        
        .metric-label {
            color: var(--text-muted);
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }
        
        .metric-value {
            font-size: 2.8rem;
            font-weight: 800;
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(90deg, #ffffff, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .metric-delta {
            font-size: 0.9rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        .delta-up { color: #10b981; }
        .delta-down { color: #ef4444; }

        /* Chat Bubbles - Premium */
        .chat-bubble {
            padding: 1.5rem;
            border-radius: 20px;
            margin-bottom: 1.5rem;
            font-size: 1rem;
            line-height: 1.6;
            max-width: 90%;
            position: relative;
            animation: fadeIn 0.5s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .user-bubble {
            background: rgba(99, 102, 241, 0.1);
            border: 1px solid rgba(99, 102, 241, 0.2);
            margin-left: auto;
            border-bottom-right-radius: 4px;
        }
        
        .assistant-bubble {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border);
            border-bottom-left-radius: 4px;
        }

        /* Buttons & Inputs */
        .stButton>button {
            width: 100%;
            background: var(--accent-glow);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-weight: 700;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px var(--primary-glow);
        }
        
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 20px var(--primary-glow);
            opacity: 0.9;
        }

        /* Source Chips */
        .source-chip {
            display: inline-block;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            padding: 4px 12px;
            border-radius: 99px;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--primary);
            margin-right: 8px;
            margin-top: 8px;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 10px; }
        
        /* Hide Streamlit components */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        </style>
    """, unsafe_allow_html=True)

def render_hero(title: str, subtitle: str):
    """Render the ultra-premium hero section."""
    title_html = title.replace("AI", "<span style='background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>AI</span>")
    
    st.markdown(f"""
        <div style='margin-top: 1rem; margin-bottom: 4rem; position: relative;'>
            <div style='position: absolute; top: -50px; left: -50px; width: 100%; height: 200%; background: radial-gradient(ellipse at top left, rgba(139, 92, 246, 0.15) 0%, transparent 70%); filter: blur(50px); z-index: -1; pointer-events: none;'></div>
            <div class='hero-title'>{title_html}</div>
            <div class='hero-subtitle'>{subtitle}</div>
        </div>
    """, unsafe_allow_html=True)

def render_metric_card(label: str, value: str, delta: str = None, is_up: bool = True, icon: str = "📊", icon_color: str = "#6366f1"):
    """Render a modern dashboard metric card with a colored circular badge."""
    delta_html = ""
    if delta:
        cls = "delta-up" if is_up else "delta-down"
        icon_delta = "↑" if is_up else "↓"
        if delta in ["Live", "Low"]:
            icon_delta = ""
        delta_html = f"<div class='metric-delta {cls}'>{icon_delta} {delta}</div>"
        
    st.markdown(f"""
        <div class='glass-card metric-glass'>
            <div class='metric-header' style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;'>
                <div class='metric-label'>{label}</div>
                <div style='background: {icon_color}20; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; border: 1px solid {icon_color}40; box-shadow: 0 0 15px {icon_color}30;'>
                    {icon}
                </div>
            </div>
            <div class='metric-card'>
                <div style='display: flex; align-items: baseline; gap: 12px;'>
                    <div class='metric-value'>{value}</div>
                    {delta_html}
                </div>
                <div style='font-size: 0.65rem; color: rgba(148, 163, 184, 0.5); margin-top: 12px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 8px;'>
                    Simulated demo metrics for academic evaluation
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_chat_bubble(role: str, content: str, sources: List[Dict] = None, confidence: float = None):
    """Render a premium chat bubble with source integration."""
    cls = "user-bubble" if role == "user" else "assistant-bubble"
    label = "YOU" if role == "user" else "PARSUMA AI"
    color = "#6366f1" if role == "user" else "#a855f7"
    
    source_html = ""
    if sources:
        source_html = "<div style='margin-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 0.75rem;'>"
        for s in sources:
            fname = s['metadata'].get('filename', 'Source')
            source_html += f"<span class='source-chip'>📄 {fname}</span>"
        source_html += "</div>"

    conf_html = ""
    if confidence:
        conf_html = f"<div style='font-size: 0.7rem; color: #94a3b8; margin-top: 4px;'>Confidence: {int(confidence*100)}%</div>"

    st.markdown(f"""
        <div class='chat-bubble {cls}'>
            <div style='font-size: 0.75rem; font-weight: 800; color: {color}; letter-spacing: 0.1em; margin-bottom: 0.5rem;'>{label}</div>
            <div style='color: #f1f5f9;'>{content}</div>
            {conf_html}
            {source_html}
        </div>
    """, unsafe_allow_html=True)

def create_gauge_plot(value: float, title: str):
    """Create a futuristic gauge using Plotly."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value * 100,
        number = {'suffix': "%", 'font': {'size': 40, 'color': '#fff', 'family': 'Outfit'}},
        title = {'text': title, 'font': {'size': 14, 'color': '#94a3b8', 'family': 'Inter'}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
            'bar': {'color': "#6366f1"},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.05)",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.05)'},
                {'range': [50, 100], 'color': 'rgba(16, 185, 129, 0.05)'}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': value * 100
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=220,
        margin=dict(l=30, r=30, t=50, b=10)
    )
    return fig

def render_footer():
    """Render a subtle professional footer."""
    st.markdown("""
        <div class='footer-container' style='text-align: center; padding: 3rem 2rem; color: rgba(148, 163, 184, 0.6); font-size: 0.85rem; letter-spacing: 0.05em;'>
            Built for Applied AI Engineering – Parsuma AI<br>
            <span style='opacity: 0.6;'>© 2026 Parsuma Knowledge Systems</span>
        </div>
    """, unsafe_allow_html=True)
