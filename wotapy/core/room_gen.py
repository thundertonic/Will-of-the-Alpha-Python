from wotapy.objects.place import Place

"""
Functions related to room generation.
"""

def empty_room(size2d):
    """
    Generate an empty room with walls on the sides.
    """
    
    sizex, sizey = size2d
    room = []

    # top wall section
    room.append('w' * sizex)
    # rows with empty space in between
    room += ['w' + ' ' * (sizex - 2) + 'w' for i in range(sizey - 2)]
    # bottom wall section
    room.append('w' * sizex)

    return Place(room, w='wall')