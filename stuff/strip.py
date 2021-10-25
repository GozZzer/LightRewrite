from typing import Optional
from enum import Enum

from driver.apa102 import APA102


class PROGRAM(Enum):
    """Current Working Programs"""
    NONE = 0


class LightStrip(APA102):
    """
    Overworked Driver for APA102
    (c) Daniel Pfurner
    """

    def __init__(self, *args, **kwargs):
        # Includes the program which is running at my led stripes of my bed
        self.bed_program: Optional[str] = None
        # If the bed LED are enabled
        self.bed: bool = False

        # Includes the program which is running at my led stripes of my table
        self.table_program: Optional[str] = None
        # If the table LED are enabled
        self.table: bool = False

        # The Number of LED`s at the table (0-110)
        self.num_table: int = 110

        # The Number of LED`s at the bed (111-288)
        self.num_bed: int = 177

        super().__init__(num_led=177, *args, **kwargs)
