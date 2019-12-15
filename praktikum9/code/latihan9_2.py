def volume_of_beam(l, w, h, beam_code = "TB03"):
    volume = l * w * h
    print("Volume balok dari %s adalah %d" % (beam_code, volume))

volume_of_beam(12, 7, 3)