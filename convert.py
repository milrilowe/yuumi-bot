#AHK returns hexadecimal values whereas I'd recorded all the constants as RGB values, so conversion necessary
from ahk import AHK

ahk = AHK()

def toRGB(self, x, y):
    ahk.pixel_get_color(x, y)
    h = ahk.pixel_get_color(x, y)
    h = h[2:]
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))