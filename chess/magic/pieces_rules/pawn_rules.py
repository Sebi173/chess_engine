def pawn_rules(xPosition, yPosition, color: str):
    listMoves = []

    def add_moves_inside_borders(xMove, yMove):
        if xMove <= 7 and xMove >= 0 and yMove <= 7 and yMove >= 0:
            listMoves.append((xMove,yMove))
        
    if color == "W":
        add_moves_inside_borders(xPosition, yPosition - 1)
        if yPosition == 6:
            add_moves_inside_borders(xPosition, yPosition - 2)
    else:
        add_moves_inside_borders(xPosition, yPosition + 1)
        if yPosition == 1:
            add_moves_inside_borders(xPosition, yPosition + 2)

    return listMoves