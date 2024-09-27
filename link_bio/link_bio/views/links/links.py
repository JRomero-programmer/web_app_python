import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
import link_bio.constants as constants

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("LinkedIn", 
                    "Mi perfil personal de LinkedIN",
                    constants.LINKEDIN_URL),
        link_button("Devsecops-spain", 
                    "Mi perfil personal de Devsecops-spain",
                    constants.LINKEDIN_URL),
        link_button("YouTube", 
                    "Mi perfil personal de YouTube",
                    constants.LINKEDIN_URL),
        link_button("Courses", 
                    "Mi perfil personal de Courses",
                    constants.LINKEDIN_URL),
        title("Personal"),
        link_button("LinkedIn", 
                    "Mi perfil personal de LinkedIN",
                    constants.LINKEDIN_URL),
        link_button("Devsecops-spain", 
                    "Mi perfil personal de Devsecops-spain",
                    constants.LINKEDIN_URL),
        link_button("YouTube", 
                    "Mi perfil personal de YouTube",
                    constants.LINKEDIN_URL),
        link_button("Courses", 
                    "Mi perfil personal de Courses",
                    constants.LINKEDIN_URL),
        width="100%",
        spacing=Size.DEFAULT.value
    )