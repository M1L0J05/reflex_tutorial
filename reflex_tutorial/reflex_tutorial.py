import reflex as rx

from .styles import style

from .components import action_bar, chat


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
        )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()