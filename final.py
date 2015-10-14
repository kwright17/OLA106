#OLA106 by Krestofer Wright, CSCI 1170-009, due 10/09/15
#Program ID: clearpapers.py  Clear NewsPapers from around the #house
#ARTHOR: Krestofer Wright
#INSTITUTION: MTSU
#REMARKS: Reeborg exits home, clears picks up newspapers from
#around his house, places all of them except one in vestibule
#then returns to bed (SouthWest corner) facing south with beeper
#in pocket.



def main():
    exitHome()
    search_find()
    depo_in_vest()
    go_to_bed()
    turn_off()

# Reeborg wakes up and exits home
def exitHome():
    face_north()
    find_vest()
    exit_vest()

#Reeborg makes right turn
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#face North
def face_north():
    while not facing_north():
        turn_left()
#Reeborg finds his vestibule
def find_vest():
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
####Reeborg Searches Perimiter

#Search Perimiter and pick up Beepers
def search_find():
    go_2_wall()
    follow_wall()

#Reeborg finds a wall after exiting vestibule
def go_2_wall():
    while on_beeper():
        pick_beeper()
    turn_left()
    move()
    while on_beeper():
         pick_beeper()
    if not front_is_clear():
        turn_right()
#follow wall and pick up beepers
def follow_wall():
    while not left_is_clear():
        while on_beeper():
            pick_beeper()
        move()
        if left_is_clear():
            while on_beeper():
                pick_beeper()
            turn_left()
            move()
        if not front_is_clear():
            if not right_is_clear():
                while on_beeper():
                    pick_beeper()
                turn_left()
                move()
            if right_is_clear():
                if left_is_clear():
                        while on_beeper():
                            pick_beeper()
                        turn_left()
                        move()
                else:
                    while on_beeper():
                        pick_beeper()
                    turn_right()
                    move()
                    while on_beeper():
                        
                        pick_beeper()
                    turn_left()
                    move()
       
#Deposits the newspapers into his vestibule
def depo_in_vest():
    while on_beeper():
        pick_beeper()
    turn_left()
    move()
    while carrying_beepers():
        put_beeper()
    pick_beeper()

#Reeborg takes his single newspaper to bed
def go_to_bed():
    if facing_south():
        while front_is_clear():
            move()
            if right_is_clear():
                turn_right()
                while front_is_clear():
                    move()
                turn_left()
    elif facing_north():
        move()
        turn_left()
        while front_is_clear():
            move()
            turn_left()
        if right_is_clear():
            turn_left()
    elif facing_west():
        while front_is_clear():
            move()
        turn_left()
        while front_is_clear():
            move()
    else:
        move()
        turn_right()
        while front_is_clear():
            move()
main()
       
   

       
