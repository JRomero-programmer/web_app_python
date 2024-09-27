import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
import link_bio.constants as constants
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.box(
            rx.link(
                f"© {datetime.date.today().year} DevSecOps by Jonatan Romero v3.",
                href=constants.LINKEDIN_URL,
                is_external=True,
                font_size=Size.MEDIUM.value
            ),
            rx.text("""BUILDING CI/CD WITH ♥ FROM BARCELONA TO THE WORLD."""),
            spacing="0",
            text_align="center"
        ),
        font_size=Size.MEDIUM.value,
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        align="center",
        color=TextColor.FOOTER.value
    )