def king_rules(xPosition, yPosition, color: str):
    listMoves = []

    def add_moves_inside_borders(xMove, yMove):
        if xMove <= 7 and xMove >= 0 and yMove <= 7 and yMove >= 0:
            listMoves.append((xMove,yMove))
        
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            xMove = xPosition + x
            yMove = yPosition + y
            add_moves_inside_borders(xMove, yMove)

    return listMoves