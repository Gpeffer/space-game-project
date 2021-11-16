import curses
from math import *
import ship 
import planets
import userinfo
import os
import market
#import story


def main():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad( 1 )
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
    highlightText = curses.color_pair( 1 )
    normalText = curses.A_NORMAL
    screen.border( 0 )
    curses.curs_set( 0 )
    max_row = 4 #max number of rows
    box = curses.newwin( max_row + 2, 64, 1, 1 )
    box.box()


    strings = [ "Travel" , "Market", "Inventory", "Quit" ] #list of strings
    row_num = len( strings )

    position = 1

    for i in range( 1, max_row + 1 ):
            if (i == position):
                box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
            else:
                box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], normalText )
            if i == row_num:
                break

    screen.refresh()
    box.refresh()

    x = screen.getch()
    while x != 27:
        if x == curses.KEY_DOWN:
                if position < i:
                    position = position + 1

        if x == curses.KEY_UP:
                if position > 1:
                    position = position - 1

        if x == ord("\n") and position == 1:
                    break
        if x == ord("\n") and position == 2:
                    market.market(ship.current_location_name)
        if x == ord("\n") and position == 3:
                    curses.endwin()
                    userinfo.inventoryget()
        if x == ord("\n") and position == 4:
                    curses.endwin()
                    exit()
        box.erase()
        screen.border( 0 )
        box.border( 0 )

        for i in range( 1 , max_row + 1 ):
                if ( i == position ):
                    box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
                else:
                    box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], normalText )

        screen.refresh()
        box.refresh()
        x = screen.getch()

quit = False
while not quit:
    main()