import turtle
from larry_test_mod import *


# Create and customize the turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(15)

# Draw the Foyer
draw_room(t, "F")

# Draw doors
draw_door(t, "S")
draw_door(t, "D")
draw_door(t, "M")
draw_door(t, "F")

# Create one player turtle
turt_player = turtle.Turtle()
turt_player.hideturtle()
turt_player.speed(1)
turt_player.shape("circle")
turt_player.shapesize(stretch_wid=0.5, stretch_len=0.5)
turt_player.penup()
turt_player.left(90)
turt_player.goto(0, -30 - forw)
turt_player.showturtle()
turt_player.forward(forw)
  
current_room = "foyer"  # Start in the foyer
game_over = False
win_phrase = "Let me out now!"
lose_phrase = "I will never escape!"    
valid_phrases = [win_phrase, lose_phrase]
valid_choices = ["s", "d", "m"]

# Get the player's name once
name = turtle.textinput("Name", "Please enter your name:")

while not game_over:

    if current_room == "foyer":
        # Ask for the door choice only when in the foyer
        door_choice = turtle.textinput(
            f"Hello {name}, you are in the foyer.",
            "The door you came through will not budge...\nEnter the door you would like to enter:\nS. for Study\nD. for Documents\nM. for Movie"
        )
       
       
        # Move to the chosen room based on the door choice
        if door_choice == "s":
            current_room = "study"
            draw_room(t, "S")
            turt_player.goto(-210, -30)  # Position in the Study room
       
        elif door_choice == "d":
            current_room = "documents room"
            draw_room(t, "D")
            turt_player.goto(0, 110)  # Position in the Documents room
       
        elif door_choice == "m":
            current_room = "movie room"
            draw_room(t, "M")
            turt_player.goto(210, -30)  # Position in the Movie room
        prev_room = "foyer"

    ### GAME LOGIC FOR EACH ROOM ###

    # STUDY
    if current_room == "study":
        leave_study = False
        while not leave_study:
            if prev_room == 'movie room':
                u_input = turtle.textinput('The door to the Foyer is locked!', 'To escape, you must type the message you saw in the movie room\nYou get 5 guesses! ')
                count = 5
                ## checks for 5 tries to give a valid guess
                while count > 0:
                    count -= 1
                    if count == 0:
                        turtle.textinput('You could not guess the phrase!', 'GAME OVER\nPress any key to continue.')
                        game_over = True
                        leave_study = True
                    else:
                        if u_input.lower() == win_phrase.lower():
                            turtle.textinput("Congratulations!", "You have escaped! \nPress any key to end the game!")
                            leave_study = True
                            game_over = True
                            # Add turtle code to escape
                            turtle.exitonclick()
                        elif u_input.lower() == lose_phrase.lower():
                            turtle.textinput("Game Over!", "You lose :P \nPress any key to end the game!")
                            leave_study = True
                            game_over = True
                            # Add turtle code to indicate game over
                            turtle.exitonclick()

                        u_input = turtle.textinput('The door to the Foyer is locked!', f'To escape, you must type the message you saw in the movie room\nYou get {str(count)} guesses! ')

            elif prev_room == 'foyer':
                u_input = turtle.textinput("You are in the Study", "This room has a pen, paper, calculator, and ledger.\nHowever ...YOU CAN NOT ESCAPE!\nYou must go back to the Foyer the way you came.\nPress any key to continue.")
                turt_player.goto(0,-30)
                current_room = "foyer"
                prev_room = 'study'
                leave_study = True


    # DOCUMENTS
    elif current_room == "documents room":
        leave_documents = False
        while not leave_documents:
            u_input = turtle.textinput(
                "Here is the Documents Room",
                "The door behind you is open. This room has a will and a car title.\n"
                "Choose an option:\n1. Read will\n2. View car title\n3. Leave room"
            )
            if u_input == "1":
                turtle.textinput(
                    "Here's the will",
                    "Once my soul has left this world, all my belongings will then be owned by my brother Andy <3\n\nPress any key to continue."
                )
            elif u_input == '2':
                turtle.textinput(
                    "Here's the Car title",
                    "2014 Toyota Prius\nLicense: BW4N224\nOwner: AJ Leigh\nOriginal State: Texas\n"
                    "Date Transferred to Owner: January 5, 2018\n\nPress any key to continue."
                )
            elif u_input == '3':
                leave_documents = True
                current_room = "foyer"
                turt_player.goto(0, -50)  # Return to foyer position


    # MOVIE
    elif current_room == "movie room":
        leave_movie = False
        while not leave_movie:
            u_input = turtle.textinput(
                "You are in the Movie Room.",
                "The door to the foyer is now locked. There are two movies: Family Vacation and Watch Me Now.\n"
                "Which movie will you watch:\n1. Family Vacation\n2. Watch Me Now\n3. Leave room"
            )
            if u_input == "1":
                turtle.textinput("Movie Choice", "Movie phrase: 'I will never escape!'"
                    "\nA secret passage opens up, and you go through it!\nPress any key to continue.")
                # SECRET TUNNEL!!!
                draw_secret_tunnel(t)
                current_room = "study"
                draw_room(t, "S")
                # take secret passage to study
                movie_right_x = (foyer_width / 2 + movie_width) - 50
                movie_right_y = (foyer_height / 2 - (foyer_height / 2 - movie_height / 2) - movie_height / 2) + 75
                study_left_x = (-foyer_width / 2 - study_width) + 50
                study_left_y = (foyer_height / 2 - (foyer_height / 2 - study_height / 2) - study_height / 2) + 75

                # Draw the secret passage avoiding the used portions and occupied areas.
                turt_player.penup()
                turt_player.goto(movie_right_x, movie_right_y)
                
                # Move up to avoid the movie room and then move left to avoid the foyer and finally move down to reach the left side of the study room.
                turt_player.goto(movie_right_x, foyer_height/2 + documents_height + door_width) 
                turt_player.goto(study_left_x, foyer_height/2 + documents_height + door_width) 
                turt_player.goto(study_left_x, (study_left_y) - 10)

                ## update rooms
                prev_room = "movie room"
                current_room = 'study'
                leave_movie = True

            elif u_input == "2":
                turtle.textinput("Movie Choice", "Movie phrase: 'Let me out now!'\nA secret passage opens up, and you go through it!\nPress any key to continue.")
               
                draw_secret_tunnel(t)
                draw_room(t, "S")
                # SECRET TUNNEL!!!
                draw_secret_tunnel(t)
                draw_room(t, "S")
                # take secret passage to study
                movie_right_x = (foyer_width / 2 + movie_width) - 50
                movie_right_y = (foyer_height / 2 - (foyer_height / 2 - movie_height / 2) - movie_height / 2) + 75
                study_left_x = (-foyer_width / 2 - study_width) + 50
                study_left_y = (foyer_height / 2 - (foyer_height / 2 - study_height / 2) - study_height / 2) + 75

                # Draw the secret passage avoiding the used portions and occupied areas.
                turt_player.penup()
                turt_player.goto(movie_right_x, movie_right_y)
                
                # Move up to avoid the movie room and then move left to avoid the foyer and finally move down to reach the left side of the study room.
                turt_player.goto(movie_right_x, foyer_height/2 + documents_height + door_width) 
                turt_player.goto(study_left_x, foyer_height/2 + documents_height + door_width) 
                turt_player.goto(study_left_x, study_left_y)
                
                ## update rooms
                leave_movie = True
                prev_room = "movie room"
                current_room = 'study'
           
            elif u_input.lower() == "3":
                turtle.textinput("OH MY !!", "This door is locked!! what shall we do next!!\nPress any key to continue")
           
            else:
                print("Invalid choice. Try again.")

# Keep the window open
turtle.done()
