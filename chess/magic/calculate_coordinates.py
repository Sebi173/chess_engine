def calculate_coordinates_for_one_piece(chessPieces: bin):
    """
    Input: ChessPieces [bin]
    Is a binary representations of exactly one category of chess pieces
    0b100010000
    Output: listCoordinates [list]
    Contains (x,y,id) tuple of every chess piece of said category, where x,y gives the positioning on the board for the frontend
    """

    binaryRepresentation = str(bin(chessPieces))
    reversedBinaryRepresentation = binaryRepresentation[::-1]

    x = 0
    y = 0
    listCoordinates = []

    for coordinate in reversedBinaryRepresentation:
        if coordinate == "1":
            #transform: translate(0px, 205px);
            listCoordinates.append((100*x, 100*y, str(x)+str(y)))

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