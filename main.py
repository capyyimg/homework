# Whenever the program is turned on, it will set one of the variable that I set up(Walk_button) to 0 and another variable (malfunction) to 0 as well.
def green():
    global range2
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(3000)
    # This is a loop to create a blinking effect, it will shut off the pin for 0.1sec and turn it on for 0.1sec and this will loop for 3 times.
    for index in range(3):
        range2 = strip.range(2, 1)
        range2.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(100)
        black()
        basic.pause(100)
# When ever you press the A button, a variable that I set up will increase by 1 and it will show the led which is full.

def on_button_pressed_a():
    global Walk_button
    Walk_button += 1
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    green()
    yellow()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Whenever you press the B button, it will simply increase another variable that I set by 1.

def on_button_pressed_b():
    global malfunction
    malfunction += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def yellow():
    global range2
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.YELLOW))
def red():
    global range2
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.RED))
def black():
    global range2
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
def sensor():
    global distance
    pins.digital_write_pin(DigitalPin.P12, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P12, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P12, 0)
    distance = pins.pulse_in(DigitalPin.P13, PulseValue.HIGH) / 58
range2: neopixel.Strip = None
distance = 0
malfunction = 0
Walk_button = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 4, NeoPixelMode.RGB)
strip.set_brightness(40)
# This is to make the code to run forever, because it is always true therefore it will run forever.
while True:
    # This code will only run and loop if the variable (Walk_button) is 0.
    while Walk_button == 0:
        # This is scenario 1, this is for normal mode for a light.
        if malfunction == 0:
            green()
            black()
            yellow()
            basic.pause(2000)
            black()
            red()
            basic.pause(2000)
            basic.show_number(distance)
            black()
        elif malfunction == 1:
            yellow()
            basic.pause(200)
            black()
            basic.pause(200)
        elif malfunction == 2:
            red()
            basic.pause(200)
            black()
            basic.pause(200)
        else:
            # This is the last scenario there is, if you press the B button more than twice it will just reset the variable so it will run the normal street light.
            malfunction = 0
    # This is the other loop, if you press the A button which is the variable Walk_button. it runs if the variable doesn't equal 0. The code is the same except there are some tiny changes.
    while Walk_button != 0:
        # It will show a person icon so that it means it means that you can walk.
        basic.show_leds("""
            . . # . .
                        . # # # .
                        . # # # .
                        . . # . .
                        . # . # .
        """)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.pause(7000)
        # After the icon shows up for a little bit, it will show a count down.
        for index3 in range(10):
            basic.show_number(10 - index3)
        for index2 in range(3):
            pins.digital_write_pin(DigitalPin.P2, 0)
            basic.pause(100)
            pins.digital_write_pin(DigitalPin.P2, 1)
            basic.pause(100)
        basic.clear_screen()
        # After the green light turns of it will show a solid red icon to show stop walking. This will happen when the yellow/red light turns on.
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(2500)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(25000)
        pins.digital_write_pin(DigitalPin.P0, 0)
        for turns2 in range(9):
            basic.show_leds("""
                . . # . .
                                . # . . .
                                # # # # #
                                . # . . .
                                . . # . .
            """)
            basic.pause(100)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            basic.pause(100)
        # It will set the the variable to 0 so that it will run the other codes again
        Walk_button = 0
        # This will stop this loop so it will go to the other part of the code.
        break

def on_in_background():
    global malfunction
    if malfunction != 0 and Walk_button != 0:
        malfunction = 0
control.in_background(on_in_background)

def music2():
    music.play_tone(659, music.beat(BeatFraction.HALF))
    music.play_tone(554, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))