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
            --secondary: #a855f7;
            --secondary-glow: rgba(168, 85, 247, 0.4);
            --bg-dark: #020617;
            --card-bg: rgba(15, 23, 42, 0.6);
            --border: rgba(255, 255, 255, 0.08);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent-glow: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        }

        .stApp {
            background-color: #020617;
            background-image: 
                radial-gradient(circle at 90% 20%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 95% 80%, rgba(168, 85, 247, 0.08) 0%, transparent 45%),
                linear-gradient(to right, transparent 40%, rgba(15, 23, 42, 0.4) 100%);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
        }

        /* Adjust main container padding for cloud deployment */
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
            background-color: rgba(2, 6, 23, 0.98);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            box-shadow: 4px 0 24px rgba(0, 0, 0, 0.4);
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
            background: linear-gradient(135deg, #fff 0%, #94a3b8 100%);
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
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(16px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 0 0 20px rgba(99, 102, 241, 0.03), 0 0 30px rgba(168, 85, 247, 0.02);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .glass-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 0 30px rgba(99, 102, 241, 0.15), 0 0 10px rgba(168, 85, 247, 0.1);
            transform: translateY(-5px);
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
            font-size: 0.75rem;
            color: var(--text-muted);
            font-weight: 500;
            letter-spacing: 0.05em;
            margin-bottom: 2rem;
        }

        .sidebar-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--border), transparent);
            margin: 1.5rem 0;
        }

        /* Footer */
        .footer-container {
            text-align: center;
            padding: 4rem 2rem 2rem;
            color: var(--text-muted);
            font-size: 0.8rem;
            letter-spacing: 0.05em;
        }

        /* Metric Dashboard Cards */
        .metric-card {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .metric-label {
            color: var(--text-muted);
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        
        .metric-value {
            font-size: 2.5rem;
            font-weight: 800;
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(90deg, #fff, #94a3b8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .metric-delta {
            font-size: 0.875rem;
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
    st.markdown(f"""
        <div style='margin-top: 1rem; margin-bottom: 4rem;'>
            <div class='hero-title'>{title}</div>
            <div class='hero-subtitle'>{subtitle}</div>
        </div>
    """, unsafe_allow_html=True)

def render_metric_card(label: str, value: str, delta: str = None, is_up: bool = True):
    """Render a modern dashboard metric card."""
    delta_html = ""
    if delta:
        cls = "delta-up" if is_up else "delta-down"
        icon = "↑" if is_up else "↓"
        delta_html = f"<div class='metric-delta {cls}'>{icon} {delta}</div>"
        
    st.markdown(f"""
        <div class='glass-card'>
            <div class='metric-card'>
                <div class='metric-label'>{label}</div>
                <div class='metric-value'>{value}</div>
                {delta_html}
                <div style='font-size: 0.6rem; color: rgba(148, 163, 184, 0.4); margin-top: 12px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 8px;'>
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
        <div class='footer-container'>
            Built for Applied AI Engineering – Parsuma AI<br>
            <span style='opacity: 0.6;'>© 2026 Parsuma Knowledge Systems</span>
        </div>
    """, unsafe_allow_html=True)
