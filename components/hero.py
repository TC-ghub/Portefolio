
import streamlit as st


def render_hero(t):
    """Render the main introduction section."""

    hero_html = f"""
    <section class="hero">

        <div class="hero-content">

            <p class="hero-eyebrow">
                {t["hero_greeting"]}
            </p>

            <h1>
                Data Analyst <span class="hero-amp">&</span><br>
                <span class="hero-highlight">Python Developer.</span>
            </h1>

            <p class="hero-description">
                {t["hero_description"]}
            </p>

            <div class="hero-actions">
                <a class="primary-button" href="#projects">
                    {t["hero_projects"]}
                </a>

                <a class="secondary-button" href="#contact">
                    {t["hero_contact"]}
                </a>
            </div>

        </div>

        <div class="hero-visual">
            <div class="mini-chart">

                <div class="chart-label">DATA OVERVIEW</div>

                <div class="chart-area">
                    <div class="chart-grid">
                        <span></span>
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>

                    <div class="chart-bars">
                        <div class="chart-bar" style="--height: 32%"></div>
                        <div class="chart-bar" style="--height: 48%"></div>
                        <div class="chart-bar" style="--height: 40%"></div>
                        <div class="chart-bar" style="--height: 72%"></div>
                        <div class="chart-bar" style="--height: 62%"></div>
                        <div class="chart-bar active" style="--height: 88%"></div>
                    </div>
                </div>

                <div class="chart-footer">
                    <span>ANALYSIS</span>
                    <span>INSIGHTS</span>
                    <span>RESULTS</span>
                </div>

            </div>
        </div>

    </section>
    """

    st.html(hero_html)
