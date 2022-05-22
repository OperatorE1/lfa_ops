import sys
from telnetlib import Telnet




if __name__ == "__main__":

    for n in range(100,181):

        with Telnet( "crosslinks.satellitesabove.me", 5300 ) as tn:
            out = tn.read_until(b"please:\n")
            #print (out)
            tn.write(b"ticket{bravo684427romeo3:GEDCwFDqDnvyG2MYS2zQ5mN8UOuJtFo-NiWDKikuX17Clx5I2TULa2-QqG6i8hjTjw}\n")


            #observation 1
            out = tn.read_until(b"am I:")
            satNum1 = "SATELLITE 155"
            tn.write(satNum1.encode('ascii') + b"\n")


            #observation 2
            out = tn.read_until(b"am I:")
            satNum1 = "SATELLITE 115"
            tn.write(satNum1.encode('ascii') + b"\n")


            #observation 3
            out = tn.read_until(b"am I:")
            satNum1 = "SATELLITE 148"
            tn.write(satNum1.encode('ascii') + b"\n")



            #observation 3
            out = tn.read_until(b"am I:")
            satNum1 = "SATELLITE 139"
            tn.write(satNum1.encode('ascii') + b"\n")



            #observation 4
            out = tn.read_until(b"am I:")
            satNum1 = "SATELLITE 169"
            tn.write(satNum1.encode('ascii') + b"\n")

            
            #try new one... 
            out = tn.read_until(b"am I:")
            satNum = "SATELLITE %s"%n
            tn.write(satNum.encode('ascii') + b"\n")


            #print (out) 

            out = tn.read_all()
            print (out.decode('ascii'))

        
