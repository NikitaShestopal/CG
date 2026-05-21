import numpy as np
from src.math.Quaternion import Quaternion
from src.engine.scene.AnimatedScene import AnimatedScene

def create_axis_quat(axis, angle_rad):
    axis = np.array(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)  # Нормалізація вектора

    half_angle = angle_rad / 2.0
    w = np.cos(half_angle)
    x, y, z = axis * np.sin(half_angle)
    return Quaternion(w, x, y, z)

def create_scene(title):
    return AnimatedScene(
        title=title,
        image_size=(10, 10),
        coordinate_rect=(-5, -5, -5, 5, 5, 5),
    )

def decompose_matrix(mat):
    translation = mat[:3, 3]

    scale_x = np.linalg.norm(mat[:3, 0])
    scale_y = np.linalg.norm(mat[:3, 1])
    scale_z = np.linalg.norm(mat[:3, 2])
    scale = np.array([scale_x, scale_y, scale_z])

    rot_mat = mat[:3, :3] / scale

    trace = np.trace(rot_mat)
    cos_theta = np.clip((trace - 1) / 2.0, -1.0, 1.0)
    angle_rad = np.arccos(cos_theta)

    if np.isclose(angle_rad, 0):
        axis = np.array([1.0, 0.0, 0.0])
    else:
        rx = rot_mat[2, 1] - rot_mat[1, 2]
        ry = rot_mat[0, 2] - rot_mat[2, 0]
        rz = rot_mat[1, 0] - rot_mat[0, 1]
        axis = np.array([rx, ry, rz])
        axis = axis / np.linalg.norm(axis)

    return translation, scale, rot_mat, axis, angle_rad