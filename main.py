x = randint(1, 6)
y = randint(1, 10)
def on_forever():
    global x
    x = randint(1, 6)
    def on_button_pressed_a():
        pass
    input.on_button_pressed(Button.A, on_button_pressed_a)
    def on_gesture_shake():
            pass
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
    if input.is_gesture(Gesture.SHAKE):
        x = 1
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
        """)
        x = 2
        basic.show_leds("""
        . . . . .
        . . # . .
        . . . . .
        . . # . .
        . . . . .
        """)
        x = 3
        basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
        x = 4
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
        x = 5
        basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
        x = 6
        basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        """)
        pass
        global y
        y = randint(1, 10)
        def on_button_pressed_b():
            pass
        input.on_button_pressed(Button.B, on_button_pressed_b)
        def on_gesture_shake():
            pass
        input.on_gesture(Gesture.SHAKE, on_gesture_shake)
        y == 1
        basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
        y == 2
        basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . . . .
        """)
        y == 3
        basic.show_leds("""
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        """)
        y == 4
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
        y == 5
        basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
        y == 6
        basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        """)
        y == 7
        basic.show_leds("""
        . . . . .
        . # . # .
        . # # # .
        . # . # .
        . . . . .
        """)
        y == 8
        basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # . # .
        . . . . .
        """)
        y == 9
        basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
        y == 10
        basic.show_leds("""
        . # . # .
        . # # # .
        . # . # .
        . # # # .
        """)

