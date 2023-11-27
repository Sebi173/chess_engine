from .pieces_rules.bishop_rules import bishop_rules
from .pieces_rules.king_rules import king_rules
from .pieces_rules.knight_rules import knight_rules
from .pieces_rules.pawn_rules import pawn_rules
from .pieces_rules.queen_rules import queen_rules
from .pieces_rules.rook_rules import rook_rules


def calculate_legal_moves(chessPiece, dicCoordinates):
    xPosition = int(chessPiece[-2])
    yPosition = int(chessPiece[-1])
    intPosition = xPosition + 8 * yPosition
    binPosition = bin(2**intPosition)
    color = chessPiece[0]
    piece = chessPiece[1:3]
    print(chessPiece)
    print(intPosition)

    listLegalMoves = []

    if piece == "Bi":
        listLegalMoves = bishop_rules(xPosition, yPosition, color)
    elif piece == "Ki":
        listLegalMoves = king_rules(xPosition, yPosition, color)
    elif piece == "Kn":
        listLegalMoves = knight_rules(xPosition, yPosition, color)
    elif piece == "Pa":
        listLegalMoves = pawn_rules(xPosition, yPosition, color)
    elif piece == "Qu":
        listLegalMoves = queen_rules(xPosition, yPosition, color)
    elif piece == "Ro":
        listLegalMoves = rook_rules(xPosition, yPosition, color)

    print(listLegalMoves)

    dicCoordinates["listLegalMoves"] = listLegalMoves

    return dicCoordinates