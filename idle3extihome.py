


##exitHome
def exitHome():
    face_north()
    find_vest()
    exit_vest()
    turn_off()
##turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
##face North 
    face_north():
        while not facing_north():
            turn_left()
##find vestibule
def find_vest():
    while front_is_clear():
        move()
        if  left_is_clear():
            turn_left()
            exit_vest()
         if not right_is_clear():
             exit_vest()     
    turn_right()
        if not right_is_clear():
            exit_vest()
##Exit Vestibule   
def exit_vest():
    move()
    if not left_is_clear():
        move()
        
    
