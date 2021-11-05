from stuff.strip import LightStrip
from stuff.effects import Effects
import time

stripe = LightStrip()

effects = Effects(stripe)
effects.loop()

print("Stopped Working!")

