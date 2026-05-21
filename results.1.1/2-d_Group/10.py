import numpy as np
from engine.model.Polygon import Polygon
from engine.scene.Scene import Scene


class Task10Scene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self["sq_init"] = Polygon()
        self["sq_init"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)
        self["sq_final"] = Polygon()
        self["sq_final"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)
        self["pivot"] = Polygon()


def set_contrasty_styles(scene):
    scene["sq_init"]["color"] = "red"
    scene["sq_init"]["line_style"] = "--"
    scene["sq_init"]["line_width"] = 1.5

    scene["sq_final"]["color"] = "cyan"
    scene["sq_final"]["line_style"] = "-"
    scene["sq_final"]["line_width"] = 2.5
    scene["sq_final"]["vertices_show"] = True
    scene["sq_final"]["vertex_color"] = "darkblue"


def apply_task10_transform(scene, order="SRT"):
    set_contrasty_styles(scene)

    # Опорна точка
    px, py = 0.5, 0.5
    scene["pivot"].set_geometry(px, py)
    scene["pivot"]["vertices_show"] = True
    scene["pivot"]["vertex_color"] = "magenta"
    scene["pivot"]["vertex_size"] = 6
    scene["pivot"]["labels"] = [("Pivot", (0.1, 0.1))]

    sx, sy = 2, 2
    angle = np.radians(30)
    tx, ty = 1, -1

    cos_a, sin_a = np.cos(angle), np.sin(angle)

    sq = scene["sq_final"]
    sq.scale = (sx, sy)
    sq.rotation = angle

    rx = px - (px * sx * cos_a - py * sy * sin_a)
    ry = py - (px * sx * sin_a + py * sy * cos_a)

    if order == "SRT":
        extra_tx, extra_ty = tx, ty

    elif order == "TSR":
        tx_scaled = tx * sx
        ty_scaled = ty * sy
        extra_tx = tx_scaled * cos_a - ty_scaled * sin_a
        extra_ty = tx_scaled * sin_a + ty_scaled * cos_a

    elif order == "STR":
        extra_tx = tx * cos_a - ty * sin_a
        extra_ty = tx * sin_a + ty * cos_a

    sq.translation = (rx + extra_tx, ry + extra_ty)


def task10_srt_frame(scene):
    apply_task10_transform(scene, order="SRT")


def task10_tsr_frame(scene):
    apply_task10_transform(scene, order="TSR")


def task10_str_frame(scene):
    apply_task10_transform(scene, order="STR")


if __name__ == '__main__':
    scene = Task10Scene(
        coordinate_rect=(-3, -3, 6, 6),
        grid_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        title="Завдання 10: Зсув -> Масштаб -> Обертання"
    )

    scene.add_frames(task10_srt_frame)
    scene.show()