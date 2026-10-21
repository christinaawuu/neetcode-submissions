class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #[row][col]

        #[0][0], [0][1], [0][2]
        #[1][0], [1][1], [1][2]
        #[2][0], [2][1], [2][2]

        #nested for loop to see if there are any duplicates
        # check columns [0][i] and then rows [i][0]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 
        box = 0
        
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue

                if val not in cols[c]:
                    #if the val is not in the col
                    cols[c].add(val) 
                else:
                    return False
                # check the row
                if val not in rows[r]:
                    #if the val is not in the row
                    rows[r].add(val) 
                else:
                    return False

                #check the boxes
                box = (r//3) * 3 + (c//3)
                #insert the val into the box and see if there's a dup for that box
                if val not in boxes[box]:
                    boxes[box].add(val)
                else:
                    return False

        return True         
              
                
                
