let איש = 0
let שחקן = 0
input.onPinPressed(TouchPin.P0, function () {
    איש = 1
})
input.onButtonPressed(Button.A, function () {
    שחקן = 1
})
input.onPinPressed(TouchPin.P2, function () {
    איש = 2
})
input.onButtonPressed(Button.AB, function () {
    שחקן = 3
})
input.onButtonPressed(Button.B, function () {
    שחקן = 2
})
input.onPinPressed(TouchPin.P1, function () {
    איש = 3
})
basic.forever(function () {
    if (שחקן == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    if (שחקן == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    }
    if (שחקן == 3) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
    if (איש == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    if (איש == 2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    }
    if (איש == 3) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
})
