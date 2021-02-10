import numpy as np


CONVERTER = np.uint8([
    0,    # unlabeled
    0,    # building
    0,    # fence
    0,    # other
    1,    # ped
    0,    # pole
    2,    # road line
    3,    # road
    4,    # sidewalk
    0,    # vegetation
    5,    # car
    0,    # wall
    0,    # traffic sign
    0,    # sky
    0,    # ground
    0,    # bridge
    0,    # railtrack
    0,    # guardrail
    0,    # trafficlight
    0,    # static
    0,    # dynamic
    0,    # water
    0,    # terrain
    6,
    7,
    8,
    ])


COLOR = np.uint8([
    (0, 0, 0),  # 0=Unlabeled
    # 1=Building, 2=Fence, 3=Other   , 4=Pedestrian, 5=Pole
    (70, 70, 70),
    (100, 40, 40),
    (55, 90, 80),
    (220, 20, 60),
    (153, 153, 153),
    # 6=RoadLine, 7=Road, 8=SideWalk, 9=Vegetation, 10=Vehicles
    (157, 234, 50),
    (128, 64, 128),
    (244, 35, 232),
    (107, 142, 35),
    (0, 0, 142),
    # 11=Wall, 12=TrafficSign, 13=Sky, 14=Ground, 15=Bridge
    (102, 102, 156),
    (220, 220, 0),
    (70, 130, 180),
    (81, 0, 81),
    (150, 100, 100),
    # 16=RailTrack, 17=GuardRail, 18=TrafficLight, 19=Static, 20=Dynamic
    (230, 150, 140),
    (180, 165, 180),
    (250, 170, 30),
    (110, 190, 160),
    (170, 120, 50),
    # 21=water, 22=terrain
    (45, 60, 150),
    (145, 170, 100),
        ])
