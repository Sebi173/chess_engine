def rook_rules(xPosition, yPosition, color: str):
    listMoves = []

    def add_moves_inside_borders(xMove, yMove):
        if xMove <= 7 and xMove >= 0 and yMove <= 7 and yMove >= 0:
            listMoves.append((xMove,yMove))
        
    for i in range(1, 8):
        if i != yPosition:
            add_moves_inside_borders(xPosition, i)
        if i != xPosition:
            add_moves_inside_borders(i, yPosition)

    return listMoves