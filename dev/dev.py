"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def about_us() -> rx.Component:
    # About us  Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-left"),
        rx.vstack(
            rx.heading("Welcome to Rexlex About us ", size = '9'),
            spacing='5',
            justify = 'center',
            min_height = '85vh',
        ),
        rx.logo(),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-left"),
        rx.vstack(
            rx.text(
                rx.heading("Welcome to Reflex GPT! ", size = '9'),
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!",),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
