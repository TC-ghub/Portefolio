
import streamlit as st


def render_header(t):
    """Render the portfolio header and navigation."""

    left, right = st.columns(
        [5, 2],
        vertical_alignment="center"
    )

    with left:
        st.markdown(
            """
            <div class="brand">
                <span class="brand-symbol">[ DA. ]</span>
                <span class="brand-subtitle">
                    DATA ANALYSIS · PYTHON DEVELOPMENT
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.radio(
            "Language",
            options=["FR", "EN"],
            horizontal=True,
            label_visibility="collapsed",
            key="language",
        )

    st.markdown(
        f"""
        <nav class="navigation">
            <a href="#about">{t["nav_about"]}</a>
            <a href="#skills">{t["nav_skills"]}</a>
            <a href="#projects">{t["nav_projects"]}</a>
            <a href="#contact">{t["nav_contact"]}</a>
        </nav>

        <div class="header-divider"></div>
        """,
        unsafe_allow_html=True,
    )
