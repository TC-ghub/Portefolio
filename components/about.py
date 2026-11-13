
import streamlit as st
from html import escape


def render_about(t):
    """Render the About section."""

    about_html = f"""
    <section id="about" class="content-section about-section">

        <div class="about-grid">

            <div class="about-heading">

                <p class="section-number">
                    {escape(t["about_eyebrow"])}
                </p>

                <h2>
                    {escape(t["about_heading_1"])}<br>
                    <span class="about-highlight">
                        {escape(t["about_heading_2"])}
                    </span>
                </h2>

            </div>

            <div class="about-description">

                <p class="about-lead">
                    {escape(t["about_paragraph_1"])}
                </p>

                <p>
                    {escape(t["about_paragraph_2"])}
                </p>

            </div>

        </div>

        <div class="about-focus">

            <div class="focus-item">
                <span class="focus-number">01</span>
                <h3>{escape(t["about_focus_1"])}</h3>
                <p>{escape(t["about_focus_1_desc"])}</p>
            </div>

            <div class="focus-item">
                <span class="focus-number">02</span>
                <h3>{escape(t["about_focus_2"])}</h3>
                <p>{escape(t["about_focus_2_desc"])}</p>
            </div>

            <div class="focus-item">
                <span class="focus-number">03</span>
                <h3>{escape(t["about_focus_3"])}</h3>
                <p>{escape(t["about_focus_3_desc"])}</p>
            </div>

        </div>

    </section>
    """

    st.html(about_html)
