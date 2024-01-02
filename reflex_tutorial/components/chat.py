import reflex as rx

from reflex_tutorial.styles import style
from reflex_tutorial.states.answer_state import AnswerState

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                question,
                style=style.question_style
            ), 
            text_align="right",
        ),
        rx.box(
            rx.text(
                answer, 
                style=style.answer_style,
            ), 
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            AnswerState.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        ),
    )