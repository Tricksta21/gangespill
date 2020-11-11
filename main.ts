let tiere = 0
let svar = 0
let enere = 0
let produkt = 0
let faktor1 = 0
let faktor2 = 0
input.onButtonPressed(Button.A, function () {
    tiere += 1
})
input.onButtonPressed(Button.AB, function () {
    svar = tiere * 10 + enere
    if (true) {
        basic.showString("" + produkt)
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showString("" + produkt)
        basic.showIcon(IconNames.Sad)
    }
})
input.onButtonPressed(Button.B, function () {
    enere += 1
})
input.onGesture(Gesture.Shake, function () {
    tiere = 0
    enere = 0
    svar = 0
    produkt = 0
    faktor1 = randint(0, 10)
    faktor2 = randint(0, 10)
    basic.showString("" + faktor1 + "x" + ("" + faktor2) + "=")
    produkt = faktor1 * faktor2
})
