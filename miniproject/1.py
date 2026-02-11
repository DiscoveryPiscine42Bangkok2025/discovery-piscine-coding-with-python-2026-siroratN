def checkmate(check):
    board = check.strip().split('\n')
    grid = []
    for line in board:
        grid.append(list(line))
    size = len(grid)
    # print(grid)
    
    # check gird
    for row in grid:
        if len(row) != size:
            print("ไม่ใช่จตุรัส")
            return
    # check if there is exactly one king
    king_count = 0
    for row in grid:
        king_count += row.count('K')
    if king_count > 1:
        print("ต้องมี K 1 ตัว")
        return
    elif king_count == 0:
        print("ต้องมี K 1 ตัว")
        return
    
    # check is P, B, R, Q, K
    valid_pieces = {'P', 'B', 'R', 'Q', 'K', '.'}
    for row in grid:
        for piece in row:
            if piece not in valid_pieces:
                print(f"หมาก {piece} ไม่ถูกต้อง")
                return
    
    # find king position
    king_pos = None
    for i in range(size):
        for j in range(size):
            print([i, j], grid[i][j])
            if grid[i][j] == 'K':
                king_pos = [i, j]
                # return
    print(f"King position: {king_pos}")
    
    kr, kc = king_pos 

    #check king 
    king_move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for move in king_move:
        r = kr + move[0]
        c = kc + move[1]
        while r >= 0 and r < size and c >= 0 and c < size:
                piece = grid[r][c]
                if piece != '.':
                    if piece == 'R' or piece == 'Q':
                        print("Success")
                        return
                    else:
                        print(f"เจอ {piece} ขวาง")
                        break 
                r = r + move[0]
                c = c + move[1]
                
            
    pbq_move = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    
    for move in pbq_move:
        r = kr + move[0]
        c = kc + move[1]

        # P จะกิน King ได้เมื่อ อยู่เหนือ King 1 
        if r >= 0 and r < size and c >= 0 and c < size:
            if grid[r][c] == 'P' and move[0] == -1: 
                print("Success")
                return
        
        while r >= 0 and r < size and c >= 0 and c < size:
            piece = grid[r][c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            elif piece != '.':
                break
                
            r += move[0]
            c += move[1]
                
    print("Fail")

def main():
    board = """\
....B.
...B..
..K...
...P..
......
......"""
    checkmate(board)

main()