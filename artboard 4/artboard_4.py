import pygame, sys

class GameState():            #Lớp các Scenes
	def __init__(self):
		self.state = "intro"

	def intro(self):       #Scene Intro
		screen = pygame.display.set_mode((width,height))
		screen.fill((255,255,255))

		screen_ = pygame.transform.scale(pygame.image.load("backround.png"), (width,height))
		screen.blit(screen_,(0, 0))

		playgame_button = pygame.transform.scale(pygame.image.load("playgame.png").convert_alpha(),(int(width/(34/15)), int(height/(34/11))))
		playgame_button_rect = playgame_button.get_rect(center = (int(width/(18/12)), int(height/2)))


		shop_button = pygame.transform.scale(pygame.image.load("shop.png").convert_alpha(),(int(width/(17/3)), int(height/(17/4))))
		shop_button_rect = shop_button.get_rect(center = (int(width/(34/9)), int(height/(17/6))))

		setting_button = pygame.transform.scale(pygame.image.load("button_setting.png").convert_alpha(),(int(width/12), int(height/10)))
		setting_button_rect = setting_button.get_rect(center = (int(width/(11/5)), int(height/12)))

		minigame_button = pygame.transform.scale(pygame.image.load("minigame.png").convert_alpha(),(int(width/(34/9)), int(height/(17/4))))
		minigame_button_rect = minigame_button.get_rect(center = (int(width/(35/11)), int(height/(17/11))))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       #Event click chuột
				pos = pygame.mouse.get_pos()              #Lấy tọa độ của chuột
				if shop_button_rect.collidepoint(pos):    #Hàm va chạm (collision)
					self.state = "shop"               #cái này giống như flag báo hiệu cho state_manager ở dưới
				if minigame_button_rect.collidepoint(pos):
					self.state = "minigame"
				if setting_button_rect.collidepoint(pos):
					self.state = "setting"
				if playgame_button_rect.collidepoint(pos):
					self.state = "playgame"
		
			
			screen.blit(shop_button,shop_button_rect)
			screen.blit(minigame_button,minigame_button_rect)
			screen.blit(setting_button,setting_button_rect)
			screen.blit(playgame_button, playgame_button_rect)

			pygame.display.update()

	def shop(self):            #Scene Game
		screen.fill((255,255,255))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("shop screen", False, (0, 128, 0))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def minigame(self):           #Scene Language
		screen.fill((0,0,0))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("minigame screen", False, (255, 255, 255))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def setting(self):           #Scene Language
		screen.fill((0,0,0))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("setting screen", False, (255, 255, 255))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def playgame(self):           #Scene Language
		screen.fill((0,0,0))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("playgame screen", False, (255, 255, 255))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def state_manager(self):             #Quản lý các Scene
		if self.state == "intro":        #Nếu mà state là "intro" thì chạy Scene Intro
			self.intro()
		if self.state == "shop":    #Nếu mà state là "main_game" thì chạy Scene game
			self.shop()
		if self.state == "setting":     #Nếu mà state là "language" thì chạy Scene Language
			self.setting()
		if self.state == "playgame":     #Nếu mà state là "language" thì chạy Scene Language
			self.playgame()
		if self.state == "minigame":     #Nếu mà state là "language" thì chạy Scene Language
			self.minigame()

pygame.init()
clock = pygame.time.Clock()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.set_caption("Test")

game_state = GameState()      #Cái này mình gán cái Class vào một object là game_state





while True:                          #Vòngy loop chính của cả game (bao gồm tất cả Scenes)
	game_state.state_manager()       #Mình là chạy cái nà để quản lý các Scenes
	clock.tick(30)
