from msvcrt import getch

escapeKey = b'\x1b'
spaceKey = b' '
oneKey = b'1'

while True:
    key = getch()

    print(key)

    if key == spaceKey:
        print("space pushed")

    if key == oneKey:
        print("one is pushed")

    if key == escapeKey:
        print("escape key pressed")
        break


