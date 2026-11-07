"""Contador interactivo con Flet.

Demuestra cómo crear una ventana, mostrar componentes gráficos y
responder a eventos del usuario (clics del mouse y teclado).
"""

import flet as ft


class ContadorApp:
    """Encapsula la interfaz y la lógica del contador."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.valor = 0

        self.configurar_ventana()
        self.crear_componentes()
        self.mostrar_componentes()

        # Evento de teclado asociado a la página completa
        self.page.on_keyboard_event = self.al_presionar_tecla

    # ---------- Construcción de la interfaz ----------
    def configurar_ventana(self):
        self.page.title = "Contador interactivo con Flet"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def crear_componentes(self):
        self.titulo = ft.Text("Contador interactivo", size=24, weight=ft.FontWeight.BOLD)

        # Elemento visual cuyo valor cambiará con los eventos
        self.etiqueta = ft.Text(str(self.valor), size=80, weight=ft.FontWeight.BOLD)

        # Cada botón asocia el evento on_click con un método
        self.boton_menos = ft.IconButton(ft.Icons.REMOVE, on_click=self.decrementar)
        self.boton_mas = ft.IconButton(ft.Icons.ADD, on_click=self.incrementar)
        self.boton_reiniciar = ft.IconButton(ft.Icons.REFRESH, on_click=self.reiniciar)

        self.ayuda = ft.Text(
            "Clic en + / − / ↻   |   Teclado: ↑ suma, ↓ resta, R reinicia",
            size=12,
        )

    def mostrar_componentes(self):
        self.page.add(
            self.titulo,
            self.etiqueta,
            ft.Row(
                [self.boton_menos, self.boton_reiniciar, self.boton_mas],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            self.ayuda,
        )

    # ---------- Manejadores de eventos ----------
    def incrementar(self, e):
        self.valor += 1
        self.actualizar_vista()

    def decrementar(self, e):
        self.valor -= 1
        self.actualizar_vista()

    def reiniciar(self, e):
        self.valor = 0
        self.actualizar_vista()

    def al_presionar_tecla(self, e: ft.KeyboardEvent):
        if e.key == "Arrow Up":
            self.incrementar(e)
        elif e.key == "Arrow Down":
            self.decrementar(e)
        elif e.key.upper() == "R":
            self.reiniciar(e)

    # ---------- Actualización de la interfaz ----------
    def actualizar_vista(self):
        self.etiqueta.value = str(self.valor)
        if self.valor > 0:
            self.etiqueta.color = ft.Colors.GREEN
        elif self.valor < 0:
            self.etiqueta.color = ft.Colors.RED
        else:
            self.etiqueta.color = None
        self.page.update()  # Redibuja la interfaz con los cambios


def main(page: ft.Page):
    ContadorApp(page)


if __name__ == "__main__":
    # ft.run en versiones recientes; ft.app en versiones antiguas
    (ft.run if hasattr(ft, "run") else ft.app)(main)