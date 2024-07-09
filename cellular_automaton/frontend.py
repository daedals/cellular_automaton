
from fastapi import FastAPI
from nicegui import app, ui, events


def init(fastapi_app: FastAPI) -> None:
    """ initializes the ui with nicegui """
    @ui.page('/')
    def show():
        ui.label('Hello, FastAPI!')
        ui.button('Hello, World!')

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

    def mouse_handler(e: events.MouseEventArguments):
        color = 'SkyBlue' if e.type == 'mousedown' else 'SteelBlue'
        ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
        ui.notify(f'{e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')

    ii = ui.interactive_image("(600,400)", on_mouse=mouse_handler, events=['mousedown', 'mouseup'])

    ui.run_with(
        fastapi_app,
        mount_path='/gui',  # NOTE this can be omitted if you want the paths passed to @ui.page to be at the root   
        storage_secret='pick your private secret here',  # NOTE setting a secret is optional but allows for persistent storage per user
    )