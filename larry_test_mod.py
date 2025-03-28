import turtle
t = turtle.Turtle()

## Variables
foyer_width = 400
foyer_height = 200
study_width = 100
study_height = 150
documents_width = 100
documents_height = 150
movie_width = 100
movie_height = 150
door_width = 10
door_height = 30
forw = 100   

def draw_room(t, room_type):
    """
    General function to draw a room rectangle with a label.
    """ 
    if room_type == "F":
        width = foyer_width
        height = foyer_height
        x = -foyer_width / 2
        y = foyer_height / 2
        label = "Foyer"
        color = "lightgrey"

    elif room_type == "S":
        width = study_width
        height = study_height
        x = -foyer_width / 2 - study_width
        y = foyer_height / 2 - (foyer_height / 2 - study_height / 2)
        label = "Study"
        color = "lightblue"
    
    elif room_type == "M":
        width = movie_width
        height = movie_height
        x = foyer_width / 2
        y = foyer_height / 2 - (foyer_height / 2 - movie_height / 2)
        label = "Movie"
        color = "lightcoral"

    elif room_type == "D":
        width = documents_width
        height = documents_height
        x = -documents_width / 2
        y = foyer_height / 2 + documents_height 
        label = "Documents"
        color = "lightgreen"
    
    else:
        print('Invalid room type')
        return

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    
    for _ in range(2):  # Draw the rectangle
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

    # Add label in the center of the room
    t.penup()
    t.goto(x + width / 2, y - height / 2)
    t.write(label, align="center", font=("Arial", 12, "bold"))

def draw_door(t, door_type):
    
    if door_type == "S":
        width = door_width
        height = door_height
        x = - foyer_width / 2
        y = - door_height / 2
        label = "S"
    
    elif door_type == "M":
        width = door_width
        height = door_height
        x = (foyer_width / 2) - 10  # "-10" is just for percise placing
        y = - door_height / 2
        label = "M"

    elif door_type == "D":
        width = door_height
        height = door_width
        x = (- door_width / 2) - 10  # "-10" is just for percise placing
        y = foyer_height / 2
        label = "D"
    
    elif door_type == "F":
        width = door_height
        height = door_width
        x = (- door_width / 2) - 10
        y = (foyer_height / 2) - 190
        label = ""

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("saddle brown")
    t.begin_fill()
    
    for _ in range(2):  # Draw the door rectangle
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

      # Add label in the center of the door
    t.penup()
    if door_type == "D":  # For horizontal door "D"
        t.goto(x + width / 2, (y - height / 2) - 5)
    else:  # For vertical doors "S" and "M"
        t.goto((x + width / 2) + 2, y - height / 2)

    t.write(label, align="center", font=("Arial", 8, "bold"))

def draw_secret_tunnel(t):
    # Coordinates for the right side of the movie room and left side of the study room
    movie_right_x = (foyer_width / 2 + movie_width) - 50
    movie_right_y = (foyer_height / 2 - (foyer_height / 2 - movie_height / 2) - movie_height / 2) + 75
    study_left_x = (-foyer_width / 2 - study_width) + 50
    study_left_y = (foyer_height / 2 - (foyer_height / 2 - study_height / 2) - study_height / 2) + 75

    # Draw the secret passage avoiding the used portions and occupied areas.
    t.penup()
    t.goto(movie_right_x, movie_right_y)
    t.pendown()
    t.pencolor("dark gray")
    
    # Move up to avoid the movie room and then move left to avoid the foyer and finally move down to reach the left side of the study room.
    t.goto(movie_right_x, foyer_height/2 + documents_height + door_width) 
    t.goto(study_left_x, foyer_height/2 + documents_height + door_width) 
    t.goto(study_left_x, study_left_y)
