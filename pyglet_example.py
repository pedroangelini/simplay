import pyglet

window = pyglet.window.Window()


def create_label(x=window.width // 2, y=window.height // 2):
    label = pyglet.text.Label(
        "Hello, world",
        font_name="Times New Roman",
        font_size=36,
        x=x,
        y=y,
        anchor_x="center",
        anchor_y="center",
    )
    return label


x = 0
y = 0
speed = 10


@window.event
def on_draw():
    global x, y, speed
    window.clear()
    x = x + speed
    y = y + speed
    if x > window.width:
        x = 0
    if y > window.height:
        y = 0
    # print(f"{x = }, {y = }")
    create_label(x, y).draw()


pyglet.app.run()
