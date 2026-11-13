
import streamlit as st
import base64
from pathlib import Path


def render_hero(t):
    """Render the main introduction section."""

    image_path = (
        Path(__file__).resolve().parents[1]
        / "assets"
        / "images"
        / "profile.png"
    )

    image_base64 = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    profile_image = f"data:image/png;base64,{image_base64}"
    
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
            <div class="hero-image-glow"></div>
            <img
                src="{profile_image}"
                alt="Portrait de Thomas Constantin"
                class="hero-profile-image"
            >
        </div>

    </section>
    """

    st.html(hero_html)
