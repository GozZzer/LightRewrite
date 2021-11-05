from typing import Optional, List
from enum import Enum

from driver.apa102 import APA102
import colour


class PROGRAM(Enum):
    """Current Working Programs"""
    NONE = 0


class STRIPE(Enum):
    """All my Stripes"""
    TABLE = (0, 110)
    T = TABLE
    BED = (111, 288)
    B = BED
    ALL = (0, 288)
    A = ALL


class LightStrip(APA102):
    """
    Overworked Driver for APA102
    (c) Daniel Pfurner
    """

    def __init__(self, *args, **kwargs):
        self.bed = self.Bed()
        self.table = self.Table()

        # The Number of LED`s at the table (0-110)
        self.num_table: int = 110

        # The Number of LED`s at the bed (111-288)
        self.num_bed: int = 177

        super().__init__(num_led=177, *args, **kwargs)

    class Bed:
        def __init__(self):
            self.numbers = [_ for _ in range(111, 288)]
            self.enabled: bool = False
            self.colors: List[colour.Color] = []
            self.rotate = False
            self.rotation = 111
            self.grade = False
            self.brightness = 100

    class Table:
        def __init__(self):
            self.numbers = [_ for _ in range(0, 110)]
            self.enabled: bool = False
            self.colors: List[colour.Color] = []
            self.rotate = False
            self.rotation = 0
            self.grade = False
            self.brightness = 100
