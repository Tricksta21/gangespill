tiere = 0
svar = 0
enere = 0
produkt = 0
faktor1 = 0
faktor2 = 0

def on_button_pressed_a():
    global tiere
    tiere += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global svar
    svar = tiere * 10 + enere
    if True:
        basic.show_string("" + str((produkt)))
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_string("" + str((produkt)))
        basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global enere
    enere += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global tiere, enere, svar, produkt, faktor1, faktor2
    tiere = 0
    enere = 0
    svar = 0
    produkt = 0
    faktor1 = randint(0, 10)
    faktor2 = randint(0, 10)
    basic.show_string("" + str(faktor1) + "x" + str(faktor2) + "=")
    produkt = faktor1 * faktor2
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
