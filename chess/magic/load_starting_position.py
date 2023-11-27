def load_starting_position():
    blackBishops = 2**2 + 2**5
    blackKing = 2**4
    blackKnights = 2**1 + 2**6
    blackPawns = 2**8 + 2**9 + 2**10 + 2**11 + 2**12 + 2**13 + 2**14 + 2**15
    blackQueen = 2**3
    blackRooks = 2**0 + 2**7

    whiteBishops = 2**58 + 2**61
    whiteKing = 2**60
    whiteKnights = 2**57 + 2**62
    whitePawns = 2**48 + 2**49 + 2**50 + 2**51 + 2**52 + 2**53 + 2**54 + 2**55
    whiteQueen = 2**59
    whiteRooks = 2**56 + 2**63

    listPosition = [blackBishops, blackKing, blackKnights, blackPawns, blackQueen, blackRooks, 
                    whiteBishops, whiteKing, whiteKnights, whitePawns, whiteQueen, whiteRooks]

    return listPosition