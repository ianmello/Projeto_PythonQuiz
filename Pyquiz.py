


from ast import If
from csv import QUOTE_NONNUMERIC
from telnetlib import PRAGMA_HEARTBEAT, SE
from pip import main
import pygame, sys
from button import Button
import time

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")
PY = pygame.image.load("python.png")
CD = pygame.image.load("code1.png")
PG = pygame.image.load("levelp.png")
SL = pygame.image.load("selectl.png")
LVL = pygame.image.load("level.png")
BKP = pygame.image.load("backpontos.png")
RANK = pygame.image.load("DISPLAY.png")
TELARANK = pygame.image.load("telarank.png")
PRATA = pygame.image.load("prata.png")
FERRO = pygame.image.load("ferro.png")
BRONZE = pygame.image.load("bronze.png")
OURO = pygame.image.load("ouro.png")
PLATINA = pygame.image.load("platina.png")
SEMRANK = pygame.image.load("semrank.png")
CORRETO = pygame.image.load("corretocheck.png")
ERRADO = pygame.image.load("errado.png")
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Dreamland Std Regular.otf", size)
def get_fontpergunta(size):
        return pygame.font.Font("pixelmix.ttf", size)
def get_fontresp(size):
        return pygame.font.Font("DS-DIGIB.TTF", size)
def get_fontselect(size):
        return pygame.font.Font("Gumball.ttf", size)
def get_fontlevel(size):
        return pygame.font.Font("upheavtt.ttf", size)
def get_fontrank(size):
        return pygame.font.Font("Valorant Font.ttf", size)       


questions = [["Para que serve a funcao type? "], [" Mostrar o tipo de dado" , "Escolher o tipo de um dado", "Mudar o tipo do dado", "Verificar o dado"],
             ["Pra que serve a / em Python ?"], ["Fazer um comentario", "Separar linhas","Realizar uma divisao", "Iniciar uma indexacao"],
             ["Qual NAO eh uma estrutura condicional em Python?"], ["if", "elif","for", "else"],
             ["Para o calculo de potencia, em Python, usa-se?"], ["*", "x ","**", "*2"], 
             ["Em Python para que serve a funcao print ?"], ["Tirar uma print do programa", "Exibir uma print na tela ","Exibir uma mensagem na tela", "Colar algo na tela"]]

questions2 = [["Quais sao operadores logico, em Python? "], [" in, for e and" , "and, or e not ","else, if e and",  "elif, not e while"],
              ["Em Python, utiliza-se para representar string? "], [" %(Porcento) " , " ''(Aspas) ","@(Arroba)",  " //(Barras) "],
              ["Quais das variaveis eh valida em Python? "], ["99garrafas" ,"vendas_anuais", "Ano Fiscal ","#2021julho"],
              ["Qual a estrutura cujos valores sao imutaveis? "], ["Lista ","Tupla", "Classe", "String"],
              ["Qual das palavras reservadas NAO existe em Python? "], [ "raise","new","while",  "not"]]

