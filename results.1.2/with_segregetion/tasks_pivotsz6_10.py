import numpy as np
from ProjectlyUtils import create_scene, create_axis_quat

from src.math.Quaternion import Quaternion
from src.engine.model.Cube import Cube
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation


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