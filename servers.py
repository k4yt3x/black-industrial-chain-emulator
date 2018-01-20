#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev: K4YT3X IZAYOI
Date Created: 1/20/2018
Last Modified: 1/20/2018


Description: Servers class initializes a list of servers
"""


class servers:

    def __init__(self):
        self.servers = []
        for srv in range(15):
            # server_id, server_status, down
            self.servers.append([srv, 0, 0])
