def queen_rules(xPosition, yPosition, color: str):
    listMoves = []

    def add_moves_inside_borders(xMove, yMove):
        if xMove <= 7 and xMove >= 0 and yMove <= 7 and yMove >= 0:
            listMoves.append((xMove,yMove))
        
    for i in range(1, 8):
        if i != yPosition:
            add_moves_inside_borders(xPosition, i)
        if i != xPosition:
            add_moves_inside_borders(i, yPosition)
    for i in range(1, 8 - xPosition):
        xMove = xPosition + i
        add_moves_inside_borders(xMove, yPosition - i)
        add_moves_inside_borders(xMove, yPosition + i)
    for i in range(1, xPosition + 1):
        xMove = xPosition - i
        add_moves_inside_borders(xMove, yPosition - i)
        add_moves_inside_borders(xMove, yPosition + i)

    return listMoves