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

    def get_id(self):
        return self.server_id

    def server_owner(self):
        return self.owner

    def get_availability(self):
        return self.down

    def get_state(self):
        return self.state

    def server_update(self):
        if self.down > 0:
            self.down -= 1

    def takeover(self, player_id):
        self.owner = player_id

    def set_downtime(self, days):
        self.down = days
