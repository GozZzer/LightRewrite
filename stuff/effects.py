import time
import keyboard
from colour import Color
import colour
from strip import LightStrip


class Effects:
    def __init__(self, strip: LightStrip = None):
        self.strip = strip
        self.bed = self.strip.bed
        self.table = self.strip.table
        self.running = True
        self.edit_bed = False
        self.edit_table = False
        self.edit_all = False

    def loop(self):
        while self.running:
            if self.edit_bed or self.edit_all:
                if self.edit_bed:
                    print("Edit Bed")
                else:
                    print("Edit All")
                if keyboard.is_pressed("d"):
                    self.bed.enabled = not self.bed.enabled
                elif keyboard.is_pressed("r"):
                    self.bed.rotate = not self.bed.rotate
                    self.edit_bed = False
                elif keyboard.is_pressed("g"):
                    self.bed.grade = not self.bed.grade
                    self.edit_bed = False
                elif keyboard.is_pressed("c"):
                    self.bed.color.append(Color(input("Color: ")))
                    self.edit_bed = False
            if self.edit_table or self.edit_all:
                if self.edit_table:
                    print("Edit Table")
                if keyboard.is_pressed("d"):
                    self.table.enabled = not self.table.enabled
                elif keyboard.is_pressed("t"):
                    self.table.rotate = not self.table.rotate
                    self.edit_table = False
                    self.edit_all = False
                elif keyboard.is_pressed("g"):
                    self.table.grade = not self.table.grade
                    self.edit_table = False
                    self.edit_all = False
                elif keyboard.is_pressed("c"):
                    self.table.color.append(Color(input("Color: ")))
                    self.edit_table = False
                    self.edit_all = False
            else:
                if keyboard.is_pressed("q"):
                    self.running = False
                elif keyboard.is_pressed("t"):
                    self.edit_table = True
                    self.edit_bed = False
                    self.edit_all = False
                elif keyboard.is_pressed("b"):
                    self.edit_table = False
                    self.edit_bed = True
                    self.edit_all = False
                elif keyboard.is_pressed("a"):
                    self.edit_table = False
                    self.edit_bed = False
                    self.edit_all = True
                else:
                    # Bed
                    if self.bed.enabled:
                        colors = []
                        if self.bed.grade:
                            if len(self.bed.color) < 1:
                                self.bed.color.append(Color("red"))
                            colors = self.bed.color[0].range_to(self.bed.color[1], len(self.bed.numbers))
                        if self.bed.rotate:
                            if self.bed.rotation > self.bed.numbers[-1]:
                                self.bed.rotation = self.bed.numbers[0]
                            else:
                                self.bed.rotation += 1
                        for led in self.bed.numbers:
                            if not colors:
                                self.strip.set_pixel(
                                    self.bed.numbers.index(led),
                                    self.bed.colors[0].get_red(),
                                    self.bed.colors[0].get_green(),
                                    self.bed.colors[0].get_blue(),
                                    self.bed.brightness
                                )
                            else:
                                self.strip.set_pixel(
                                    self.bed.numbers.index(led),
                                    colors[self.bed.numbers.index(led)].get_red(),
                                    colors[self.bed.numbers.index(led)].get_green(),
                                    colors[self.bed.numbers.index(led)].get_blue(),
                                    self.bed.brightness
                                )
                            if self.bed.rotate:
                                cutoff = 4 * (self.bed.rotation % len(self.bed.numbers))
                                self.bed_leds = self.strip.leds[len(self.table.numbers):]
                                self.bed_leds = self.bed_leds[cutoff:] + self.bed_leds[:cutoff]
                                self.strip.leds = self.strip.leds[:len(self.bed.numbers)] + self.bed_leds
                    if self.table.enabled:
                        colors = []
                        if self.table.grade:
                            if len(self.table.color) < 1:
                                self.table.color.append(Color("red"))
                            colors = self.table.color[0].range_to(self.table.color[1], len(self.table.numbers))
                        if self.table.rotate:
                            if self.table.rotation > self.table.numbers[-1]:
                                self.table.rotation = self.table.numbers[0]
                            else:
                                self.table.rotation += 1
                        for led in self.table.numbers:
                            if not colors:
                                self.strip.set_pixel(
                                    self.table.numbers.index(led),
                                    self.table.colors[0].get_red(),
                                    self.table.colors[0].get_green(),
                                    self.table.colors[0].get_blue(),
                                    self.table.brightness
                                )
                            else:
                                self.strip.set_pixel(
                                    self.table.numbers.index(led),
                                    colors[self.table.numbers.index(led)].get_red(),
                                    colors[self.table.numbers.index(led)].get_green(),
                                    colors[self.table.numbers.index(led)].get_blue(),
                                    self.table.brightness
                                )
                            if self.table.rotate:
                                cutoff = 4 * (self.table.rotation % len(self.table.numbers))
                                self.table_leds = self.strip.leds[len(self.table.numbers):]
                                self.table_leds = self.table_leds[cutoff:] + self.table_leds[:cutoff]
                                self.strip.leds = self.strip.leds[:len(self.table.numbers)] + self.table_leds
                    self.strip.show()
            time.sleep(0.2)
        else:
            self.strip.clear_strip()

    def enable(self):
        if self.running is False:
            self.running = True

    def disable(self):
        if self.running is True:
            self.running = False
