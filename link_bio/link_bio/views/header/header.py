import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.components.info_text import info_text
from link_bio.styles.colors import TextColor as TextColor
import link_bio.constants as constants
import datetime

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JR", size="7"),
            rx.vstack(
                rx.box(
                    rx.heading(
                        "Jonatan Romero", 
                        size="6",
                        color=TextColor.HEADER.value
                    ),
                    rx.text(
                        "@devsecops-spain",
                        color=TextColor.BODY.value
                    ),
                    spacing="0"
                ),
                rx.hstack(
                    link_icon(constants.LINKEDIN_URL),
                    link_icon(constants.LINKEDIN_URL),
                    link_icon(constants.LINKEDIN_URL)
                ),
                width="100%"
            ),
            align="center",
            spacing=Size.BIG.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+",
                "años de experiencia"
            ),
            rx.spacer(),
            info_text(
                "+10",  
                "certificaciones"
            ),
            rx.spacer(),
            info_text(
                "+100",  
                "clientes"
            ),
            width="100%"
        ),
        rx.text(
            f"""
            Soy ingeniero de telecomunicaciones masterizado en DevOps.
            Soy ingeniero de telecomunicaciones masterizado en DevOps.
            Con {experience()} años de experiencia
            """,
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value
    )

def experience() -> int:
    return datetime.date.today().year - 2010