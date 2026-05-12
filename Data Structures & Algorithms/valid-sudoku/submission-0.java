class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int row=0;row<9;row++){
            for(int col=0;col<9;col++){
                char num=board[row][col];
                if(num=='.'){
                    continue;
                }
                for(int i=0;i<9;i++){
                    if(i!=col&&board[row][i]==num){
                        return false;
                    }
                }
                for(int i=0;i<9;i++){
                    if(i!=row&&board[i][col]==num){
                        return false;
                    }
                }
                int startrow=row-(row%3);
                int startcol=col-(col%3);
                for(int i=0;i<3;i++){
                    for(int j=0;j<3;j++){
                        if(((i+startrow)!=row||(j+startcol)!=col)&&board[i+startrow][j+startcol]==num){
                            return false;
                        }
                    }
                }

            }
        }
        return true;
    }
    
}
