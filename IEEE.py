import struct


def decimal_a_ieee(ieee):
    bits, = struct.unpack('!I', struct.pack("!f", ieee))
    return "{:032b}".format(bits)
