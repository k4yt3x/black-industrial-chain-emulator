# map of the play area

from servers import Servers

class asciiMap():

    neutral = "N"
    hostile = "X"
    hacked = "H"

    # Servers
    server0 =  Servers(0, 100, 200, "N")
    server1 =  Servers(1, 100, 200, "N")
    server2 =  Servers(2, 100, 200, "N")
    server3 =  Servers(3, 100, 200, "N")
    server4 =  Servers(4, 100, 200, "N")
    server5 =  Servers(5, 100, 200, "N")
    server6 =  Servers(6, 100, 200, "N")
    server7 =  Servers(7, 100, 200, "N")
    server8 =  Servers(8, 100, 200, "N")
    server9 =  Servers(9, 100, 200, "N")
    server10 = Servers(10, 100, 200, "N")
    server11 = Servers(11, 100, 200, "N")
    server12 = Servers(12, 100, 200, "N")
    server13 = Servers(13, 100, 200, "N")
    server14 = Servers(14, 100, 200, "N")
    server15 = Servers(15, 100, 200, "N")

    #area = "...................." + server0 + "......\n..........." + server1 + "...............\n....." + server2 + ".....................\n...........................\n........." + server3 + ".........." + server4 + "......\n..." + server5 + ".........." + server6 + "............\n......" + server7 + "..........." + server8 + "........\n.........................." + server9 + "\n...........................\n...........................\n.." + server10 + "..........." + server11 + server12 + "...........\n............" + server13 + "........" + server14 + "...." + server15 + "\n"

    def __init__(self, server0, server1, server2, server3, server4, server5, server6, server7, server8, server9, server10, server11, server12, server13, server14, server15):
        self.server0 =  server0
        self.server1 =  server1
        self.server2 =  server2
        self.server3 =  server3
        self.server4 =  server4
        self.server5 =  server5
        self.server6 =  server6
        self.server7 =  server7
        self.server8 =  server8
        self.server9 =  server9
        self.server10 = server10
        self.server11 = server11
        self.server12 = server12
        self.server13 = server13
        self.server14 = server14
        self.server15 = server15

    #def get_area(self):
        #return self.area
    
    def get_status(self):
        return self.server0.state

    def get_map_state(self):
        area = "...................." + self.server0.state + "......\n..........." + self.server1.state + "...............\n....." + self.server2.state + ".....................\n...........................\n........." + self.server3.state + ".........." + self.server4.state + "......\n..." + self.server5.state + ".........." + self.server6.sate + "............\n......" + self.server7.state + "..........." + self.server8.state + "........\n.........................." + self.server9.state + "\n...........................\n...........................\n.." + self.server10.state + "..........." + self.server11.state + self.server12.state + "...........\n............" + self.server13.state + "........" + self.server14.state + "...." + self.server15.state + "\n"
        return area