def from_coordinates_to_binary(listCoordinates):
    binPosition = 0

    for x,y in listCoordinates:
        intCoordinate = x + y * 8
        binCoordinate = 2**intCoordinate
        binPosition += binCoordinate

    return binPosition