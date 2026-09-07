class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for mst in range(0,9,3):
            for nst in range(0,9,3):
                temp=[]
                for i in range(mst,mst+3):
                    for j in range(nst,nst+3):
                        cur=board[i][j]
                        if cur!='.':
                            temp.append(int(cur))
                if len(temp)!=len(set(temp)):
                    return False
        for i in range(len(board)):
            t=[]
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    t.append(int(board[i][j]))
            if len(t)!=len(set(t)):
                    return False

            
        
        for i in range(len(board[0])):
            te=[]
            for j in range(len(board)):
                if board[j][i]!='.':
                    te.append(board[j][i])
            if len(te)!=len(set(te)):
                return False


        return True

        