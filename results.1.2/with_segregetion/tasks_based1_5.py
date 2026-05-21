import numpy as np
import random
from ProjectlyUtils import create_scene, create_axis_quat

from src.math.Quaternion import Quaternion
from src.engine.model.Cube import Cube
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation


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