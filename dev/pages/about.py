"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from dev import ui



def about_us_page() -> rx.Component:
    # About us  Page (Index)
    return ui.base_layout(
        rx.color_mode.button(position="top-left"),
        rx.vstack(
            rx.heading("Welcome to Rexlex About us ", size = '9'),
            spacing='5',
            justify = 'center',
            min_height = '85vh',
        ),
        rx.logo(),
    )
