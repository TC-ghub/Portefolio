
import streamlit as st
from html import escape


def render_contact(t):
    """Render the Contact section."""

    # Replace with your Gmail address
    email = "YOUR_EMAIL@gmail.com"

    contact_html = f"""
    <section id="contact" class="content-section contact-section">

        <div class="contact-content">
            <p class="section-number">{escape(t["contact_eyebrow"])}</p>

            <h2>
                {escape(t["contact_title"])}
            </h2>

            <p class="contact-description">
                {escape(t["contact_description"])}
            </p>

            
            <div class="contact-links">

                <a class="contact-link"
                href="mailto:{escape("thoms.constantin@gmail.com", quote=True)}">
                    <span class="contact-link-icon">✉</span>
                    <span>{escape(t["contact_email"])}</span>
                    <span class="contact-link-arrow">↗</span>
                </a>

                <a class="contact-link"
                href="https://mail.google.com/mail/?view=cm&fs=1&to={escape("thoms.constantin@gmail.com", quote=True)}"
                target="_blank"
                rel="noopener noreferrer">
                    <span class="contact-link-icon">G</span>
                    <span>{escape(t["contact_gmail"])}</span>
                    <span class="contact-link-arrow">↗</span>
                </a>

                <a class="contact-link"
                href="https://www.linkedin.com/in/thomas-constantin-50189b97/"
                target="_blank"
                rel="noopener noreferrer">
                    <span class="contact-link-icon">in</span>
                    <span>LinkedIn</span>
                    <span class="contact-link-arrow">↗</span>
                </a>

                <a class="contact-link"
                href="https://github.com/TC-ghub"
                target="_blank"
                rel="noopener noreferrer">
                    <span class="contact-link-icon">⌘</span>
                    <span>GitHub</span>
                    <span class="contact-link-arrow">↗</span>
                </a>

            </div>

        </div>

        <div class="contact-footer">
            <span>Data Analyst & Python Developer</span>
            <span>© 2026</span>
        </div>

    </section>
    """

    st.html(contact_html)
