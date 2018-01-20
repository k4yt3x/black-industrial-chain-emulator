#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: HTC Gamerule/Session controller

Dev: K4YT3X IZAYOI
Date Created: 1/20/2018
Last Modified: 1/20/2018

Description: Hackers class for game HTC
This class defines basic attributes and actions
for hackers.
"""

from servers import Servers
from hacker import Hacker
from worldmap import Worldmap
# from manager import Manager
import socket
import traceback

TIME_LIMIT = 30
GAME_SESSIONS = []
ONLINE_PLAYERS = []


class new_session:

    def __init__(self, player_1_id, player_2_id):
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.empty = True

    def setup_session(self):
        """Creates instances

        This method is called when the game is first started.
        It will create instances for players, map generators
        and servers.

        15 servers instances will be created
        """
        self.player_1 = Hacker()
        self.player_2 = Hacker()
        self.servers = []
        for srv in range(15):
            self.servers.append(Servers(srv))
        self.wmap = Worldmap(self.servers)

    def await_player_actions(self):
        """ Takes user actions

        This method awaits for a user input from the web
        client and make changes to the world accordingly
        """
        pass

    def game_start(self):
        """ Starts the game

        Loops for a certain amount of days, awaits
        for user actions each day.
        """
        for day in range(30):
            self.await_player_actions()
            self.cycle_day()

    def cycle_day(self):
        """
        Decrement busy days by one everyday
        """
        if self.player_1.busy > 0:
            self.player_1.busy -= 1
        if self.player_2.busy > 0:
            self.player_2.busy -= 1


def start_hosting():
    """
    This functions starts the game server.
    It initializes the server socket and starts
    listening on tcp/4444. For each 2 players, it
    will start a new game.
    """
    def initialize_sockets():
        """
        Start listening to TCP stream
        on tcp/4444

        Using 4444 from metasploit
        """
        global sock0
        sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock0.bind(('0.0.0.0', 4444))
        sock0.listen(10)

    def socket_daemon():
        """
        Accepting new tcp connections and created sessions
        """
        while True:
            conn, (rip, rport) = sock0.accept()

    initialize_sockets()


if __name__ == '__main__':
    start_hosting()
else:
    print("This file cannot be imported")