pergunta = 0
qnum = 1
pontos = 0
def proxima_questao():
    global pontos, qnum, pergunta
    pontos = pontos
    qnum += 2 
    pergunta += 2
    while True: 
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(PG, (0, 0))
        if pergunta == len(questions):
            if pontos >= 3:
                score(pontos)
                desafio1()
            mostra_pontos()
        PERGUNTA2 = get_font(35).render(questions[pergunta][0], True, "White")
        PLAY_RECT2 = PERGUNTA2.get_rect(center=(610, 150))
        SCREEN.blit(PERGUNTA2, PLAY_RECT2)
        
        
        A = Button(image=None, pos=(295, 420), 
                            text_input= questions[qnum][0], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = questions[qnum][1], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = questions[qnum][2], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= questions[qnum][3], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        
        A.changeColor(PLAY_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(PLAY_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(PLAY_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(PLAY_MOUSE_POS)
        D.update(SCREEN)
        time.sleep(.1)
        score(pontos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.checkForInput(PLAY_MOUSE_POS):
                    proxima_questao() 
                if B.checkForInput(PLAY_MOUSE_POS):
                    proxima_questao()               
                if C.checkForInput(PLAY_MOUSE_POS):               
                    questao2() 
                if D.checkForInput(PLAY_MOUSE_POS):               
                    proxima_questao()     
        pygame.display.update()
def questao2():
    global pontos, qnum, pergunta
    pontos += 1
    qnum += 2 
    pergunta += 2
    while True: 
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(PG, (0, 0))
        if pergunta == len(questions):
            if pontos >= 3:
                score(pontos)
                desafio1()
            mostra_pontos()
        PERGUNTA2 = get_font(35).render(questions[pergunta][0], True, "White")
        PLAY_RECT2 = PERGUNTA2.get_rect(center=(610, 150))
        SCREEN.blit(PERGUNTA2, PLAY_RECT2)
        
        A = Button(image=None, pos=(300, 420), 
                            text_input= questions[qnum][0], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = questions[qnum][1], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(300, 610), 
                            text_input = questions[qnum][2], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= questions[qnum][3], font=get_fontresp(21), base_color="yellow", hovering_color="green")
        
        A.changeColor(PLAY_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(PLAY_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(PLAY_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(PLAY_MOUSE_POS)
        D.update(SCREEN)
        time.sleep(.1)
        score(pontos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if A.checkForInput(PLAY_MOUSE_POS):
                        proxima_questao() 
                    if B.checkForInput(PLAY_MOUSE_POS):
                        proxima_questao()               
                    if C.checkForInput(PLAY_MOUSE_POS):               
                        questao2() 
                    if D.checkForInput(PLAY_MOUSE_POS):               
                        proxima_questao()     
        pygame.display.update()

pergunta2 = 0
qnum2 = 1
pontos2 = 0
def proxima_questao2():
    global pontos2, qnum2, pergunta2
    pontos2 = pontos2
    qnum2 += 2 
    pergunta2 += 2
    while True: 
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(PG, (0, 0))
        if pergunta2 == len(questions):
            if pontos2 >= 3:
                score(pontos2)
                desafio2()
            mostra_pontos2()
        PERGUNTA2 = get_font(35).render(questions2[pergunta2][0], True, "White")
        PLAY_RECT2 = PERGUNTA2.get_rect(center=(610, 150))
        SCREEN.blit(PERGUNTA2, PLAY_RECT2)
        
        A = Button(image=None, pos=(290, 420), 
                            text_input= questions2[qnum2][0], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = questions2[qnum2][1], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = questions2[qnum2][2], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= questions2[qnum2][3], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        
        A.changeColor(PLAY_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(PLAY_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(PLAY_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(PLAY_MOUSE_POS)
        D.update(SCREEN)
        time.sleep(.1)
        score(pontos2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.checkForInput(PLAY_MOUSE_POS):
                    proxima_questao2() 
                if B.checkForInput(PLAY_MOUSE_POS):
                    questao3() 
                if C.checkForInput(PLAY_MOUSE_POS):               
                    proxima_questao2()               
                if D.checkForInput(PLAY_MOUSE_POS):               
                    proxima_questao2()     
        pygame.display.update()
def questao3():
    global pontos2, qnum2, pergunta2
    pontos2 += 1
    qnum2 += 2 
    pergunta2 += 2
    while True: 
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(PG, (0, 0))
        if pergunta2 == len(questions):
            if pontos2 >= 3:
                score(pontos2)
                desafio2()
            mostra_pontos2()
        PERGUNTA2 = get_font(35).render(questions2[pergunta2][0], True, "White")
        PLAY_RECT2 = PERGUNTA2.get_rect(center=(610, 150))
        SCREEN.blit(PERGUNTA2, PLAY_RECT2)
        
        A = Button(image=None, pos=(290, 420), 
                            text_input= questions2[qnum2][0], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = questions2[qnum2][1], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = questions2[qnum2][2], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= questions2[qnum2][3], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        
        A.changeColor(PLAY_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(PLAY_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(PLAY_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(PLAY_MOUSE_POS)
        D.update(SCREEN)
        time.sleep(.1)
        score(pontos2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if A.checkForInput(PLAY_MOUSE_POS):
                        proxima_questao2() 
                    if B.checkForInput(PLAY_MOUSE_POS):
                        questao3() 
                    if C.checkForInput(PLAY_MOUSE_POS):               
                        proxima_questao2()               
                    if D.checkForInput(PLAY_MOUSE_POS):               
                        proxima_questao2()     
        pygame.display.update()
       
def score(score):
    texto = get_fontrank(40).render("Score:"+str(score), True, "Black")
    SCREEN.blit(texto, (0, 0))
rank = ''
rank2 = '' 

def mostra_pontos():
    global rank
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BKP, (0, 0))
        TELA_PONTOS = Button(image=None, pos=(640, 180), 
                                    text_input= f"SUA PONTUACAO FOI DE: {pontos} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        if pontos == 1:
            rank = 'Ferro'
        elif pontos == 2:
            rank = 'Bronze'
        elif pontos == 3:
            rank = 'Prata'
        elif pontos == 4:
            rank = 'Ouro'
        elif pontos == 5:
            rank = 'Platina'
        else :
            rank = 'Sem rank'
        TELA_RANK = Button(image=None, pos=(640, 270), 
                                    text_input=f"SEU RANK SERÁ: {rank} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_PONTOS.update(SCREEN)
        TELA_RANK.update(SCREEN)
        BACK = Button(image=None, pos=(640, 450), 
                            text_input="BACK", font=get_fontlevel(75), base_color="White", hovering_color="Green")
        BACK.changeColor(LEVEL_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LEVEL_MOUSE_POS):
                    select_level()
            pygame.display.update()
    
def mostra_pontos2():
    global rank2
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BKP, (0, 0))
        TELA_PONTOS = Button(image=None, pos=(640, 180), 
                                    text_input= f"SUA PONTUACAO FOI DE: {pontos2} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        if pontos2 == 1:
            rank2 = 'Ferro'
        elif pontos2 == 2:
            rank2 = 'Bronze'
        elif pontos2 == 3:
            rank2 = 'Prata'
        elif pontos2 == 4:
            rank2 = 'Ouro'
        elif pontos2 == 5:
            rank2 = 'Platina'
        else :
            rank2 = 'Sem rank'
        TELA_RANK = Button(image=None, pos=(640, 270), 
                                    text_input=f"SEU RANK SERÁ: {rank2} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_PONTOS.update(SCREEN)
        TELA_RANK.update(SCREEN)
        BACK = Button(image=None, pos=(640, 450), 
                            text_input="BACK", font=get_fontlevel(75), base_color="White", hovering_color="Green")
        BACK.changeColor(LEVEL_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LEVEL_MOUSE_POS):
                    select_level()
            pygame.display.update() 

def mostra_pontosdes1():
    global rank
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BKP, (0, 0))
        TELA_PONTOS = Button(image=None, pos=(640, 180), 
                                    text_input= f"SUA PONTUACAO FOI DE: {pontos} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_DESC = Button(image=None, pos=(640, 80), text_input= f"DESAFIO CORRETO ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        if pontos == 1:
            rank = 'Ferro'
        elif pontos == 2:
            rank = 'Bronze'
        elif pontos == 3:
            rank = 'Prata'
        elif pontos == 4:
            rank = 'Ouro'
        elif pontos == 5:
            rank = 'Platina'
        else:
            rank = 'Sem rank'
        TELA_RANK = Button(image=None, pos=(640, 270), 
                                    text_input=f"SEU RANK SERÁ: {rank} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_PONTOS.update(SCREEN)
        TELA_RANK.update(SCREEN)
        TELA_DESC.update(SCREEN)
        SCREEN.blit(CORRETO, (960,47))
        BACK = Button(image=None, pos=(640, 450), 
                            text_input="BACK", font=get_fontlevel(75), base_color="White", hovering_color="Green")
        BACK.changeColor(LEVEL_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LEVEL_MOUSE_POS):
                    select_level()
            pygame.display.update() 
    
    

def mostra_pontosdes2():
    global rank2
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BKP, (0, 0))
        TELA_PONTOS = Button(image=None, pos=(640, 180), 
                                    text_input= f"SUA PONTUACAO FOI DE: {pontos2} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_DESC = Button(image=None, pos=(640, 80), text_input= f"DESAFIO CORRETO ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        if pontos2 == 1:
            rank2 = 'Ferro'
        elif pontos2 == 2:
            rank2 = 'Bronze'
        elif pontos2 == 3:
            rank2 = 'Prata'
        elif pontos2 == 4:
            rank2 = 'Ouro'
        elif pontos2 == 5:
            rank2 = 'Platina'
        else :
            rank2 = 'Sem rank'
        TELA_RANK = Button(image=None, pos=(640, 270), 
                                    text_input=f"SEU RANK SERÁ: {rank2} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_PONTOS.update(SCREEN)
        TELA_RANK.update(SCREEN)
        TELA_DESC.update(SCREEN)
        SCREEN.blit(CORRETO, (960,47))
        BACK = Button(image=None, pos=(640, 450), 
                            text_input="BACK", font=get_fontlevel(75), base_color="White", hovering_color="Green")
        BACK.changeColor(LEVEL_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LEVEL_MOUSE_POS):
                    select_level()
            pygame.display.update() 
    

def erro_des1():
    global rank
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BKP, (0, 0))
        TELA_PONTOS = Button(image=None, pos=(640, 180), 
                                    text_input= f"SUA PONTUACAO FOI DE: {pontos} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_DESC = Button(image=None, pos=(640, 80), text_input= f"DESAFIO INCORRETO ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        if pontos == 1:
            rank = 'Ferro'
        elif pontos == 2:
            rank = 'Bronze'
        elif pontos == 3:
            rank = 'Prata'
        elif pontos == 4:
            rank = 'Ouro'
        elif pontos == 5:
            rank = 'Platina'
        else:
            rank = 'Sem rank'
        TELA_RANK = Button(image=None, pos=(640, 270), 
                                    text_input=f"SEU RANK SERÁ: {rank} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_PONTOS.update(SCREEN)
        TELA_RANK.update(SCREEN)
        TELA_DESC.update(SCREEN)
        SCREEN.blit(ERRADO, (1010,55))
        BACK = Button(image=None, pos=(640, 450), 
                            text_input="BACK", font=get_fontlevel(75), base_color="White", hovering_color="Green")
        BACK.changeColor(LEVEL_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LEVEL_MOUSE_POS):
                    select_level()
            pygame.display.update() 

def erro_des2():
    global rank2
    while True:
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BKP, (0, 0))
        TELA_PONTOS = Button(image=None, pos=(640, 180), 
                                    text_input= f"SUA PONTUACAO FOI DE: {pontos2} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_DESC = Button(image=None, pos=(640, 80), text_input= f"DESAFIO INCORRETO ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        if pontos2 == 1:
            rank2 = 'Ferro'
        elif pontos2 == 2:
            rank2 = 'Bronze'
        elif pontos2 == 3:
            rank2 = 'Prata'
        elif pontos2 == 4:
            rank2 = 'Ouro'
        elif pontos2 == 5:
            rank2 = 'Platina'
        else:
            rank2 = 'Sem rank'
        TELA_RANK = Button(image=None, pos=(640, 270), 
                                    text_input=f"SEU RANK SERÁ: {rank2} ", font=get_fontlevel(75), base_color="#d7fcd4", hovering_color="#d7fcd4")
        TELA_PONTOS.update(SCREEN)
        TELA_RANK.update(SCREEN)
        TELA_DESC.update(SCREEN)
        SCREEN.blit(ERRADO, (1010,55))
        BACK = Button(image=None, pos=(640, 450), 
                            text_input="BACK", font=get_fontlevel(75), base_color="White", hovering_color="Green")
        BACK.changeColor(LEVEL_MOUSE_POS)
        BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(LEVEL_MOUSE_POS):
                    select_level()
            pygame.display.update() 
    
    
def play2():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(PG, (0, 0))
        
        PERGUNTA1 = get_font(35).render(questions2[0][0], True, "White")
        PLAY_RECT1 = PERGUNTA1.get_rect(center=(610, 150))
        SCREEN.blit(PERGUNTA1, PLAY_RECT1)

        A = Button(image=None, pos=(290, 420), 
                            text_input= questions2[1][0], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = questions2[1][1], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = questions2[1][2], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= questions2[1][3], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        
        score(pontos2)
        A.changeColor(PLAY_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(PLAY_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(PLAY_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(PLAY_MOUSE_POS)
        D.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.checkForInput(PLAY_MOUSE_POS):
                    proxima_questao2() 
                if B.checkForInput(PLAY_MOUSE_POS):
                    questao3()
                if C.checkForInput(PLAY_MOUSE_POS):               
                    proxima_questao2()               
                if D.checkForInput(PLAY_MOUSE_POS):               
                    proxima_questao2()               
        
            
                    
        pygame.display.update()

def desafio1():
    while True:
        DES_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(PG, (0, 0))
        
        DESAFIO = get_fontselect(60).render("DESAFIO", True, "White")
        PERGUNTA1 = get_font(35).render("Print(4.00/(2.0+2.0))", True, "White")
        PERGUNTA2 = get_font(35).render("Qual o resultado dessa expressao?", True, "White")
        DES_RECT = DESAFIO.get_rect(center=(610, 110))
        PLAY_RECT1 = PERGUNTA1.get_rect(center=(610, 170))
        PLAY_RECT2 = PERGUNTA2.get_rect(center=(610, 210))
        SCREEN.blit(PERGUNTA1, PLAY_RECT1)
        SCREEN.blit(PERGUNTA2, PLAY_RECT2)
        SCREEN.blit(DESAFIO, DES_RECT)

        A = Button(image=None, pos=(290, 420), 
                            text_input= "1.0", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = "2", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = "0", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= "4", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        
        A.changeColor(DES_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(DES_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(DES_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(DES_MOUSE_POS)
        D.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.checkForInput(DES_MOUSE_POS):
                    mostra_pontosdes1()
                if B.checkForInput(DES_MOUSE_POS):
                    erro_des1()
                if C.checkForInput(DES_MOUSE_POS):               
                    erro_des1()
                if D.checkForInput(DES_MOUSE_POS):               
                    erro_des1()
                    
        pygame.display.update()
        

def desafio2():
    while True:
        DES_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(PG, (0, 0))
        
        DESAFIO = get_fontselect(60).render("DESAFIO", True, "White")
        PERGUNTA1 = get_font(35).render("x = [1,2,3,4] Print(x[-1])", True, "White")
        PERGUNTA2 = get_font(35).render("Qual o resultado dessa expressao?", True, "White")
        DES_RECT = DESAFIO.get_rect(center=(610, 110))
        PLAY_RECT1 = PERGUNTA1.get_rect(center=(610, 170))
        PLAY_RECT2 = PERGUNTA2.get_rect(center=(610, 210))
        SCREEN.blit(PERGUNTA1, PLAY_RECT1)
        SCREEN.blit(PERGUNTA2, PLAY_RECT2)
        SCREEN.blit(DESAFIO, DES_RECT)

        A = Button(image=None, pos=(290, 420), 
                            text_input= "1", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = "[1,2,3]", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = "[4,3,2,1]", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= "4", font=get_fontresp(22), base_color="yellow", hovering_color="green")
        
        A.changeColor(DES_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(DES_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(DES_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(DES_MOUSE_POS)
        D.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.checkForInput(DES_MOUSE_POS):
                    erro_des2()
                if B.checkForInput(DES_MOUSE_POS):
                    erro_des2()
                if C.checkForInput(DES_MOUSE_POS):               
                    erro_des2()
                if D.checkForInput(DES_MOUSE_POS):               
                    erro_des2()
                    
        pygame.display.update()
        
def play():
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(PG, (0, 0))
        
        PERGUNTA1 = get_font(35).render(questions[0][0], True, "White")
        PLAY_RECT1 = PERGUNTA1.get_rect(center=(610, 150))
        SCREEN.blit(PERGUNTA1, PLAY_RECT1)

        A = Button(image=None, pos=(290, 420), 
                            text_input= questions[1][1], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        B = Button(image=None, pos=(910, 420), 
                            text_input = questions[1][3], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        C = Button(image=None, pos=(295, 610), 
                            text_input = questions[1][0], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        D = Button(image=None, pos=(910, 595), 
                            text_input= questions[1][2], font=get_fontresp(22), base_color="yellow", hovering_color="green")
        
        score(pontos)
        A.changeColor(PLAY_MOUSE_POS)
        A.update(SCREEN)
        B.changeColor(PLAY_MOUSE_POS)
        B.update(SCREEN)
        C.changeColor(PLAY_MOUSE_POS)
        C.update(SCREEN)
        D.changeColor(PLAY_MOUSE_POS)
        D.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A.checkForInput(PLAY_MOUSE_POS):
                    proxima_questao()
                if B.checkForInput(PLAY_MOUSE_POS):
                    proxima_questao()               
                if C.checkForInput(PLAY_MOUSE_POS):               
                    questao2()
                if D.checkForInput(PLAY_MOUSE_POS):               
                    proxima_questao()               
        
            
                    
        pygame.display.update()
    
def select_level():
    global pontos, pontos2, qnum, qnum2, pergunta, pergunta2
    while True:
        LEVEL__MOUSE_POS = pygame.mouse.get_pos()    
        SCREEN.fill("purple")
        SCREEN.blit(SL, (-50, 20))
        SCREEN.blit(LVL, (3, -10))
        SCREEN.blit(LVL, (100, -10))
        SCREEN.blit(RANK, (300, 290))
        
        
        SELECT = get_fontselect(55).render("SELECIONE O LEVEL?", True, "White")
        SELECT_RECT = SELECT.get_rect(center=(610, 145))
        SCREEN.blit(SELECT, SELECT_RECT)
        
        q1 =  Button(image=None, pos=(365, 405), 
                             text_input="1", font=get_fontlevel(70), base_color="white", hovering_color="green")
        q2 =  Button(image=None, pos=(462, 405), 
                             text_input="2", font=get_fontlevel(70), base_color="white", hovering_color="green")
        BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_fontlevel(75), base_color="Black", hovering_color="Green")
        RANKS = Button(image=None, pos=(1000, 540), 
                            text_input="RANK", font=get_fontlevel(65), base_color="Black", hovering_color="Green")
        
        RANKS.changeColor(LEVEL__MOUSE_POS)
        RANKS.update(SCREEN)
        BACK.changeColor(LEVEL__MOUSE_POS)
        BACK.update(SCREEN)
        
        q1.changeColor(LEVEL__MOUSE_POS)
        q1.update(SCREEN)
        q2.changeColor(LEVEL__MOUSE_POS)
        q2.update(SCREEN)
        BACK.changeColor(LEVEL__MOUSE_POS)
        BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if q1.checkForInput(LEVEL__MOUSE_POS):
                    pontos = 0
                    qnum = 1
                    pergunta = 0
                    play()
                if  q2.checkForInput(LEVEL__MOUSE_POS):
                    pontos2= 0
                    qnum2 = 1
                    pergunta2 = 0
                    play2()
                if BACK.checkForInput(LEVEL__MOUSE_POS):
                    main_menu()
                if RANKS.checkForInput(LEVEL__MOUSE_POS):
                    ranks()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()          
        pygame.display.update()   
def ranks():
    while True:
        RANK_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(TELARANK,(0,0))
        

        RANK_TEXT = get_fontrank(50).render("Seu rank atual é", True, 'White')
        RANKLVL1 = get_fontrank(50).render("LEVEL 1", True, 'White')
        RANKLVL2 = get_fontrank(50).render("LEVEL 2", True, 'White')
        SEU_RANK = get_fontrank(50).render(f"{rank}", True, 'White')
        SEU_RANK2 = get_fontrank(50).render(f"{rank2}", True, 'White')      
        if rank == "Ferro":
            SCREEN.blit(FERRO,(340,355))
        elif rank == "Bronze":
            SCREEN.blit(BRONZE,(340,355))
        elif rank == "Prata":
            SCREEN.blit(PRATA,(340,355))
        elif rank == "Ouro":
            SCREEN.blit(OURO,(340,355))
        elif rank == "Platina":
            SCREEN.blit(PLATINA,(340,355))
        elif pontos == 0:
            SCREEN.blit(SEMRANK,(340,355))    
            
        if rank2 == "Ferro":
            SCREEN.blit(FERRO, (830, 355))
        elif rank2 == "Bronze":
            SCREEN.blit(BRONZE,(830,355))
        elif rank2 == "Prata":
            SCREEN.blit(PRATA,(830,355))
        elif rank2 == "Ouro":
            SCREEN.blit(OURO,(830,355))
        elif rank2 == "Platina":
            SCREEN.blit(PLATINA,(830,355))
        elif pontos2 == 0:
            SCREEN.blit(SEMRANK,(830,355))    
                    
        RANK_RECT = RANK_TEXT.get_rect(center=(640, 120))
        RECT = SEU_RANK.get_rect(center=(400, 300))
        RECT2 = SEU_RANK2.get_rect(center=(890, 300))
        RECTLVL1 = RANKLVL1.get_rect(center=(400, 200))
        RECTLVL2 = RANKLVL2.get_rect(center=(890, 200))
        SCREEN.blit(RANK_TEXT, RANK_RECT)
        SCREEN.blit(SEU_RANK, RECT)
        SCREEN.blit(SEU_RANK2, RECT2)
        SCREEN.blit(RANKLVL1, RECTLVL1)
        SCREEN.blit(RANKLVL2, RECTLVL2)
        RANK_BACK = Button(image=None, pos=(610, 640), 
                            text_input =  'BACK', font=get_fontrank(75), base_color="Black", hovering_color="Green")
        
        RANK_BACK.changeColor(RANK_MOUSE_POS)
        RANK_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RANK_BACK.checkForInput(RANK_MOUSE_POS):
                    select_level()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        select_level()        

        pygame.display.update()
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(45).render("As regras do jogo se baseam em um jogo de perguntas e respostas,", True, "white")
        OPTIONS_2TEXT = get_font(45).render("onde existem 4 alternativas e, apenas, uma é a correta.", True, "white")
        OPTIONS_3TEXT = get_font(45).render("A cada pergunta correta, um ponto será adicionado ao jogador,", True, "white")
        OPTIONS_4TEXT = get_font(41).render("ao final de cada nível, a pontuação será somada e será determinado o ranking.", True, "white")
        OPTIONS_5TEXT = get_font(41).render("Se o jogador tiver pontuação acima ou igual a 3 será apresentado um desafio.", True, "white")
        
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 120))
        OPTIONS_2RECT = OPTIONS_2TEXT.get_rect(center=(640, 170))
        OPTIONS_3RECT = OPTIONS_3TEXT.get_rect(center=(640, 220))
        OPTIONS_4RECT = OPTIONS_4TEXT.get_rect(center=(640, 270))
        OPTIONS_5RECT = OPTIONS_5TEXT.get_rect(center=(640, 320))

        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_2TEXT, OPTIONS_2RECT)
        SCREEN.blit(OPTIONS_3TEXT, OPTIONS_3RECT)
        SCREEN.blit(OPTIONS_4TEXT, OPTIONS_4RECT)
        SCREEN.blit(OPTIONS_5TEXT, OPTIONS_5RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu()        

        pygame.display.update()
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render('''Bem-vindo ao Pyquiz''', True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("j2.png"), pos=(640, 250), 
                            text_input="JOGAR", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("j2.png"), pos=(640, 400), 
                            text_input="REGRAS", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("j2.png"), pos=(640, 550), 
                            text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(PY,(-370, -200))
        SCREEN.blit(CD,(780,200 ))
        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select_level()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
               

        pygame.display.update()
from PyQt5 import  uic,QtWidgets
import sqlite3
import re

def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE email = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        banco.close()
    except:
        print("Erro ao buscar senha")
    if senha == senha_bd[0][0]:
        primeira_tela.close()
        main_menu()
    else:
        primeira_tela.label_3.setText("Dados de login incorretos")
        primeira_tela.label_3.setStyleSheet("color: red")

def logout_cadastro():
    tela_cadastro.close()
    primeira_tela.show()
def erro_email():
    tela_cadastro.close()
    tela_cadastro.show()
def abre_tela_cadastro():
    tela_cadastro.show()
def sair_banco():
    banco = sqlite3.connect('banco_cadastro.db')
    banco.close()
def cadastrar():  
    
    email = tela_cadastro.lineEdit.text()
    senha = tela_cadastro.lineEdit_2.text()
    c_senha = tela_cadastro.lineEdit_3.text()
    if email.endswith('@maua.br')== True:
        if (len(senha)< 4):
            tela_cadastro.label_5.setStyleSheet("color: red")
            tela_cadastro.label_5.setText('Comprimento de senha pequeno demais.')  
        else:
            if (senha == c_senha):
                try:
                    banco = sqlite3.connect('banco_cadastro.db') 
                    cursor = banco.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (email text,senha text)")
                    cursor.execute("INSERT INTO cadastro VALUES ('"+email+"','"+senha+"')")

                    banco.commit() 
                    banco.close()
                    tela_cadastro.pushButton.clicked.connect(logout_cadastro)

                except sqlite3.Error as erro:
                    tela_cadastro.label_6.setText('Conta já existente.')
                    tela_cadastro.label_6.setStyleSheet("color: red")
            else:
                tela_cadastro.label_5.setStyleSheet("color: red")
                tela_cadastro.label_5.setText('As senhas digitadas estão diferentes.')
    else:
        tela_cadastro.pushButton.clicked.connect(erro_email)
        tela_cadastro.label_6.setText('Email inserido incorreto(deve ser @maua.br)')
        tela_cadastro.label_6.setStyleSheet("color: red")

   

    


app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
primeira_tela.setWindowTitle("Login")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
tela_cadastro.setWindowTitle("Cadastro")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)



primeira_tela.show()
app.exec()

main_menu()