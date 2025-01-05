איש = 0
שחקן = 0

def on_pin_pressed_p0():
    global איש
    איש = 1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global שחקן
    שחקן = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global איש
    איש = 2
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global שחקן
    שחקן = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global שחקן
    שחקן = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global איש
    איש = 3
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_forever():
    if שחקן == 1:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    if שחקן == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    if שחקן == 3:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
    if איש == 1:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    if איש == 2:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    if איש == 3:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
basic.forever(on_forever)
