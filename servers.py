#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev: K4YT3X IZAYOI
Date Created: 1/20/2018
Last Modified: 1/20/2018

Dev: Thai
Last Modified: 1/20/2018

Description: Servers class initializes a list of servers
"""


class Servers:

    def __init__(self, server_id, player_1_id, player_2_id, server_state):
        self.server_id = server_id
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.state = server_state
        # 0 being neutral, if belongs to a player then this value == player_id
        self.owner = 0
        # 0 being up, otherwise represents the remaining days being down.
        # This value should decrement everyday if self.down != 0
        self.down = 0

    def get_id(self):
        return self.server_id

    def server_owner(self):
        return self.owner

    def get_availability(self):
        return self.down

    def get_state(self):
        return self.state
