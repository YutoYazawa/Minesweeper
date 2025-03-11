import pygame

import bomb_generator
from colors import *
from lib import *

class Board(): # ボードを定義するクラス
    def __init__(self, board_size, cell_size, bomb_num, offset):
        self.OFFSET=offset
        self.board_size=board_size
        self.cell_size=cell_size
        self.bomb_num=bomb_num
        self.clear()
        self.num_font=pygame.font.SysFont(None,cell_size[0]-4)
        self.flag_num=0
    
    def clear(self):
        self.board_list=[[0 for i in range(self.board_size[1])]for j in range(self.board_size[0])]
        self.display_list=[[False for i in range(self.board_size[1])]for j in range(self.board_size[0])]
        #self.display_list=[[True for i in range(self.board_size[1])]for j in range(self.board_size[0])]
        self.flag_list=[[False for i in range(self.board_size[1])]for j in range(self.board_size[0])]
    
    def toggle_flag(self, coord):
        if (not self.display_list[coord[0]][coord[1]]) and self.flag_num<self.bomb_num:
        	if self.flag_list[coord[0]][coord[1]]:
        		self.flag_num-=1
        	else:
        		self.flag_num+=1
            self.flag_list[coord[0]][coord[1]]=not self.flag_list[coord[0]][coord[1]]
            if [[1 if j else 0 for j in i] for i in self.display_list]==[[0 if j else 1 for j in i] for i in self.flag_list]: # もし判明してる安全な場所 == !フラグが建てられてる場所なら
                return 0xff
            return 0
        return -1
    
    def click(self, coord):
        if not self.display_list[coord[0]][coord[1]] and not self.flag_list[coord[0]][coord[1]]:
            self.display_list[coord[0]][coord[1]]=True
            if self.board_list[coord[0]][coord[1]]==1:
                return -1
            else:
                if self.get_cell_num(coord)==0:
                    surround=((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))
                    for rel_coord in surround:
                        if coord[0]+rel_coord[0]<0 or coord[1]+rel_coord[1]<0 or coord[0]+rel_coord[0]>self.board_size[0]-1 or coord[1]+rel_coord[1]>self.board_size[1]-1:
                            continue
                        self.click((coord[0]+rel_coord[0],coord[1]+rel_coord[1]))
                if [[1 if j else 0 for j in i] for i in self.display_list]==[[0 if j else 1 for j in i] for i in self.flag_list]: # もし判明してる安全な場所 == !フラグが建てられてる場所なら
                    return 0xff
                return 0
        return 1
    
    def generate(self,ignore_coord):
        generator=bomb_generator.BombGenerator(board_size=self.board_size,bomb_num=self.bomb_num)
        self.board_list=generator.generate(ignore_coord)

    def draw(self, screen):
        pygame.draw.rect(screen,BROWN,(self.OFFSET-1,self.OFFSET-1,self.cell_size[0]*(self.board_size[0])+2,self.cell_size[1]*(self.board_size[1])+2),2)
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                pygame.draw.rect(screen,BROWN,(self.OFFSET+self.cell_size[0]*i,self.OFFSET+self.cell_size[1]*j,self.cell_size[0],self.cell_size[1]),1)
                if self.display_list[i][j]:
                    cell_num=self.get_cell_num((i,j))
                    pygame.draw.rect(screen,CELL_COLORS[cell_num],(self.OFFSET+self.cell_size[0]*i+1,self.OFFSET+self.cell_size[1]*j+1,self.cell_size[0]-2,self.cell_size[1]-2))
                    screen.blit(self.num_font.render(str(cell_num),True,WHITE),(self.OFFSET+self.cell_size[0]*i+self.cell_size[0]/2-8,self.OFFSET+self.cell_size[1]*j+self.cell_size[1]/2-12))
                else:
                    pygame.draw.rect(screen,NULL,(self.OFFSET+self.cell_size[0]*i+1,self.OFFSET+self.cell_size[1]*j+1,self.cell_size[0]-2,self.cell_size[1]-2))
                    if self.flag_list[i][j]:
                        draw_flag(screen=screen,coord=(self.OFFSET+self.cell_size[0]*i,self.OFFSET+self.cell_size[1]*j), cell_size=self.cell_size)
    
    def get_cell_num(self, coord):
        if self.board_list[coord[0]][coord[1]]==1:
            return -1
        surround=((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))
        num=0
        for rel_coord in surround:
            if coord[0]+rel_coord[0]<0 or coord[1]+rel_coord[1]<0 or coord[0]+rel_coord[0]>self.board_size[0]-1 or coord[1]+rel_coord[1]>self.board_size[1]-1:
                continue
            a=(coord[0]+rel_coord[0],coord[1]+rel_coord[1])
            if self.board_list[a[0]][a[1]]==1:
                num+=1
        return num
