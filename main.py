from Controller.controller import Controller

def criar_view(tipo):
    if tipo == "tkinter":
        from View.TkInterView import TkInterView
        return TkInterView()
    raise ValueError("Tipo de View Inválido!")

def main():
    controller = Controller()
    view = criar_view("tkinter")
    view.set_controller(controller)
    controller.set_view(view)
    view.iniciar_app()

if __name__ == "__main__":
    main()