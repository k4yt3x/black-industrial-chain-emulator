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
        self.down = 0
        self.owner = 0

    def get_id(self):
        return self.server_id

    def get_server_owner(self):
        """gets server owner id

        returns current owner ID
        if not owned by anyone (neutral), then
        owner == 0. Otherwise owner == user ID
        """
        return self.owner

    def get_availability(self):
        """Gets server "down" information

        Returns an int. in remaining "down" days
        """
        return self.down

    def takeover(self, player_id):
        """when player hacks this server

        The ownership of the server will be
        yelded to the player if this player
        hacks it successfully
        """
        self.owner = player_id

    def set_downtime(self, days):
        """Set server downtime

        When a player ddos this server or
        if there's a conflict
        """
        self.down = days
