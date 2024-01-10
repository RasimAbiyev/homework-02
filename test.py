# import rotatescreen
# import time


# screen = rotatescreen.get_primary_display()
# start_pos = screen.current_orientation

# for i in range(4):
#     pos = abs((start_pos - i*90) % 360)
#     screen.rotate_to(pos)
#     time.sleep(1)

import calendar

yy = 1970
mm = 1
print(calendar.month(yy, mm))


# from colorama import Fore
# def heart_shape(msg="Merry Christmas"):
#     lines = []
#     for y in range(15, -15, -1):
#         line = ""
#         for x in range(-30, 30):
#             f = ((x * 0.05) ** 2 + (y * 0.10) ** 2 -1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
#             line += msg[(x - y) % len(msg)] if f <= 0 else " "
#         lines.append(line)
#     print(Fore.RED+"\n".join(lines))
#     print(Fore.GREEN+msg)
# heart_shape()

