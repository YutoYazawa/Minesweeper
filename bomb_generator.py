import numpy as np
from lib import on_area

class BombGenerator():
    def __init__(self,board_size,bomb_num):
        self.board_size=board_size
        self.bomb_num=bomb_num

    def generate(self,ignore_coord):
        if on_area((0,0),(self.board_size[0]-1,self.board_size[1]-1),click_coord=ignore_coord):
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-9),np.ones(self.bomb_num)]) # zerosの数に-9してるのは初期マスの関係
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]-1)+ignore_coord[1]-1,[0,0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-1,[0,0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]+1)+ignore_coord[1]-1,[0,0,0])
        elif ignore_coord==(0,0):
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-4),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1],[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]+1)+ignore_coord[1],[0,0])
        elif ignore_coord==(0,self.board_size[1]-1):
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-4),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-1,[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]+1)+ignore_coord[1]-1,[0,0])
        elif ignore_coord==(self.board_size[0]-1,0):
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-4),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-2,[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]-1)+ignore_coord[1],[0,0])
        elif ignore_coord==(self.board_size[0]-1,self.board_size[1]-1):
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-4),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]-1)+ignore_coord[1]-1,[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-1,[0,0])
        elif ignore_coord[0]==0:
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-6),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-1,[0,0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]+1)+ignore_coord[1]-1,[0,0,0])
        elif ignore_coord[0]==self.board_size[0]-1:
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-6),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]-1)+ignore_coord[1]-1,[0,0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-1,[0,0,0])
        elif ignore_coord[1]==0:
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-6),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]-1)+ignore_coord[1],[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1],[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]+1)+ignore_coord[1],[0,0])
        elif ignore_coord[1]==self.board_size[1]-1:
            board_alpha=np.hstack([np.zeros(self.board_size[0]*self.board_size[1]-self.bomb_num-6),np.ones(self.bomb_num)])
            np.random.shuffle(board_alpha)
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]-1)+ignore_coord[1]-1,[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0])+ignore_coord[1]-1,[0,0])
            board_alpha=np.insert(board_alpha,self.board_size[1]*(ignore_coord[0]+1)+ignore_coord[1]-1,[0,0])
        board_alpha=board_alpha.reshape(self.board_size[0],self.board_size[1])
        return list(board_alpha)