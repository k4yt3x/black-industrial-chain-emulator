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

    def __init__(self, server_id):
        self.server_id = server_id
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

    def server_update(self):
        if self.down > 0:
            self.down -= 1

    def takeover(self, player_id):
        self.owner = player_id

    def add_downtime(self, days):
        self.down = days
