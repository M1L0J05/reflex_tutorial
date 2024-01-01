import reflex as rx

from reflex_tutorial.styles import style


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
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )