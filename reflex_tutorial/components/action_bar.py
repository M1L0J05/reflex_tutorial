import reflex as rx

from reflex_tutorial.styles import style
from reflex_tutorial.states.answer_state import AnswerState

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=AnswerState.question,
            placeholder="Ask a question",
            on_change=AnswerState.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=AnswerState.answer,
            style=style.button_style,
        ),
    )