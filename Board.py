import os

class Board():
    def __init__(self, size,line_length,first_player):
        """initialize the board obj, get total size, lines, who starts first"""
        self.size = size 
        self.board = []
        self.line_length = line_length
        self.build_board()
        self.current_player = first_player
        self.size_range = [i for i in range(1,size + 1)]
        self.winner_state = False
        #self.winner_letter = None
        
    @staticmethod
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    
    def build_board(self):
        """build the board with according from 1 to end numbers"""
        for  i in range(1,self.size+1):
            self.board.append(i)
    
    def print_board(self):
        """prints the board """
        for i in range(1,len(self.board) + 1):
            if(i%self.line_length == 0):
                print(self.board[i-1])
            else:
                print(self.board[i-1],end="")

    def check_valid_move(self, number):
        """check if move numebr is valid"""
        if self.board[number -1] in self.size_range:
            return True
        return False
    
    def change_player(self):
        """changes player"""
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
             
    def handle_move(self,move=-1):
        """handles player move"""
        done = False
        number = None
        if(move < 0):
            while not done:
                number = int(input("enter number to player: "))
                done = self.check_valid_move(number)
            self.board[number - 1] = self.current_player #the numbers starts from 0 so need go one down
            self.change_player()
        else:
            self.board[move - 1] = self.current_player #the numbers starts from 0 so need go one down
            #self.change_player()          
    
    def winner_check(self):
        """return True if there is a winner and False if not"""
         
        add = 1
        count = 0
        loc = 0
        compare_to = self.board[0]
       
        #left-right alacson
        for i in range(self.line_length - 1):
            loc = loc + self.line_length + add
            if self.board[loc] == compare_to:
                count += 1
            if count == self.line_length - 1:
                return True
        
        count = 0
        loc = self.line_length - 1
        compare_to = self.board[self.line_length - 1]

        #right left alacson
        for i in range(self.line_length - 1):
            loc = loc + self.line_length -1
            if self.board[loc] == compare_to:
                count += 1
            if count == self.line_length - 1:
                return True
        
        #right-left lines
        current_index = 0
        l1 = []
        for i in range(self.line_length):
            for i in range(self.line_length):
                    l1.append(self.board[current_index])
                    current_index += 1
            if l1.count(l1[0]) == self.line_length:
                return True
            l1 = []

        #up-down lines
        current_index = 0
        l1 = []
        num_top = range(1,self.line_length + 1)
        for i in num_top:
            current_index = i - 1
            for k in range(self.line_length):
                l1.append(self.board[current_index])
                current_index += self.line_length 
            if l1.count(l1[0]) == self.line_length:
                return True
            l1 = []

        #at end!
        return False       

    def play(self):
        """simple play console base"""
        count = 0
        while count < 9 and self.winner_state == False:
            self.cls()
            self.print_board()
            self.handle_move()
            self.winner_state = self.winner_check()
            self.cls()
            self.print_board()
            count+=1
        if(self.winner_state):
            self.change_player()
            print(f"There is a winner! {self.current_player}")
        else:
            print("a tie")
        input()
    

