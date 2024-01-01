import reflex as rx

from reflex_tutorial.styles import style


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Haz una pregunta",
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            style=style.button_style,
        ),
        
    )