
import streamlit as st
from html import escape


def render_skills(t):
    """Render the Technical Skills section."""

    skill_categories = [
        {
            "number": "01",
            "icon": "</>",
            "title": t["skills_programming"],
            "description": {
                "FR": "Programmation et manipulation des données.",
                "EN": "Programming and data manipulation.",
            },
            "technologies": [
                "Python",
                "Pandas",
                "NumPy",
                "Regex",
            ],
        },
        {
            "number": "02",
            "icon": "◫",
            "title": t["skills_analysis"],
            "description": {
                "FR": "Exploration, analyse et visualisation.",
                "EN": "Data exploration, analysis and visualization.",
            },
            "technologies": [
                "Seaborn",
                "Plotly",
                "DuckDB",
                "Power BI",
            ],
        },
        {
            "number": "03",
            "icon": "⌘",
            "title": t["skills_development"],
            "description": {
                "FR": "Applications, API et infrastructure.",
                "EN": "Applications, APIs and infrastructure.",
            },
            "technologies": [
                "Streamlit",
                "FastAPI",
                "Docker",
                "MongoDB",
            ],
        },
        {
            "number": "04",
            "icon": "✳",
            "title": t["skills_ml"],
            "description": {
                "FR": "Apprentissage automatique et traitement du langage.",
                "EN": "Machine learning and natural language processing.",
            },
            "technologies": [
                "Scikit-learn",
                "NLP",
                "TF-IDF",
            ],
        },
    ]

    language = st.session_state.language

    cards_html = ""

    for category in skill_categories:

        technologies_html = "".join(
            f'<span class="skill-tag">{escape(tech)}</span>'
            for tech in category["technologies"]
        )

        cards_html += f"""
        <article class="skill-card">

            <div class="skill-card-header">

                <span class="skill-icon">
                    {escape(category["icon"])}
                </span>

                <span class="skill-number">
                    {category["number"]}
                </span>

            </div>

            <h3>{escape(category["title"])}</h3>

            <p class="skill-description">
                {escape(category["description"][language])}
            </p>

            <div class="skill-tags">
                {technologies_html}
            </div>

        </article>
        """

    skills_html = f"""
    <section id="skills" class="content-section skills-section">

        <div class="skills-heading">

            <p class="section-number">
                {escape(t["skills_eyebrow"])}
            </p>

            <h2>{escape(t["skills_title"])}</h2>

        </div>

        <div class="skills-grid">
            {cards_html}
        </div>

    </section>
    """

    st.html(skills_html)
