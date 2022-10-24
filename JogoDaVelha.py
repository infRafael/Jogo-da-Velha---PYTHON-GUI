import pygame 
import time
pygame.init()
txt='hello world'                                 
pygame.font.init()                                
fonte = pygame.font.get_default_font()            
titulo = pygame.font.SysFont(fonte, 60)
texto = pygame.font.SysFont(fonte, 30)
pygame.display.set_caption("JOGO DA VELHA")

white = (255, 255, 255)
black = (0, 0, 0)
display = pygame.display.set_mode((600, 600))
ganhador = 0


def Jogo():
    i, ganhador, rodada = 0, 0, 1
    tabuleiro = [[0]*3,[0]*3,[0]*3]
    display.fill(white)
    pygame.draw.line(display, black, (200,0),(200,600),width=1)
    pygame.draw.line(display, black, (400,0),(400,600),width=1)
    pygame.draw.line(display, black, (0,200),(600,200),width=1)
    pygame.draw.line(display, black, (0,400),(600,400),width=1)
    pygame.display.update()
    while i < 9:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                
                if(pos[0] <= 200):
                    x = 0; 
                elif(pos[0] >= 200 and pos[0] <= 400):
                    x = 1
                elif(pos[0] >= 400):
                    x = 2        
                if(pos[1] <= 200):
                    y = 0;
                elif(pos[1] >= 200 and pos[1] <= 400):
                    y = 1
                elif(pos[1] >= 400):
                    y = 2

                if tabuleiro[y][x] == 0:
                    tabuleiro[y][x] = rodada
                    y = (y*2+1)*100
                    x = (x*2+1)*100
                    if(rodada == 1):
                        pygame.draw.line(display, black, (x-25,y-25),(x+25,y+25),width=1)
                        pygame.draw.line(display, black, (x+25,y-25),(x-25,y+25),width=1)
                    else:
                        pygame.draw.circle(display, black, (x,y), 40,width=1)
                    pygame.display.update()
                    rodada = (rodada % 2) + 1

                if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != 0:
                    ganhador = tabuleiro[0][0]
                elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != 0:
                    ganhador = tabuleiro[0][2]
                else:
                    for cont in range(3):
                        if tabuleiro[cont][0] == tabuleiro[cont][1] and tabuleiro[cont][1] == tabuleiro[cont][2] and tabuleiro[cont][0] != 0:
                            ganhador = tabuleiro[cont][0]
                        elif tabuleiro[0][cont] == tabuleiro[1][cont] and tabuleiro[1][cont] == tabuleiro[2][cont] and tabuleiro[0][cont] != 0:
                            ganhador = tabuleiro[0][cont]
                    
                
                if ganhador != 0:
                    i = 10
                i += 1
                
    if ganhador == 1:
        Validar(ganhador)
    elif ganhador == 2:
        Validar(ganhador)
    else:
        Validar(ganhador)


def Validar(ganhador):
    pygame.draw.rect(display, black, (100,225,400,150))
    pygame.draw.rect(display, white, (105,230,390,140))
    
    pygame.draw.rect(display, black, (140,310,120,40))
    pygame.draw.rect(display, black, (370,310,60,40))
    
    txt = texto.render('REINICIAR', 1, white, (0,0,0))
    display.blit(txt,(147,320))
    txt = texto.render('SAIR', 1, white, (0,0,0))  
    display.blit(txt,(375,320))

    if ganhador == 1:
        txt = titulo.render('X GANHOU', 1,(0,0,0))  
    elif ganhador == 2:
        txt = titulo.render('O GANHOU', 1,(0,0,0))  
    else:
        txt = titulo.render('    VELHA', 1,(0,0,0))  
        
    display.blit(txt,(190,250))
    pygame.display.update()
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if ((pos[0] >= 370 and pos[0] <= 430) and (pos[1] >= 310 and pos[1] <= 350)):
                    exit()
                elif ((pos[0] >= 140 and pos[0] <= 260) and (pos[1] >= 310 and pos[1] <= 350)):
                    Jogo()


display.fill(white)
pygame.draw.line(display, black, (200,0),(200,600),width=1)
pygame.draw.line(display, black, (400,0),(400,600),width=1)
pygame.draw.line(display, black, (0,200),(600,200),width=1)
pygame.draw.line(display, black, (0,400),(600,400),width=1)

        
pygame.draw.rect(display, black, (100,225,400,150))
pygame.draw.rect(display, white, (105,230,390,140))
    
pygame.draw.rect(display, black, (140,310,120,40))
pygame.draw.rect(display, black, (370,310,60,40))

txt = titulo.render('JOGO DA VELHA', 1, (0,0,0))
display.blit(txt,(130,250))
txt = texto.render('INICIAR', 1, white, (0,0,0))
display.blit(txt,(160,320))
txt = texto.render('SAIR', 1, white, (0,0,0))  
display.blit(txt,(375,320))

pygame.display.update()
while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if ((pos[0] >= 370 and pos[0] <= 430) and (pos[1] >= 310 and pos[1] <= 350)):
                    exit()
                elif ((pos[0] >= 140 and pos[0] <= 260) and (pos[1] >= 310 and pos[1] <= 350)):
                    Jogo()
