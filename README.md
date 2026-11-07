# Contador interactivo con Flet

Taller de investigación — Programación Orientada a Objetos
Tema: Interfaces gráficas y programación orientada a eventos

**Biblioteca:** [Flet](https://flet.dev)

## Descripción
Flet es un framework para construir aplicaciones de escritorio, web y móviles
en Python, usando controles basados en Flutter. Este proyecto es un contador
interactivo que demuestra la creación de una ventana, de componentes gráficos
y el manejo de eventos del usuario.

## Instalación y ejecución
Requisitos: Python 3.10 o superior.

```bash
git clone https://github.com/andrxs73/contador-flet.git
cd contador-flet
pip install -r requirements.txt
python main.py
```
Para verlo en el navegador: `flet run --web main.py`

## Evidencia

**Valor positivo (se muestra en verde):**

![Contador en valor positivo](capturas/Captura_de_pantalla_2026-11-07_095204.png)

**Valor negativo (se muestra en rojo):**

![Contador en valor negativo](capturas/Captura_de_pantalla_2026-11-07_095214.png)

**Valor en cero (después de reiniciar):**

![Contador en cero](capturas/Captura_de_pantalla_2026-11-07_095222.png)

**Video de demostración:** [Ver video](capturas/Contador_interactivo_con_Flet_2026-11-07_09-51-27.mp4)

## Explicación del ejemplo
La clase `ContadorApp` construye la interfaz y contiene la lógica.
- **Ventana:** Flet entrega un objeto `Page` a `main(page)`; se configura su título y alineación.
- **Componentes:** `Text` muestra el título y el valor; tres `IconButton` (+, −, reiniciar) están dentro de un `Row`.
- **Eventos:**
  - `on_click` de cada botón detecta los clics del mouse.
  - `page.on_keyboard_event` detecta teclas (↑ suma, ↓ resta, R reinicia).
- **Respuesta:** los métodos `incrementar`, `decrementar`, `reiniciar` y
  `al_presionar_tecla` modifican el valor del contador.
- **Actualización visual:** `actualizar_vista()` cambia el texto y su color y
  llama a `page.update()` para redibujar.

## Investigación

**¿Qué es y para qué sirve?** Framework de Python para crear interfaces sin conocimientos de frontend, con controles basados en Flutter.

**¿Qué aplicaciones permite?** Herramientas internas, dashboards, formularios y prototipos, empaquetables para Windows, macOS, Linux, iOS, Android y web.

**¿Instalación y requisitos?** Python 3.10+ y `pip install flet`. Se ejecuta con `flet run` o `python main.py`.

**¿Componentes principales?** `Page`, `Text`, `TextField`, `IconButton`, `Button`, `Row`, `Column`, `Container`, `Image`, `Checkbox`, `Dropdown`, `Slider`, `AlertDialog`, entre otros.

**¿Manejo de eventos?** Cada control tiene propiedades `on_*` (`on_click`, `on_change`, ...) a las que se asigna una función que recibe un objeto de evento. El teclado se maneja con `page.on_keyboard_event`. Tras modificar controles se llama a `page.update()`.

**Ventajas frente a Tkinter:** aspecto moderno, multiplataforma (incluye web y móvil), código compacto, empaquetado integrado.

**Limitaciones:** hay que instalarlo (Tkinter viene con Python), es más pesado, es más joven y su API ha cambiado entre versiones, y tiene menos material de apoyo que Tkinter.

## Fuentes consultadas
- Repositorio oficial: https://github.com/flet-dev/flet
- Documentación: https://pub.dev/documentation/flet/latest/
- Sitio oficial: https://flet.dev

## Autor
Tu nombre — Programación Orientada a Objetos
