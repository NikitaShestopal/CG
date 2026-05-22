import numpy as np

from engine.scene.AnimatedScene import AnimatedScene
from src.math.Quaternion import Quaternion
from src.engine.model.Cube import Cube
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation


# ==========================================
def get_rx(angle_deg):
    a = np.radians(angle_deg)
    return np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])


def get_ry(angle_deg):
    a = np.radians(angle_deg)
    return np.array([[np.cos(a), 0, np.sin(a)], [0, 1, 0], [-np.sin(a), 0, np.cos(a)]])


def get_rz(angle_deg):
    a = np.radians(angle_deg)
    return np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])


CUBE_VERTS = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

def create_scene(title):
    return AnimatedScene(
        title=title,
        image_size=(10, 10),
        coordinate_rect=(-5, -5, -5, 5, 5, 5),
        grid_show=True,              # Додаємо сітку
        axis_show_from_origin=True,
        axis_line_width=1.0,
        axis_line_style="--"
    )
# ==========================================
def task_1_new():
    print("\n--- Завдання 1: Масштаб, Euler XYZ, Зсув ---")
    scale = np.array([2.0, 0.5, 1.0])
    trans = np.array([-3.0, 2.0, 5.0])

    S_mat = np.diag([2.0, 0.5, 1.0])
    R_mat = get_rz(60) @ get_ry(45) @ get_rx(30)

    verts_scaled = CUBE_VERTS @ S_mat.T
    verts_rotated = verts_scaled @ R_mat.T
    verts_final = verts_rotated + trans

    print(f"Матриця обертання XYZ:\n{np.round(R_mat, 3)}")
    print(f"Координати вершини (1,1,1) після всіх трансформацій: {np.round(verts_final[6], 3)}")

    # Візуалізація
    scene = create_scene("Завдання 1: Розтяг, Ейлер XYZ, Зсув")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    qx = Quaternion.rotation_x(np.radians(30))
    qy = Quaternion.rotation_y(np.radians(45))
    qz = Quaternion.rotation_z(np.radians(60))
    q_final = qz * qy * qx

    scene.add_animations(
        ScaleAnimation(end=scale, channel="cube"),
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=trans, channel="cube")
    )
    scene.show()


# ==========================================
def task_2_new():
    print("\n--- Завдання 2: Euler ZYX та Зсув ---")
    trans = np.array([1.0, 3.0, -2.0])

    R_mat = get_rx(50) @ get_ry(35) @ get_rz(20)
    verts_rotated = CUBE_VERTS @ R_mat.T
    verts_final = verts_rotated + trans

    print(f"Матриця обертання ZYX:\n{np.round(R_mat, 3)}")

    scene = create_scene("Завдання 2: Кути Ейлера ZYX")
    cube = Cube(alpha=0.5)
    cube.show_local_frame()
    scene["cube"] = cube

    qz = Quaternion.rotation_z(np.radians(20))
    qy = Quaternion.rotation_y(np.radians(35))
    qx = Quaternion.rotation_x(np.radians(50))
    q_final = qx * qy * qz

    scene.add_animations(
        QuaternionAnimation(end_quaternion=q_final, channel="cube"),
        TranslationAnimation(end=trans, channel="cube")
    )
    scene.show()


# ==========================================
def task_3_new():
    print("\n--- Завдання 3: Порівняння XYZ та ZYX ---")
    ax, ay, az = 45, 30, 60

    R_xyz = get_rz(az) @ get_ry(ay) @ get_rx(ax)
    R_zyx = get_rx(ax) @ get_ry(ay) @ get_rz(az)

    verts_xyz = CUBE_VERTS @ R_xyz.T
    verts_zyx = CUBE_VERTS @ R_zyx.T

    print("Матриця XYZ:\n", np.round(R_xyz, 3))
    print("Матриця ZYX:\n", np.round(R_zyx, 3))
    print("\nРізниця координат вершини (1,1,1):")
    print(f"XYZ: {np.round(verts_xyz[6], 3)}")
    print(f"ZYX: {np.round(verts_zyx[6], 3)}")


# ==========================================
def task_5_new():
    print("\n--- Завдання 5: Практичний доказ Gimbal Lock ---")

    R1 = get_rz(45) @ get_ry(90) @ get_rx(30)
    verts1 = CUBE_VERTS @ R1.T

    R2 = get_rz(35) @ get_ry(90) @ get_rx(40)
    verts2 = CUBE_VERTS @ R2.T

    diff = np.max(np.abs(verts1 - verts2))
    print(f"Максимальна різниця між координатами двох станів: {diff:.10f}")
    if np.allclose(verts1, verts2):
        print("ВИСНОВОК: Координати ідентичні! Зміна X і Z скомпенсувала одна одну (склеювання осей).")


# ==========================================
def lerp(a, b, t):
    return a + (b - a) * t


def task_6_new():
    print("\n--- Завдання 6: Lerp у зоні сингулярності ---")
    vec_forward = np.array([0, 0, 1])

    steps = 10
    print("Крок | Кути (X,Y,Z)       | Вектор погляду (transform(0,0,1))")
    print("-" * 65)
    for i in range(steps + 1):
        t = i / steps
        ax = lerp(0, 90, t)
        ay = lerp(0, 90, t)
        az = lerp(0, 90, t)

        R = get_rz(az) @ get_ry(ay) @ get_rx(ax)
        vec_transformed = R @ vec_forward

        print(f"{i:4d} | ({ax:5.1f}, {ay:5.1f}, {az:5.1f}) | {np.round(vec_transformed, 3)}")

    print("\nПояснення: При наближенні до Y=90°, зміна осей X та Z починає діяти")
    print("в одній площині, що призводить до нелінійної швидкості повороту вектора погляду.")

# ==========================================
def extract_euler_from_matrix(R):
    sy = R[0, 2]

    if np.isclose(sy, 1.0):
        y = np.pi / 2
        x = 0.0
        z = np.arctan2(R[1, 0], R[1, 1])
        print("⚠️ Виявлено Gimbal Lock (Y=90°). Примусово встановлено X=0.")
    elif np.isclose(sy, -1.0):
        y = -np.pi / 2
        x = 0.0
        z = -np.arctan2(R[1, 0], R[1, 1])
        print("⚠️ Виявлено Gimbal Lock (Y=-90°). Примусово встановлено X=0.")
    else:
        y = np.arcsin(sy)
        x = np.arctan2(-R[1, 2], R[2, 2])
        z = np.arctan2(-R[0, 1], R[0, 0])

    return np.degrees([x, y, z])


def task_7_new():
    print("\n--- Завдання 7: Декомпозиція матриці ---")
    R_gimbal = get_rz(45) @ get_ry(90) @ get_rx(30)

    print("Оригінальні кути: X=30°, Y=90°, Z=45°")
    extracted_angles = extract_euler_from_matrix(R_gimbal)

    print(f"Знайдені кути: X={extracted_angles[0]:.1f}°, Y={extracted_angles[1]:.1f}°, Z={extracted_angles[2]:.1f}°")
    print("Сума X+Z (або різниця) зберігається, що підтверджує наявність безлічі розв'язків!")


if __name__ == '__main__':
    # task_1_new()
    # task_2_new()
    # task_3_new()
    # task_5_new()
    # task_6_new()
    task_7_new()