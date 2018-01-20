#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: hackbuttons

Dev: K4YT3X IZAYOI
Date Created: 1/20/2018
Last Modified: 1/20/2018

Description: Ajax will call this file when the
user clicks a button. It will send the button ID
to the server using TCP
"""


import socket

RHOST = "uofthacks.k4yt3x.com"


def initialize_socket():
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock0.connect((RHOST, 4444))
    return sock0


"""
def on_recv():
    global sock0
    recved = sock0.recv(1024).decode()"""


def send_msg(msg):
    global sock0
    sock0.send(str(msg).encode('utf-8'))


if __name__ == '__main__':
    sock0 = initialize_socket()
    send_msg(1)
