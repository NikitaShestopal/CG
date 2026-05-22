import numpy as np


def quat_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return np.array([
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    ])


def quat_conjugate(q):
    return np.array([q[0], -q[1], -q[2], -q[3]])


# ==========================================
def task_0():
    print("\n--- Завдання 0: Від осі/кута до кватерніона ---")
    axis = np.array([1, 1, 1]) / np.sqrt(3)
    angle = np.radians(60)

    w = np.cos(angle / 2)
    xyz = axis * np.sin(angle / 2)
    q = np.array([w, xyz[0], xyz[1], xyz[2]])

    norm = np.linalg.norm(q)
    print(f"Кватерніон q: {np.round(q, 4)}")
    print(f"Норма |q|: {norm:.4f}")

    w, x, y, z = q
    R = np.array([
        [1 - 2 * y ** 2 - 2 * z ** 2, 2 * x * y - 2 * z * w, 2 * x * z + 2 * y * w],
        [2 * x * y + 2 * z * w, 1 - 2 * x ** 2 - 2 * z ** 2, 2 * y * z - 2 * x * w],
        [2 * x * z - 2 * y * w, 2 * y * z + 2 * x * w, 1 - 2 * x ** 2 - 2 * y ** 2]
    ])
    print("Відповідна матриця R:\n", np.round(R, 4))


# ==========================================
def task_1():
    print("\n--- Завдання 1: Поворот вектора кватерніоном ---")
    p = np.array([1, 0, 0])
    v = np.array([0, 1, 0, 0])

    angle = np.radians(90)
    q = np.array([np.cos(angle / 2), 0, 0, np.sin(angle / 2)])
    q_inv = quat_conjugate(q)

    # v' = q * v * q^-1
    temp = quat_mult(q, v)
    v_prime = quat_mult(temp, q_inv)

    print(f"Початкова точка p: {p}")
    print(f"Результат (векторна частина v'): {np.round(v_prime[1:], 4)}")
    print("Очікуваний результат: [0. 1. 0.] - Збігається!")


# ==========================================
def task_2():
    print("\n--- Завдання 2: Композиція обертань ---")
    tet_verts = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])

    ax = np.radians(45)
    q1 = np.array([np.cos(ax / 2), np.sin(ax / 2), 0, 0])

    ay = np.radians(30)
    q2 = np.array([np.cos(ay / 2), 0, np.sin(ay / 2), 0])

    q_total = quat_mult(q2, q1)
    print(f"Результуючий кватерніон: {np.round(q_total, 4)}")

    theta = 2 * np.arccos(q_total[0])
    axis = q_total[1:] / np.sin(theta / 2)
    print(f"Сумарний кут: {np.degrees(theta):.2f}°")
    print(f"Сумарна вісь: {np.round(axis, 4)}")

    print("Нові координати тетраедра:")
    q_inv = quat_conjugate(q_total)
    for pt in tet_verts:
        v = np.array([0, pt[0], pt[1], pt[2]])
        v_prime = quat_mult(quat_mult(q_total, v), q_inv)
        print(f"{pt} -> {np.round(v_prime[1:], 4)}")


# ==========================================
def task_3():
    print("\n--- Завдання 3: Кути Ойлера та Gimbal Lock ---")
    roll = np.radians(50)
    pitch = np.radians(90)
    yaw = np.radians(20)

    qx = np.array([np.cos(roll / 2), np.sin(roll / 2), 0, 0])
    qy = np.array([np.cos(pitch / 2), 0, np.sin(pitch / 2), 0])
    qz = np.array([np.cos(yaw / 2), 0, 0, np.sin(yaw / 2)])

    q_total = quat_mult(quat_mult(qz, qy), qx)
    print(f"Фінальний кватерніон: {np.round(q_total, 4)}")
    print(
        "Висновки: Кватерніон має валідні компоненти. На відміну від матриць, де стовпці дублюються при Pitch=90°, кватерніон зберігає унікальну 4D-орієнтацію.")


# ==========================================
def task_5():
    print("\n--- Завдання 4 та 5: Повна декомпозиція матриці ---")
    M = np.array([
        [0, -2, 0, 10],
        [1, 0, 0, -5],
        [0, 0, 1.5, 3],
        [0, 0, 0, 1]
    ])

    T = M[:3, 3]
    print(f"1. Вилучення трансляції T: {T}")

    S = np.array([
        np.linalg.norm(M[:3, 0]),
        np.linalg.norm(M[:3, 1]),
        np.linalg.norm(M[:3, 2])
    ])
    print(f"2. Масштаб S: {S}")

    R = M[:3, :3] / S
    print("3. Чиста матриця обертання R:\n", np.round(R, 4))

    trace = np.trace(R)
    w = np.sqrt(1 + trace) / 2
    x = (R[2, 1] - R[1, 2]) / (4 * w)
    y = (R[0, 2] - R[2, 0]) / (4 * w)
    z = (R[1, 0] - R[0, 1]) / (4 * w)

    q = np.array([w, x, y, z])
    print(f"4. Результуючий кватерніон: {np.round(q, 4)}")


if __name__ == '__main__':
    task_0()
    task_1()
    task_2()
    task_3()
    task_5()