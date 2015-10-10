#find and search
def find_search():
    go_2_wall()
    follow_wall()

#get to wall
def go_2_wall():
    turn_left()
    move()#find and search
def find_search():
    go_2_wall()
    follow_wall()

#get to wall
def go_2_wall():
    turn_left()
    move()
    if not front_is_clear():
        turn_right()

#follow wall
def follow_wall():
        while not left_is_clear():
            move()
            if  left_is_clear():
                turn_left()
                move()
            
            if not front_is_clear():
                if not right_is_clear():
                    turn_left()
                    move()
                if right_is_clear():
                    if left_is_clear():
                        turn_left()
                        move()
                    else:
                        turn_right()
                        move()
                        turn_left()
                        move()
            
            
            
        
##exitHome
def exitHome():
    face_north()
    go_outside()
    exit_vest()
    #turn_off()
##turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
##face North 
def face_north():
        while not facing_north():
            turn_left()
##find vestibule
def go_outside():
    while not left_is_clear():
        
        if right_is_clear():
            if not front_is_clear():
                turn_right()
            move()
        else:
            move()
#Exit Vestibule
def exit_vest():
    if not right_is_clear():
        move()
    else:
        turn_left()
        move()
    if not left_is_clear():
        move()
        turn_left()
        move()

def main ():
    exitHome()
    find_search()
    turn_off()
main()
    if not front_is_clear():
        turn_right()

#follow wall
def follow_wall():
    while not left_is_clear():
        for i in range(4):
            while not left_is_clear():
                move()
            turn_rigt()
            move()


##exitHome
def exitHome():
    face_north()
    go_outside()
    exit_vest()
    turn_off()
##turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()   
##face North 
def face_north():
        while not facing_north():
            turn_left()
##find vestibule
def go_outside():
    while not left_is_clear():
        
        if right_is_clear():
            if not front_is_clear():
                turn_right()
            move()
        else:
            move()
#Exit Vestibule
def exit_vest():
    if not right_is_clear():
        move()
    else:
        turn_left()
        move()
    if not left_is_clear():
        move()
        turn_left()
        move()
