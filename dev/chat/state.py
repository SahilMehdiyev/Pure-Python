import reflex as rx



class ChatState(rx.State):
    did_submit: bool = True

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit

    def handle_submit(self,form_data:dict):
        print(form_data)