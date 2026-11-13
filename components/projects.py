
import base64
import streamlit as st

from html import escape
from pathlib import Path

from data.projects import PROJECTS


PROJECT_IMAGES_DIR = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "images"
    / "projects"
)


def get_image_base64(filename):
    """Load a local project image and encode it for HTML."""

    image_path = PROJECT_IMAGES_DIR / filename

    if not image_path.exists():
        return None

    extension = image_path.suffix.lower()
    mime_type = "image/png" if extension == ".png" else "image/jpeg"

    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


def render_project_card(project, t):
    """Build one project card."""

    images_html = ""

    for image_name in project.get("images", []):
        image_data = get_image_base64(image_name)

        if image_data:
            images_html += f"""
                <img
                    class="project-image"
                    src="{image_data}"
                    alt="{escape(project['title'])}"
                >
            """

    if images_html:
        visual_html = f"""
            <div class="project-visual">
                {images_html}
            </div>
        """
    else:
        visual_html = f"""
            <div class="project-visual project-visual-placeholder">
                <span class="project-placeholder-icon">
                    {"◈" if project["id"] == "mimicom" else "⌂"}
                </span>
                <span class="project-placeholder-label">
                    {escape(t["project_no_preview"])}
                </span>
            </div>
        """

    technologies_html = "".join(
        f'<span class="project-tag">{escape(tech)}</span>'
        for tech in project["technologies"]
    )

    links_html = ""

    for link in project.get("links", []):
        label = escape(t[link["label"]])
        url = escape(link["url"], quote=True)

        links_html += f"""
            <a
                class="project-link"
                href="{url}"
                target="_blank"
                rel="noopener noreferrer"
            >
                {label} <span>↗</span>
            </a>
        """

    collaboration_html = ""

    if project.get("collaboration"):
        collaboration_html = f"""
            <p class="project-collaboration">
                {escape(t["project_collaboration"])}
                <strong>{escape(project["collaboration"])}</strong>
            </p>
        """

    confidential_html = ""

    if project.get("confidential"):
        confidential_html = f"""
            <p class="project-confidential">
                {escape(t["project_confidential"])}
            </p>
        """

    return f"""
        <article class="project-card" id="project-{escape(project['id'])}">
            {visual_html}

            <div class="project-card-content">
                <p class="project-category">
                    {escape(t[project["category"]])}
                </p>

                <h3>{escape(project["title"])}</h3>

                <p class="project-description">
                    {escape(t[project["description"]])}
                </p>

                {collaboration_html}
                {confidential_html}

                <div class="project-tags">
                    {technologies_html}
                </div>

                <div class="project-links">
                    {links_html}
                </div>
            </div>
        </article>
    """


def render_projects(t):
    """Render the Projects section."""

    cards_html = "".join(
        render_project_card(project, t)
        for project in PROJECTS
    )

    projects_html = f"""
        <section id="projects" class="content-section projects-section">

            <div class="projects-heading">
                <p class="section-number">
                    {escape(t["projects_eyebrow"])}
                </p>

                <h2>{escape(t["projects_title"])}</h2>

                <p class="projects-intro">
                    {escape(t["projects_intro"])}
                </p>
            </div>

            <div class="projects-grid">
                {cards_html}
            </div>

        </section>
    """

    st.html(projects_html)
