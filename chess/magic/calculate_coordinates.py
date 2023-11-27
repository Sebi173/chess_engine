def calculate_coordinates_for_one_piece(chessPieces):
    binaryRepresentation = str(bin(chessPieces))
    reversedBinaryRepresentation = binaryRepresentation[::-1]

    x = 0
    y = 0
    listCoordinates = []

    for coordinate in reversedBinaryRepresentation:
        if coordinate == "1":
            #transform: translate(0px, 205px);
            #listCoordinates.append(f"transform: translate({100*x}px, {100*y}px);")
            listCoordinates.append((100*x, 100*y))

        x += 1
        if x == 8:
            y += 1
            x = 0

    return listCoordinates

def calculate_coordinates_for_all_pieces(listPosition):

    dicCoordinates = {}

    dicCoordinates["blackBishops"] = calculate_coordinates_for_one_piece(listPosition[0])
    dicCoordinates["blackKing"] = calculate_coordinates_for_one_piece(listPosition[1])
    dicCoordinates["blackKnights"] = calculate_coordinates_for_one_piece(listPosition[2])
    dicCoordinates["blackPawns"] = calculate_coordinates_for_one_piece(listPosition[3])
    dicCoordinates["blackQueen"] = calculate_coordinates_for_one_piece(listPosition[4])
    dicCoordinates["blackRooks"] = calculate_coordinates_for_one_piece(listPosition[5])

    dicCoordinates["whiteBishops"] = calculate_coordinates_for_one_piece(listPosition[6])
    dicCoordinates["whiteKing"] = calculate_coordinates_for_one_piece(listPosition[7])
    dicCoordinates["whiteKnights"] = calculate_coordinates_for_one_piece(listPosition[8])
    dicCoordinates["whitePawns"] = calculate_coordinates_for_one_piece(listPosition[9])
    dicCoordinates["whiteQueen"] = calculate_coordinates_for_one_piece(listPosition[10])
    dicCoordinates["whiteRooks"] = calculate_coordinates_for_one_piece(listPosition[11])

    return dicCoordinates