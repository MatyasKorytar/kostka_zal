let x = randint(1, 6)
let y = randint(1, 10)
function on_forever() {
    
    x = randint(1, 6)
    input.onButtonPressed(Button.A, function on_button_pressed_a() {
        
    })
    input.onGesture(Gesture.Shake, function on_gesture_shake() {
        
    })
    if (input.isGesture(Gesture.Shake)) {
        x = 1
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
        `)
        x = 2
        basic.showLeds(`
        . . . . .
        . . # . .
        . . . . .
        . . # . .
        . . . . .
        `)
        x = 3
        basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        `)
        x = 4
        basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        `)
        x = 5
        basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        `)
        x = 6
        basic.showLeds(`
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
        
        
        y = randint(1, 10)
        input.onButtonPressed(Button.B, function on_button_pressed_b() {
            
        })
        input.onGesture(Gesture.Shake, function on_gesture_shake() {
            
        })
        y == 1
        basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
        y == 2
        basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . . . .
        `)
        y == 3
        basic.showLeds(`
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        `)
        y == 4
        basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        `)
        y == 5
        basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        `)
        y == 6
        basic.showLeds(`
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
        y == 7
        basic.showLeds(`
        . . . . .
        . # . # .
        . # # # .
        . # . # .
        . . . . .
        `)
        y == 8
        basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # . # .
        . . . . .
        `)
        y == 9
        basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
        y == 10
        basic.showLeds(`
        . # . # .
        . # # # .
        . # . # .
        . # # # .
        `)
    }
    
}

