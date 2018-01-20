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
from exploits import Exploit
# from manager import Manager
import multiprocessing
import socket
import time
import traceback

WINNING_AMOUNT = 30000
TIME_LIMIT = 30
GAME_SESSIONS = []
ONLINE_PLAYERS = []
player_id = 0


class new_session:

    def __init__(self, player_1_id, player_2_id, player_1_socket):
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.player_1_socket = player_1_socket
        self.player_2_socket = False
        self.player_1_action = False
        self.player_2_action = False
        self.exploit = Exploit()
        self.setup_session()
        while True:
            if self.player_2_socket:
                self.game_start()
            else:
                time.sleep(0.1)

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

    def listen_for_actions(self, sock_obj):
        return sock_obj.recv(1024).decode('utf-8')

    def await_player_actions(self):
        """ Takes user actions

        This method awaits for a user input from the web
        client and make changes to the world accordingly
        """
        listening_session = []
        p1 = multiprocessing.Process(target=self.listen_for_actions, args=(self.player_1_socket,))
        p2 = multiprocessing.Process(target=self.listen_for_actions, args=(self.player_2_socket,))
        listening_session.append(p1)
        listening_session.append(p2)
        p1.start()
        p2.start()
        pass

    def process_player_actions(self):
        """ Apply actions into database

        This method processes the action and change the server
        data/player data according to the user action.
        """
        if self.exploit == 0:
            print('zero_day')
        elif self.exploit == 1:
            print('nmap_scan')
        elif self.exploit == 2:
            print('sqlmap')
        elif self.exploit == 3:
            print('eternal_blue')
        elif self.exploit == 4:
            print()
        elif self.exploit == 5:
            print()

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

        # Each hacked server will generate $50 for
        # the hacker every day
        for server in self.servers:
            if server.owner == self.player_1_id:
                self.player_1.money += 50
            elif server.owner == self.player_2_id:
                self.player_2.money += 50
        if self.player_1.money >= WINNING_AMOUNT:
            print('Hacker 1 Won!')
        if self.player_2.money >= WINNING_AMOUNT:
            print('Hacker 2 Won!')
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
        sock0.listen(4)

    def socket_daemon():
        """
        Accepting new tcp connections and created sessions
        """
        global player_id
        while True:
            conn, (rip, rport) = sock0.accept()
            if len(GAME_SESSIONS) == 0:
                GAME_SESSIONS.append(new_session(player_id, player_id + 1, conn))
                player_id += 1
            else:
                for game in GAME_SESSIONS:
                    if game.player_2_id == player_id:
                        game.player_2_socket = conn

    initialize_sockets()
    socket_daemon()

if __name__ == '__main__':
    exit(0)
    try:
        start_hosting()
    except Exception:
        # This will grab and print the error
        # Nothing else at this point for fail-safe handling
        traceback.print_exc()
else:
    print("This file cannot be imported")
