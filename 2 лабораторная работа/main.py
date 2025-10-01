import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "INIT":

        if True:
            state = "RIGHT"
            t.setheading(0)  # Разворот вправо
            return state, turn
        return state, turn

    if state == "RIGHT":
        t.forward(40)

        if turn > 2:
            state = "STOP"
            return state, turn

        if x >= 0:
            state = "DOWN1"
            t.setheading(270)
            return state, turn
        return state, turn

    if state == "DOWN1":
        t.forward(10)

        if y <= 0:
            state = "LEFT"
            t.setheading(180)
            return state, turn
        return state, turn

    if state == "LEFT":
        t.forward(40)

        if y <= 0:
            state = "DOWN2"
            t.setheading(270)
            return state, turn
        return state, turn

    if state == "DOWN2":
        t.forward(10)

        if y <= 0:
            state = "RIGHT"
            t.setheading(0)
            turn += 1
            return state, turn
        return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if __name__ == "__main__":
    draw()
