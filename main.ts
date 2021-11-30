// Whenever the program is turned on, it will set one of the variable that I set up(Walk_button) to 0 and another variable (malfunction) to 0 as well.
function green () {
    range2 = strip.range(2, 1)
    range2.showColor(neopixel.colors(NeoPixelColors.Green))
}
// When ever you press the A button, a variable that I set up will increase by 1 and it will show the led which is full.
input.onButtonPressed(Button.A, function () {
    Walk_button += 1
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    green()
    yellow()
})
function music2 () {
    music.playTone(659, music.beat(BeatFraction.Half))
    music.playTone(554, music.beat(BeatFraction.Half))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Half))
}
input.onButtonPressed(Button.AB, function () {
    control.reset()
})
// Whenever you press the B button, it will simply increase another variable that I set by 1.
input.onButtonPressed(Button.B, function () {
    malfunction += 1
})
function yellow () {
    range2 = strip.range(1, 1)
    range2.showColor(neopixel.colors(NeoPixelColors.Yellow))
}
function red () {
    range2 = strip.range(0, 1)
    range2.showColor(neopixel.colors(NeoPixelColors.Red))
}
function black () {
    range2 = strip.range(1, 1)
    range2.showColor(neopixel.colors(NeoPixelColors.Black))
    range2 = strip.range(2, 1)
    range2.showColor(neopixel.colors(NeoPixelColors.Black))
    range2 = strip.range(0, 1)
    range2.showColor(neopixel.colors(NeoPixelColors.Black))
}
function sensor () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    control.waitMicros(2)
    pins.digitalWritePin(DigitalPin.P12, 1)
    control.waitMicros(10)
    pins.digitalWritePin(DigitalPin.P12, 0)
    distance = pins.pulseIn(DigitalPin.P13, PulseValue.High) / 58
}
let distance = 0
let range2: neopixel.Strip = null
let malfunction = 0
let Walk_button = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P0, 4, NeoPixelMode.RGB)
strip.setBrightness(40)
// This is to make the code to run forever, because it is always true therefore it will run forever.
while (true) {
    // This code will only run and loop if the variable (Walk_button) is 0.
    while (Walk_button == 0) {
        // This is scenario 1, this is for normal mode for a light.
        if (malfunction == 0) {
            green()
            basic.pause(3000)
            // This is a loop to create a blinking effect, it will shut off the pin for 0.1sec and turn it on for 0.1sec and this will loop for 3 times.
            for (let index = 0; index < 3; index++) {
                range2 = strip.range(2, 1)
                range2.showColor(neopixel.colors(NeoPixelColors.Green))
                basic.pause(100)
                black()
                basic.pause(100)
            }
            black()
            yellow()
            basic.pause(2000)
            black()
            red()
            basic.pause(2000)
            black()
        } else if (malfunction == 1) {
            yellow()
            basic.pause(200)
            black()
            basic.pause(200)
        } else if (malfunction == 2) {
            red()
            basic.pause(200)
            black()
            basic.pause(200)
        } else {
            // This is the last scenario there is, if you press the B button more than twice it will just reset the variable so it will run the normal street light.
            malfunction = 0
        }
    }
    // This is the other loop, if you press the A button which is the variable Walk_button. it runs if the variable doesn't equal 0. The code is the same except there are some tiny changes.
    while (Walk_button != 0) {
        // It will show a person icon so that it means it means that you can walk.
        basic.showLeds(`
            . . # . .
            . # # # .
            . # # # .
            . . # . .
            . # . # .
            `)
        green()
        for (let index = 0; index < 5; index++) {
            music2()
        }
        // After the icon shows up for a little bit, it will show a count down.
        for (let index3 = 0; index3 <= 9; index3++) {
            basic.showNumber(10 - index3)
        }
        // This is a loop to create a blinking effect, it will shut off the pin for 0.1sec and turn it on for 0.1sec and this will loop for 3 times.
        for (let index = 0; index < 3; index++) {
            range2 = strip.range(2, 1)
            range2.showColor(neopixel.colors(NeoPixelColors.Green))
            basic.pause(100)
            black()
            basic.pause(100)
        }
        basic.clearScreen()
        // After the green light turns of it will show a solid red icon to show stop walking. This will happen when the yellow/red light turns on.
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        yellow()
        basic.pause(2500)
        black()
        red()
        basic.pause(25000)
        for (let index = 0; index < 9; index++) {
            basic.showLeds(`
                . . # . .
                . # . . .
                # # # # #
                . # . . .
                . . # . .
                `)
            basic.pause(100)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            basic.pause(100)
        }
        // It will set the the variable to 0 so that it will run the other codes again
        Walk_button = 0
        // This will stop this loop so it will go to the other part of the code.
        break;
    }
}
control.inBackground(function () {
    if (malfunction != 0 && Walk_button != 0) {
        malfunction = 0
    }
})
