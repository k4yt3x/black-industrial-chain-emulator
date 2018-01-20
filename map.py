# map of the play area

class asciiMap():

    neutral = "N"
    hostile = "X"
    hacked = "H"
    server0 = "N"
    server1 = "N"
    server2 = "N"
    server3 = "N"
    server4 = "N"
    server5 = "N"
    server6 = "N"
    server7 = "N"
    server8 = "N"
    server9 = "N"
    server10 = "N"
    server11 = "N"
    server12 = "N"
    server13 = "N"
    server14 = "N"
    server15 = "N"
    area = "...................." + server0 + "......\n..........." + server1 + "...............\n....." + server2 + ".....................\n...........................\n........." + server3 + ".........." + server4 + "......\n..." + server5 + ".........." + server6 + "............\n......" + server7 + "..........." + server8 + "........\n.........................." + server9 + "\n...........................\n...........................\n.." + server10 + "..........." + server11 + server12 + "...........\n............" + server13 + "........" + server14 + "...." + server15 + "\n"
    width = 27
    length = 12
    servers = 15

    print(area)


asciiMap()
    