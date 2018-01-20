#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev: K4YT3X IZAYOI
Last Modified: 1/20/2018

Dev: Thai
Date Created: 1/20/2018
Last Modified: 1/20/2018

Description: Hackers class for game HTC
This class defines basic attributes and actions
for hackers.
"""


class Hacker:

    def __init__(self):
        self.money = 5000
        self.busy = 0  # if equals 0 then hacker can make a move

    class exploit:

        def zero_day(level):
            # The ultimate attack that will compromise a server
            # immediately at a high cost of money
            return level

        def nmap_scan(level):
            print("Doing nmap scan")
            return level

        def sql_injection(level):
            self.hacker.busy += level
            return level

        def smb(level):
            # If the smb port is open
            return level

    def day_pass(self):
        if self.busy > 0:
            self.busy -= 1

    def add_busy(self, level):
        if self.busy == 0:
            self.busy += level
            print("Successfully initialized exploit")


# Single file debugging statements

if __name__ == '__main__':
    hacker = Hacker()
    print(hacker.exploit.test())
    print(hacker.busy)
