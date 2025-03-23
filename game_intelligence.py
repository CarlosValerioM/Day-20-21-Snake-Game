# Constants for movement directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Constant for movement distance
MOVE_DISTANCE = 20


def move_up(head, xposition, yposition):
    """Moves the snake upwards if it's not currently moving down."""
    if head.heading() != DOWN:  # Prevents moving in the opposite direction
        head.setheading(UP)
        head.goto(xposition, yposition + MOVE_DISTANCE)


def move_down(head, xposition, yposition):
    """Moves the snake downwards if it's not currently moving up."""
    if head.heading() != UP:
        head.setheading(DOWN)
        head.goto(xposition, yposition - MOVE_DISTANCE)


def move_left(head, xposition, yposition):
    """Moves the snake to the left if it's not currently moving right."""
    if head.heading() != RIGHT:
        head.setheading(LEFT)
        head.goto(xposition - MOVE_DISTANCE, yposition)


def move_right(head, xposition, yposition):
    """Moves the snake to the right if it's not currently moving left."""
    if head.heading() != LEFT:
        head.setheading(RIGHT)
        head.goto(xposition + MOVE_DISTANCE, yposition)


def check_collision_front(head, collision_object):
    """
    Checks if the snake's head is about to collide with a given object.

    Args:
        head: The snake's head (turtle object).
        collision_object: The object to check for collision.

    Returns:
        True if the distance between the head and the object is less than MOVE_DISTANCE, False otherwise.
    """

    # Get current position of the snake's head
    x, y = head.xcor(), head.ycor()

    # Adjust position based on movement direction
    heading = head.heading()
    if heading == RIGHT:
        x += MOVE_DISTANCE
    elif heading == UP:
        y += MOVE_DISTANCE
    elif heading == LEFT:
        x -= MOVE_DISTANCE
    elif heading == DOWN:
        y -= MOVE_DISTANCE

    # Check if the head is close enough to the collision object
    return head.distance(collision_object) < MOVE_DISTANCE