import numpy as np
import random

from src.math.Quaternion import Quaternion
from src.engine.scene.AnimatedScene import AnimatedScene
from src.engine.model.Cube import Cube
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation

# ==========================================
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

# ==========================================
def task_1():
    scene = create_scene("Завдання 1: Обертання на 45° та зсув")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    q_final = create_axis_quat([1, 1, 0], np.radians(45))
    t_final = np.array([2.0, -1.0, 3.0])

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
def task_2():
    scene = create_scene("Завдання 2: Масштаб, Ейлер, Зсув")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    s_final = np.array([2.0, 0.5, 1.0])
    t_final = np.array([-3.0, 2.0, 5.0])

    qx = Quaternion.rotation_x(np.radians(30))
    qy = Quaternion.rotation_y(np.radians(45))
    qz = Quaternion.rotation_z(np.radians(60))
    q_final = qz * qy * qx

    scene.add_animations(
        ScaleAnimation(end=s_final, channel="cube"),
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
def task_3():
    scene = create_scene("Завдання 3: Композиція обертань")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    q1 = Quaternion.rotation_z(np.radians(60))

    q2 = create_axis_quat([1, 1, 1], np.radians(45))

    q_final = q2 * q1
    t_final = np.array([4.0, -2.0, 1.0])

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
def task_4():
    scene = create_scene("Завдання 4: Кути Ейлера ZYX")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    qz = Quaternion.rotation_z(np.radians(20))
    qy = Quaternion.rotation_y(np.radians(35))
    qx = Quaternion.rotation_x(np.radians(50))

    q_final = qx * qy * qz
    t_final = np.array([1.0, 3.0, -2.0])

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
def task_5():
    scene = create_scene("Завдання 5: Рандомізація")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    angle = np.radians(random.uniform(10, 90))
    rand_axis = [random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)]

    t_final = np.array([random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)])
    q_final = create_axis_quat(rand_axis, angle)

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
def task_6():
    scene = create_scene("Завдання 6: Опорна точка")
    cube = Cube(alpha=0.5)

    cube.show_pivot()
    cube.pivot(2, 0, 3)
    cube.show_local_frame()

    scene["cube"] = cube

    q_final = Quaternion.rotation_y(np.radians(45))
    t_final = np.array([-1.0, 2.0, 4.0])

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
def task_7():
    scene = create_scene("Завдання 7: Масштаб + Обертання (Опорна точка)")
    cube = Cube(alpha=0.5)
    cube.show_pivot()
    cube.pivot(1, 2, 3)
    cube.show_local_frame()
    scene["cube"] = cube
    s_final = np.array([1.0, 1.0, 3.0])
    q_final = Quaternion.rotation_z(np.radians(30))
    scene.add_animations(
        ScaleAnimation(end=s_final, channel="cube"),
        QuaternionAnimation(end_quaternion=q_final, channel="cube")
    )
    scene.show()


# ==========================================
def task_8():
    scene = create_scene("Завдання 8: Обертання зміщеної осі")
    obj = Cube(alpha=0.5)
    obj.show_pivot()
    obj.pivot(2, 3, 4)
    obj.show_local_frame()
    scene["obj"] = obj
    q_final = create_axis_quat([1, 1, 1], np.radians(90))
    t_final = np.array([0.0, -3.0, 2.0])

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="obj"),
        TranslationAnimation(end=t_final, channel="obj")
    )
    scene.show()

# ==========================================
def task_9():
    scene = create_scene("Завдання 9: Зміна перспективи")
    obj = Cube(alpha=0.5)
    obj.show_pivot()
    obj.pivot(3, 3, 0)
    obj.show_local_frame()
    scene["obj"] = obj
    qy = Quaternion.rotation_y(np.radians(60))
    qx = Quaternion.rotation_x(np.radians(30))
    q_final = qx * qy

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="obj")
    )
    scene.show()


# ==========================================
def task_10():
    scene = create_scene("Завдання 10: Комплексна трансформація")
    cube = Cube(alpha=0.5)

    cube.show_pivot()
    cube.pivot(1, 1, 1)
    cube.show_local_frame()
    scene["cube"] = cube

    s_final = np.array([2.0, 1.0, 1.0])
    q_final = Quaternion.rotation_y(np.radians(45))
    t_final = np.array([-3.0, 4.0, 2.0])

    scene.add_animations(
        ScaleAnimation(end=s_final, channel="cube"),
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=t_final, channel="cube")
    )
    scene.show()

# ==========================================
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

    # Декомпозиція
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

# ==========================================
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


# ==========================================
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

if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    # task_9()
    # task_10()
    # task_11()
    # task_12()
    # task_13()
    task_15()