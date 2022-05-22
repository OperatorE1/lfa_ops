import sys
from telnetlib import Telnet




if __name__ == "__main__":

    for n in range(100,181):

        with Telnet( "crosslinks.satellitesabove.me", 5300 ) as tn:
            out = tn.read_until(b"please:\n")
            #print (out)
            tn.write(b"ticket{bravo684427romeo3:GEDCwFDqDnvyG2MYS2zQ5mN8UOuJtFo-NiWDKikuX17Clx5I2TULa2-QqG6i8hjTjw}\n")

            
            out = tn.read_until(b"am I:")

            #observation 1
            satNum1 = "SATELLITE 155"
            print ("observation 1 - %s" % satNum1)
            tn.write(satNum1.encode('ascii') + b"\n")


            out = tn.read_until(b"am I:")
            satNum = "%s"%n
            tn.write(satNum.encode('ascii') + b"\n")

            #print (out) 

            out = tn.read_all()
            print (out.decode('ascii'))

