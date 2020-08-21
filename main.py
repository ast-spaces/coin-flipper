def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
    if Math.random_boolean():
        basic.show_icon(IconNames.SKULL)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)
