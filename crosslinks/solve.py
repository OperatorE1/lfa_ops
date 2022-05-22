import sys
from telnetlib import Telnet


def force(satNum):
    with Telnet( "crosslinks.satellitesabove.me", 5300 ) as tn:
        out = tn.read_until(b"please:\n")
        #print (out)
        tn.write(b"ticket{bravo684427romeo3:GEDCwFDqDnvyG2MYS2zQ5mN8UOuJtFo-NiWDKikuX17Clx5I2TULa2-QqG6i8hjTjw}\n")

        out = tn.read_until(b"am I:")

        #print (out)

        tn.write(satNum.encode('ascii') + b"\n")

        out = tn.read_all()
        print (out.decode('ascii'))


if __name__ == "__main__":
    for n in range(101,180):
        print(n)

        force("%s"%n)

