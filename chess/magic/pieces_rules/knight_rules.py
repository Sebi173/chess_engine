def knight_rules(xPosition, yPosition, color: str):
    listMoves = []

    def add_moves_inside_borders(xMove, yMove):
        if xMove <= 7 and xMove >= 0 and yMove <= 7 and yMove >= 0:
            listMoves.append((xMove,yMove))
        
    x = 2
    for y in [-1, 1]:
        add_moves_inside_borders(xPosition - x, yPosition + y)
        add_moves_inside_borders(xPosition + x, yPosition + y)
    y = 2
    for x in [-1, 1]:
        add_moves_inside_borders(xPosition + x, yPosition - y)
        add_moves_inside_borders(xPosition + x, yPosition + y)

    return listMoves