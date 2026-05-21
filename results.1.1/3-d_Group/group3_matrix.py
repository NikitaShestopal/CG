import numpy as np
from engine.model.Polygon import Polygon
from engine.scene.Scene import Scene


class MatrixScene(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self["sq_init"] = Polygon()
        self["sq_init"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)

        self["sq_final"] = Polygon()
        self["sq_final"].set_geometry(0, 0, 1, 0, 1, 1, 0, 1)

        self["pivot"] = Polygon()
        self["pivot"].set_geometry(0, 0)
        self["pivot"]["vertices_show"] = False


def set_contrasty_styles(scene):
    scene["sq_init"]["color"] = "red"
    scene["sq_init"]["line_style"] = "--"
    scene["sq_init"]["line_width"] = 1.5

    scene["sq_final"]["color"] = "cyan"
    scene["sq_final"]["line_style"] = "-"
    scene["sq_final"]["line_width"] = 2.5
    scene["sq_final"]["vertices_show"] = True
    scene["sq_final"]["vertex_color"] = "darkblue"

def task11_frame(scene):
    set_contrasty_styles(scene)

    T = np.array([
        [2.934, 0.624, 0],
        [-0.416, 1.956, 0],
        [2.000, 3.400, 1]
    ])

    T_inv = np.linalg.inv(T)
    print("Матриця зворотної трансформації:\n", np.round(T_inv, 3))
    pts_global = np.array([
        [2.0, 3.4, 1],
        [4.9, 4.0, 1],
        [4.5, 6.0, 1],
        [1.6, 5.4, 1]
    ])
    pts_local = pts_global.dot(T_inv)

    local_coords = pts_local[:, :2].flatten().tolist()
    global_coords = pts_global[:, :2].flatten().tolist()

    scene["sq_init"].set_geometry(*local_coords)
    scene["sq_final"].set_geometry(*global_coords)

def task12_frame(scene):
    set_contrasty_styles(scene)

    T = np.array([
        [0.866, 0.5, 0],
        [0.5, 0.866, 0],
        [4, 3, 1]
    ])

    pts_initial = np.array([
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ])

    pts_final = pts_initial.dot(T)

    final_coords = pts_final[:, :2].flatten().tolist()

    scene["sq_final"].set_geometry(*final_coords)

def task13_frame(scene):
    set_contrasty_styles(scene)

    T = [
        [1.414, 1.414, 0],
        [-2.121, 2.121, 0],
        [1.0, 1.0, 1]
    ]

    sx = np.sqrt(T[0][0] ** 2 + T[0][1] ** 2)
    sy = np.sqrt(T[1][0] ** 2 + T[1][1] ** 2)

    angle_rad = np.arccos(T[0][0] / sx)

    tx, ty = T[2][0], T[2][1]

    scene["sq_final"].scale = (sx, sy)
    scene["sq_final"].rotation = angle_rad
    scene["sq_final"].translation = (tx, ty)


def task14_frame(scene):
    set_contrasty_styles(scene)

    px, py = 1, 1
    scene["pivot"].set_geometry(px, py)
    scene["pivot"]["vertices_show"] = True
    scene["pivot"]["vertex_color"] = "magenta"
    scene["pivot"]["vertex_size"] = 6
    scene["pivot"]["labels"] = [("Pivot (1, 1)", (0.1, 0.1))]

    T = [
        [1.732, 1, 0],
        [-1, 1.732, 0],
        [5, -3, 1]
    ]

    sx = np.sqrt(T[0][0] ** 2 + T[0][1] ** 2)  # = 2
    sy = np.sqrt(T[1][0] ** 2 + T[1][1] ** 2)  # = 2
    angle_rad = np.arccos(T[0][0] / sx)  # = 30 градусів

    tx, ty = T[2][0], T[2][1]

    scene["sq_final"].scale = (sx, sy)
    scene["sq_final"].rotation = angle_rad
    scene["sq_final"].translation = (tx, ty)


if __name__ == '__main__':
    scene = MatrixScene(
        coordinate_rect=(-2, -2, 8, 8),
        grid_show=True,
        axis_show=True,
        axis_color=("black", "black"),
        title="Завдання 11: Відновлення зображення (Inverse Matrix)"
    )

    scene.add_frames(task11_frame)
    scene.show()