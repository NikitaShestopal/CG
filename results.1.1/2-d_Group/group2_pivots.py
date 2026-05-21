import numpy as np
from engine.model.Polygon import Polygon
from engine.scene.Scene import Scene


class PivotScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self["sq_init"] = Polygon()
        self["sq_init"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)
        self["sq_final"] = Polygon()
        self["sq_final"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)

        self["pivot"] = Polygon()  # Крапка для візуалізації опорної точки


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

def apply_pivot_transform(scene, pivot_pt, scale=(1, 1), angle_deg=0, extra_translation=(0, 0)):
    set_contrasty_styles(scene)
    px, py = pivot_pt
    scene["pivot"].set_geometry(px, py)
    scene["pivot"]["vertices_show"] = True
    scene["pivot"]["vertex_color"] = "red"

    sx, sy = scale
    angle = np.radians(angle_deg)
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    sq = scene["sq_final"]
    sq.scale = (sx, sy)
    sq.rotation = angle
    rx = px - (px * sx * cos_a - py * sy * sin_a)
    ry = py - (px * sx * sin_a + py * sy * cos_a)
    sq.translation = (rx + extra_translation[0], ry + extra_translation[1])

# --- Завдання 7: Поворот навколо Pivot ---
def task7_frame(scene):
    apply_pivot_transform(scene, pivot_pt=(2,2), angle_deg=60)

# --- Завдання 8: Розтяг навколо Pivot ---
def task8_frame(scene):
    apply_pivot_transform(scene, pivot_pt=(0.5, 0.5), scale=(2, 3))

# --- Завдання 9: Розтяг + Переміщення з Pivot ---
def task9_frame(scene):
    apply_pivot_transform(scene, pivot_pt=(1, 1), scale=(2, 1), extra_translation=(3, -2))

if __name__ == '__main__':
    scene = PivotScene(coordinate_rect=(-2, -4, 6, 2), grid_show=True, axis_show=True)
    scene.add_frames(task9_frame)
    scene.show()