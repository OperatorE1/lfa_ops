from telnetlib import Telnet

data={
    "d6bc6fbee628c3278ef534fd22700ea4017914c2214aa86447805f858d9b8ad4" : "4aada52c9abb92d32c57007091f35bc8", #  boston.jpg
    "04ca7d835e92ae1e4b6abc44fa2f78f6490e0058427fcb0580dbdcf7b15bbb55" : "a6ec1dcd107fc4b5373003db4ed901f3", #  chicago.jpg
    "242f693263d0bcc3dd3d710409c22673e5b6a58c1a1d16ed2e278a8d844d7b0b" : "ae7a2a6b7b583aa9cee67bd13edb211e", #  la.jpg
    "2aa0736e657a05244e0f8a1c10c4492dde39907c032dba9f3527b49873f1d534" : "1312798c840210cd7d18cf7d1ff64a40", #  miami.jpg
    "983b1cc802ff33ab1ceae992591f55244538a509cd58f59ceee4f73b6a17b182" : "e115d6633cdecdad8c5c84ee8d784a55", #  nyc.jpg
    "7e03349fe5fa4f9e56642e6787a0bfda27fb4f647e3c283faaf7bd91dbfd1d39" : "", #  oahu.jpg
    "b4447c4b264b52674e9e1c8113e5f29b5adf3ee4024ccae134c2d12e1b158737" : "20b7542ea7e35bf58e9c2091e370a77d", #  portland.jpg
    "f37e36824f6154287818e6fde8a4e3ca56c6fea26133aba28198fe4a5b67e1a1" : "f24b6a952d3f0a8f724e3c70de2e250c", #  sf.jpg
    "088f26f7c0df055b6d1ce736f6d5ffc98242b752bcc72f98a1a20ef3645d05c1" : "09e829c63aff7b72cb849a92bf7e7b48", #  slc.jpg
    "3b20a3b5b327c524674ca5a8310beb2d9efc5c257e60c4a9b0709d41e63584a3" : "7cef397dfa73de3dfedb7e537ed8bf03", #  vegas.jpg
}


cmds=[
    "PLAYBACK_FILE" ,
    "SHELL_CMD",
    "SEND_FILE",
    "LOAD_TBL",
    "START_APP",
    "DECOMPRESS_FILE",
    "TAKE_IMG",
    "GET_IMAGE_SIZE",
    "DLINK_IMG",
      ]


cmdNum=1

if __name__ == "__main__":

    with Telnet( "leggo.satellitesabove.me", 5300 ) as tn:
        out = tn.read_until(b"please:\n")
        tn.write(b"ticket{oscar361565delta3:GLuL_GF0FuUMXvnsP4O2ixZRnl59eHaOdum4k0z4wvqqzoDyUIQO32Mx2yPl-CJMCA}\n")

        out= tn.read_until(b"CMD>")
        c = cmds[cmdNum]
        print(c)
        tn.write(c.encode('ascii') + b"\n")

        out = tn.read_until(b">>")
        out = out.decode('ascii')

        sha = out.split("\n")[0][:-1]

        r = data[sha].upper()
        print(sha,r)
        
        tn.write(r.encode('ascii') + b"\n")
        
        out = tn.read_all()
        print (out.decode('ascii'))
        

