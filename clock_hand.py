import pyglet


window = pyglet.window.Window(width=1000, height=1000, caption="Pendulum")


# white background
pyglet.gl.glClearColor(1, 1, 1, 1)

BLACK = (0, 0, 0, 255)


pin_position = (window.width // 2, window.height // 2)
ball_radius = 10
line_lenght = 100
line_width = 9
rotation_clockwise = 1  # 1 clockwise, -1 counter-clockwise
initial_rotation_speed = rotation_speed = 360 / 60  # deg/sec
speed_increment = 60 / 60  # increase 60 deg/sec


batch = pyglet.graphics.Batch()
pin = pyglet.shapes.Circle(
    pin_position[0],
    pin_position[1],
    radius=ball_radius // 2,
    batch=batch,
    color=BLACK,
)
line = pyglet.shapes.Rectangle(
    x=0, y=0, width=line_lenght, height=line_width, color=BLACK, batch=batch
)
line.anchor_position = (0, line_width // 2 + 1)
line.position = pin_position
#
# foreground = pyglet.graphics.Group(order=1)

fps_display = pyglet.window.FPSDisplay(window=window)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_release(symbol, modifiers):
    global rotation_speed, rotation_clockwise

    # ESCAPE exists the symulation
    if symbol == pyglet.window.key.ESCAPE:
        raise (SystemExit(0))
    elif symbol == pyglet.window.key.LEFT:
        rotation_clockwise = 1
    elif symbol == pyglet.window.key.RIGHT:
        rotation_clockwise = -1
    elif symbol == pyglet.window.key.UP:
        rotation_speed += speed_increment
    elif symbol == pyglet.window.key.UP:
        rotation_speed -= speed_increment
    elif symbol == pyglet.window.key.SPACE:
        rotation_speed = initial_rotation_speed


def update_sim(dt):
    line.rotation = line.rotation + dt * rotation_speed * rotation_clockwise


if __name__ == "__main__":
    pyglet.clock.schedule_interval_soft(update_sim, 1 / 60.0)
    pyglet.app.run()
