import numpy as np
from engine.model.Polygon import Polygon
from engine.scene.Scene import Scene


class Group1Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self["sq_init"] = Polygon()
        self["sq_init"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)
        self["sq_final"] = Polygon()
        self["sq_final"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)


def set_contrasty_styles(scene):
    scene["sq_init"]["color"] = "red"
    scene["sq_init"]["line_style"] = "--"
    scene["sq_init"]["line_width"] = 1.5

    scene["sq_final"]["color"] = "cyan"
    scene["sq_final"]["line_style"] = "-"
    scene["sq_final"]["line_width"] = 2.5
    scene["sq_final"]["vertices_show"] = True
    scene["sq_final"]["vertex_color"] = "darkblue"
    scene["sq_final"]["vertex_size"] = 5


def task1_frame(scene):
    set_contrasty_styles(scene)
    scene["sq_final"].rotation = np.radians(30)
    scene["sq_final"].translation = (2, 3)


def task2_frame(scene):
    set_contrasty_styles(scene)
    scene["sq_final"].scale = (2, 1)
    scene["sq_final"].rotation = np.radians(45)


def task3_frame(scene):
    set_contrasty_styles(scene)
    scene["sq_final"].rotation = np.radians(90)
    scene["sq_final"].translation = (2, 3)


def task4_frame(scene):
    set_contrasty_styles(scene)
    scene["sq_final"].scale = (1, 3)
    scene["sq_final"].rotation = np.radians(60)


def task5_frame(scene):
    set_contrasty_styles(scene)
    # Завдання: Переміщення (1, -1) -> Масштаб (2, 2)
    scene["sq_final"].scale = (2, 2)
    scene["sq_final"].translation = (1 * 2, -1 * 2)


def task6_frame(scene):
    set_contrasty_styles(scene)
    # Завдання 6. Варіант 2: Переміщення (2,3) -> Розтяг (1,3) -> Поворот 60°
    s_x, s_y = 1, 3
    angle = np.radians(60)
    t_x, t_y = 2, 3

    tx_scaled = t_x * s_x
    ty_scaled = t_y * s_y

    tx_final = tx_scaled * np.cos(angle) - ty_scaled * np.sin(angle)
    ty_final = tx_scaled * np.sin(angle) + ty_scaled * np.cos(angle)

    scene["sq_final"].scale = (s_x, s_y)
    scene["sq_final"].rotation = angle
    scene["sq_final"].translation = (tx_final, ty_final)


if __name__ == '__main__':
    scene = Group1Scene(
        coordinate_rect=(-12, -12, 16, 16),
        grid_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        title=""
    )

    scene.add_frames(task6_frame)
    scene.show()