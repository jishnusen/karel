#!/usr/bin/env python
from board import Board, LogicException
import sys

# this needs to be smarter soon
if len(sys.argv) > 1:
    _board = Board(sys.argv[1])
else:
    _board = Board('levels/03.karelmap')

def _refresh(callback):
    def inner():
        res = callback()
        _board.draw()
        return res
    return inner

move = _refresh(_board.move)
turn_left = _refresh(_board.turn_left)
pick_beeper = _refresh(_board.pick_beeper)
put_beeper = _refresh(_board.put_beeper)
front_is_clear = _board.front_is_clear
right_is_clear = _board.right_is_clear
left_is_clear = _board.left_is_clear
beeper_is_present = _board.beeper_is_present
facing_north = _board.facing_north
facing_south = _board.facing_south
facing_east = _board.facing_east
facing_west = _board.facing_west

def execute(callback):
    try:
        _board.start_screen()
        _board.draw()
        callback()
        return callback
    except LogicException, e:
        _board.draw_exception(e)
    except Exception, e:
        raise e
    finally:
        _board.end_screen()

def run():
    """
    Funtions
    move = _refresh(_board.move) #Moves the robot forward one space!
    turn_left = _refresh(_board.turn_left) #Turns the robot 90 degrees left
    pick_beeper = _refresh(_board.pick_beeper) #Turns the robot 90 degrees right
    put_beeper = _refresh(_board.put_beeper) #Takes beeper out of bag and puts it down
    front_is_clear = _board.front_is_clear #Returns True if front is clear
    right_is_clear = _board.right_is_clear #Returns True if right is clear
    left_is_clear = _board.left_is_clear #Returns True if left is clear
    beeper_is_present = _board.beeper_is_present #Returns True if there is a beeper in the bag
    facing_north = _board.facing_north #Returns True if robot is facing north
    facing_south = _board.facing_south #Returns True if robot is facing south
    facing_east = _board.facing_east #Returns True if robot is facing east
    facing_west = _board.facing_west #Returns True if robot is facing west
    """
    """
    Delete pass and write your own code here!
    """
    pass

execute(run)

