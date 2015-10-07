


##exitHome
def exitHome():
    face_north()
    exit()
    turn_off
##turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
##face North 
def face_north():
    if front_is_clear():
        exit_vest()
    while not facing_north():

        turn_left()
##find vestibule
def exit():
    if left_is_clear():
        turn_left()
        exit_vest()
    while right_is_clear():
        if not front_is_clear():
            turn_right()
        move()
    
    exit_vest()
##Exit Vestibule   
def exit_vest():
    
    move()
    if not left_is_clear():
        move()
    
exitHome()




