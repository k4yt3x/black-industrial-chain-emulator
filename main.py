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

TIME_LIMIT = 30


class new_session:

    def __init__(self, player_1_id, player_2_id):
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id

    def setup_session(self):
        self.player_1 = Hacker()
        self.player_2 = Hacker()
        self.servers = []
        for srv in range(15):
            self.servers.append(Servers(srv))
        self.wmap = Worldmap(self.servers)

    def game_start(self):
        for day in range(30):
            self.cycle_day()

    def cycle_day(self):
        if self.player_1.busy > 0:
            self.player_1.busy -= 1
        if self.player_2.busy > 0:
            self.player_2.busy -= 1


def start_hosting():
    pass


if __name__ == '__main__':
    start_hosting()
else:
    print("This file cannot be imported")
