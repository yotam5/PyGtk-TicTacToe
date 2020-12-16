from gi.repository import Gtk, Pango, Gdk
from Board import Board
import sys
"""
    button1.modify_fg(Gtk.StateType.NORMAL,Gdk.color_parse("green"))
        button1.modify_bg(Gtk.StateType.NORMAL,Gdk.color_parse("green"))
"""

import gi
import time
gi.require_version("Gtk", "3.0")


class MyPopUp(Gtk.Window):
    """simple class for the pop up window when there is a winner or a tie"""

    def __init__(self):
        Gtk.Window.__init__(self, title="Game Ended!")

        self.button = Gtk.Button(label="Click Here to exit!")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Quitting!")
        Gtk.main_quit()


def run_pop():
    """run the pop up window"""
    win = MyPopUp()
    win.set_position(Gtk.WindowPosition.CENTER)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


class GridWindow(Gtk.Window):
    """the main window for the game"""

    def __init__(self):
        Gtk.Window.__init__(self, title="Tic Tac Toe")
        css = "GtkButton { font: 16}"
        grid = Gtk.Grid()
        print(grid.get_child_at(0, 1))
        self.add(grid)
        self.set_size_request(300, 300)
        width = 100
        height = 100
        self.game_board = Board(9, 3, 'X')
        self.winner = False
        self.count = 0
        self._quit_c = 0
        font = Pango.font_description_from_string("Times 20")

        button1 = Gtk.Button(label="1")
        button1.connect("clicked", self.on_button_clicked)
        button1.set_size_request(width, height)
        button1.modify_font(font)

        button2 = Gtk.Button(label="2")
        button2.set_size_request(width, height)
        button2.connect("clicked", self.on_button_clicked)
        button2.set_size_request(width, height)
        button2.modify_font(font)

        button3 = Gtk.Button(label="3")
        button3.set_size_request(width, height)
        button3.connect("clicked", self.on_button_clicked)
        button3.set_size_request(width, height)
        button3.modify_font(font)

        button4 = Gtk.Button(label="4")
        button4.set_size_request(width, height)
        button4.connect("clicked", self.on_button_clicked)
        button4.set_size_request(width, height)
        button4.modify_font(font)

        button5 = Gtk.Button(label="5")
        button5.set_size_request(width, height)
        button5.connect("clicked", self.on_button_clicked)
        button5.set_size_request(width, height)
        button5.modify_font(font)

        button6 = Gtk.Button(label="6")
        button6.set_size_request(width, height)
        button6.connect("clicked", self.on_button_clicked)
        button6.set_size_request(width, height)
        button6.modify_font(font)

        button7 = Gtk.Button(label="7")
        button7.set_size_request(width, height)
        button7.connect("clicked", self.on_button_clicked)
        button7.set_size_request(width, height)
        button7.modify_font(font)

        button8 = Gtk.Button(label="8")
        button8.set_size_request(width, height)
        button8.connect("clicked", self.on_button_clicked)
        button8.set_size_request(width, height)
        button8.modify_font(font)

        self.button9 = Gtk.Button(label="9")
        self.button9.set_size_request(width, height)
        self.button9.connect("clicked", self.on_button_clicked)
        self.button9.set_size_request(width, height)
        self.button9.modify_font(font)

        grid.add(button1)
        grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(button1, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button4, button1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button6, button3, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button5, button2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button7, button4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button8, button5, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.button9, button6,
                            Gtk.PositionType.BOTTOM, 1, 1)

    def on_button_clicked(self, button):
        """activated when a button clicked"""
        if not self.winner:  # if the game ended with winner you dont need to click
            self.game_board.handle_move(int(button.get_label()))
            # self.button9.modify_fg(Gtk.StateType.NORMAL,Gdk.color_parse("green"))
            button.set_label(self.game_board.current_player)
            # button.modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse("green")) why not working?
            self.game_board.change_player()
            # print(1)
            button.set_sensitive(False)
            # print(2)
            self.winner_exit()
            self.count += 1
            if self.count == 9 and not self.winner:
                print("a tie!")

        while Gtk.events_pending():  # idk...
            Gtk.main_iteration()

    def winner_exit(self):
        """if theres a winner the bool state updates"""
        if self.game_board.winner_check():
            print("a winner!")
            self.winner = True
        while Gtk.events_pending():
            Gtk.main_iteration()


#global vars
state = True


def main():
    # more global vars
    global win
    global state
    win = GridWindow()
    win.set_position(Gtk.WindowPosition.CENTER)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    while state and win.props.visible:
        while Gtk.events_pending():
            Gtk.main_iteration()
        if win.winner or (win.count == 9 and not win.winner):
            # PaR('q')
            # Insert text at the end on the textview.
            run_pop()
            state = False

    # print(1)
    # print(2)
    while Gtk.events_pending():
        Gtk.main_iteration()
    time.sleep(2)
    # print(3)
    Gtk.main_quit()


main()
