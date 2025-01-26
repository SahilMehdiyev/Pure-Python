import reflex as rx

from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE) 
    
    def to_about_us(self):
        # print('clickeddddd-----------')
        return rx.redirect(routes.ABOUT_US_ROUTE) 
    
    def to_chat(self):
        return rx.redirect(routes.CHAT_ROUTE)
    
    def to_signup(self):
        return rx.redirect(routes.SIGNUP)

    def to_login(self):
        return rx.redirect(routes.LOGIN)