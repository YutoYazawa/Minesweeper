import sys
import pygame
from pygame.locals import *

import menu
import board
from colors import *
from lib import on_area, get_coord_from_click


# Consts
SCREEN_SIZE = (1200,800)
BOARD_SIZE = (20,10)
CELL_SIZE = (48,48)
BOMB_NUM = 100
OFFSET = 20

def main():
    # Pygameの初期化
    pygame.init()
    # スクリーンの作成 (大きさSCREEN_SIZE)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    # タイトルバーの設定
    pygame.display.set_caption("Test")
    
    game_stat=0
    
    myboard = board.Board(board_size=BOARD_SIZE,cell_size=CELL_SIZE, bomb_num=BOMB_NUM, offset=OFFSET)
    while True: # メインループ
        screen.fill(BACKGROUND)
        
        myboard.draw(screen)
        
        if game_stat==2:
            screen.blit(pygame.font.SysFont("Zen Maru Gothic Black",size=64).render("[DEBUG]\nGameOver",True,FLAG),(SCREEN_SIZE[0]/2-400,SCREEN_SIZE[1]/2-64))
        elif game_stat==3:
            screen.blit(pygame.font.SysFont("Zen Maru Gothic Black",size=64).render("[DEBUG]\nGameClear",True,CELL_COLORS[6]),(SCREEN_SIZE[0]/2-400,SCREEN_SIZE[1]/2-64))
        
        pygame.display.update()
        
        # イベント処理
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if on_area((OFFSET,OFFSET),(OFFSET+BOARD_SIZE[0]*CELL_SIZE[0],OFFSET+BOARD_SIZE[0]*CELL_SIZE[0]),event.pos):
                        match game_stat:
                            case 0:
                                myboard.generate(get_coord_from_click(click_coord=event.pos, cell_size=CELL_SIZE, OFFSET=OFFSET))
                                myboard.click(get_coord_from_click(click_coord=event.pos, cell_size=CELL_SIZE, OFFSET=OFFSET))
                                game_stat=1
                            case 1:
                                ret=myboard.click(get_coord_from_click(click_coord=event.pos, cell_size=CELL_SIZE, OFFSET=OFFSET))
                                if ret==-1:
                                    game_stat=2
                                elif ret==0xff:
                                    game_stat=3
                    else:
                        pass
                elif event.button==3:
                    if on_area((OFFSET,OFFSET),(OFFSET+BOARD_SIZE[0]*CELL_SIZE[0],OFFSET+BOARD_SIZE[0]*CELL_SIZE[0]),event.pos):
                        match game_stat:
                            case 1:
                                ret=myboard.toggle_flag(get_coord_from_click(click_coord=event.pos, cell_size=CELL_SIZE, OFFSET=OFFSET))
                                if ret==0xff:
                                    game_stat=3

if __name__=="__main__":
    main()