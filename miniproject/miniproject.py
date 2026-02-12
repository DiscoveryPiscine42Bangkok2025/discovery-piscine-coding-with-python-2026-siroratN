def checkmate(check):
    board = check.strip().split('\n')
    grid = []
    for line in board:
        grid.append(list(line))
    size = len(grid)
    # print(grid)
    
    # check gird
    for row in grid:
        print(row)
        if len(row) != size:
            print("ไม่ใช่จตุรัส")
            return
        
    # check is one king
    king_count = 0
    for row in grid:
        king_count += row.count('K')
    if king_count != 1:
        print("ต้องมี K 1 ตัว")
        return

    # check is P, B, R, Q, K
    valid_pieces = ['P', 'B', 'R', 'Q', 'K', '.']
    for row in grid:
        for piece in row:
            if piece not in valid_pieces:
                print(f"{piece} ไม่ถูกต้อง")
                return
    
    # king position
    king_pos = None
    for i in range(size):
        for j in range(size):
            print([i, j], grid[i][j])
            if grid[i][j] == 'K':
                king_pos = [i, j]
                break
        if king_pos is not None:
            break
    # print(f"King position: {king_pos}")

#check king 
    kr = king_pos[0]
    kc = king_pos[1]
    
    #ตรงกับนอน (+)
    
    #    .
    #  . K .
    #    .
    
    king_move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for move in king_move:
        r = kr + move[0]
        c = kc + move[1]
        # print(kr, kc, "->", r, c)
        # print(kc)
        while r >= 0 and r < size and c >= 0 and c < size:
                piece = grid[r][c]
                # ถ้าถูกล้อมด้วย R หรือ Q ในรูปแบบ แสดงว่าโดน checkmate ได้
                if piece == 'R' or piece == 'Q':
                    print("Success")
                    return
                elif piece != '.':
                    break
                r = r + move[0]
                c = c + move[1]
                
    
    # แนวทแยง
    
    # .   .
    #   K  
    # .   .
    
    pbq_move = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for move in pbq_move:
        r = kr + move[0]
        c = kc + move[1]
        print(kc)
        if r >= 0 and r < size and c >= 0 and c < size:
            # เป็นเบี้ยไหม
            if grid[r][c] == 'P' and move[0] == -1: 
                print("Success")
                return
        
        while r >= 0 and r < size and c >= 0 and c < size:
            # เป็น Bishop หรือ Queen ไหม (ไม่เช็ค move[0] == -1 เพราะมันกินกลับหลังได้ด้วย)
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
....
.K..
....
....
"""
    checkmate(board)

main()