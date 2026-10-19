#!/usr/bin/env python3
"""Décollage, hover au-dessus de la position de départ, puis atterrissage.

Prérequis : le launch Crazyswarm2 tourne déjà dans un autre terminal
    ros2 launch crazyflie launch.py backend:=cpp mocap:=True
avec /poses publié et le drone connecté.

Usage :
    source ~/eswarm/install/setup.bash
    python3 hover_start.py
"""
from crazyflie_py import Crazyswarm

ROBOT = "cf1_eswarm"   # nom du robot dans crazyflies.yaml
HEIGHT = 0.3           # m, hauteur de hover (commence bas)
TAKEOFF_TIME = 3.0     # s
HOVER_TIME = 10.0      # s
LAND_TIME = 3.0        # s


def main():
    swarm = Crazyswarm()
    time_helper = swarm.timeHelper
    cf = swarm.allcfs.crazyfliesByName[ROBOT]

    try:
        # Le commandeur haut niveau décolle à la verticale de la position
        # courante, puis maintient (x, y, z) grâce à l'EKF alimenté par la MoCap.
        cf.takeoff(targetHeight=HEIGHT, duration=TAKEOFF_TIME)
        time_helper.sleep(TAKEOFF_TIME + 0.5)

        # Hover : on laisse simplement le drone tenir sa position.
        time_helper.sleep(HOVER_TIME)
    finally:
        # Atterrissage, y compris si le script est interrompu.
        cf.land(targetHeight=0.04, duration=LAND_TIME)
        time_helper.sleep(LAND_TIME + 0.5)


if __name__ == "__main__":
    main()
