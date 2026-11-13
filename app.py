
from pathlib import Path
from textwrap import dedent
from data.translations import TRANSLATIONS
from components.skills import render_skills
from components.about import render_about
from components.navbar import render_header
from components.hero import render_hero
from components.projects import render_projects
from components.contact import render_contact
import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Portfolio Thomas CONSTANTIN | Data Analyst & Python Developer",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).parent
CSS_PATH = BASE_DIR / "assets" / "css" / "style.css"



# ============================================================
# SESSION STATE
# ============================================================

if "language" not in st.session_state:
    st.session_state.language = "FR"

lang = st.session_state.language
t = TRANSLATIONS[lang]


# ============================================================
# CSS LOADER
# ============================================================

def load_css():
    """Load the global CSS stylesheet."""
    if CSS_PATH.exists():
        css = CSS_PATH.read_text(encoding="utf-8")
        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True,
        )


load_css()


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():



    t = TRANSLATIONS[st.session_state.language]
    
    render_header(t)
    
    render_hero(t)
    st.divider()

    render_about(t)
    st.divider()
    render_skills(t)
    st.divider()

    render_projects(t)
    st.divider()

    render_contact(t)


if __name__ == "__main__":
    main()
