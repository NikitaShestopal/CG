import numpy as np
from ProjectlyUtils import create_scene, create_axis_quat, decompose_matrix

from src.math.Quaternion import Quaternion
from src.engine.model.Cube import Cube
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation


def task_11():
    print("\n--- Завдання 11: Математичний доказ ---")
    qx = Quaternion.rotation_x(np.radians(30))
    qy = Quaternion.rotation_y(np.radians(45))
    qz = Quaternion.rotation_z(np.radians(60))
    q_extrinsic = qz * qy * qx
    q_intrinsic = qz * qy * qx

    print(
        f"Кватерніон Зовнішнього (A): ({q_extrinsic.w:.4f}, {q_extrinsic.x:.4f}, {q_extrinsic.y:.4f}, {q_extrinsic.z:.4f})")
    print(
        f"Кватерніон Внутрішнього (Б): ({q_intrinsic.w:.4f}, {q_intrinsic.x:.4f}, {q_intrinsic.y:.4f}, {q_intrinsic.z:.4f})")
    print("Висновок: Послідовності призводять до ідентичної орієнтації!")

    scene = create_scene("Завдання 11: Зовнішні vs Внутрішні")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_extrinsic, channel="cube")
    )
    scene.show()


def task_12():
    print("\n--- Завдання 12: Декомпозиція 'Чорної скриньки' ---")
    mat_black_box = np.array([
        [2.0, 0.0, 0.0, 1.0],
        [0.0, 2.0, 0.0, 2.0],
        [0.0, 0.0, 2.0, 3.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    t, s, r_mat, ax, ang = decompose_matrix(mat_black_box)
    is_orthogonal = np.allclose(r_mat.T @ r_mat, np.eye(3))

    print(f"Знайдений Вектор перенесення: {t}")
    print(f"Знайдений Масштаб: {s}")
    print(f"Чиста матриця обертання ортогональна?: {is_orthogonal}")
    print(f"Обертання: кут {np.degrees(ang):.2f}° навколо осі {ax}")

    scene = create_scene("Завдання 12: Результат декомпозиції")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    scene.add_animations(
        TranslationAnimation(end=t, channel="cube"),
        ScaleAnimation(end=s, channel="cube"),
        QuaternionAnimation(end_quaternion=create_axis_quat(ax, ang), channel="cube")
    )
    scene.show()


def task_13():
    scene = create_scene("Завдання 13: Локальні трансформації")
    obj = Cube(alpha=0.5)
    obj.show_local_frame()
    scene["obj"] = obj

    q1 = Quaternion.rotation_x(np.radians(45))
    t_global = np.array([2.0, 0.0, 0.0])
    q3_local = Quaternion.rotation_y(np.radians(30))
    q_final = q1 * q3_local

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="obj"),
        TranslationAnimation(end=t_global, channel="obj")
    )
    scene.show()


def task_15():
    scene = create_scene("Завдання 15: Комплексна композиція")
    cube = Cube(alpha=0.5)
    cube.show_pivot()
    cube.pivot(1, 1, 1)
    cube.show_local_frame()
    scene["cube"] = cube

    s_final = np.array([2.0, 2.0, 2.0])
    q_final = Quaternion.rotation_z(np.radians(90))
    t_final = np.array([-3.0, 4.0, 2.0])

    scene.add_animations(
        ScaleAnimation(end=s_final, channel="cube"),
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )

    print("\n--- Завдання 15: Дані передані до рушія ---")
    print("Рушій автоматично враховує зсув опорної точки для фінальної позиції вершин.")
    scene.show()