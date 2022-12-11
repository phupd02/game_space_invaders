import pygame, sys

class Button:
    # gui_font = pygame.font.Font("comicsans", 30)
    # screen = pygame.display.set_mode((500, 500))
    # pos = (x, y)
    # elevation: decript action click mouse
    
    '''
    Input: Vị trí, Text, cửa sổ vẽ
    --> Gọi hàm draw để vẽ button lên cửa sổ tương ứng
    '''
    pygame.font.init()
    TEXT_FONT = pygame.font.SysFont("comicsans", 30)
    SCREEN = pygame.display.set_mode((650, 550))

    def __init__(self, text, width, height, pos, elevation):
        # Core attribute
        self.pressed = False # Kiểm tra đã nhấn chưa??
        self.elevation = elevation # Di chuyển hình chữ nhật
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top_rectange
        self.top_rect = pygame.Rect(pos, (width, height)) # vẽ hình chữ nhật bên trên
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#000000'

        # text
        self.text_surf = self.TEXT_FONT.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    
    def draw(self):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        
        pygame.draw.rect(self.SCREEN, self.bottom_color, self.bottom_rect, border_radius = 12)
        pygame.draw.rect(self.SCREEN, self.top_color, self.top_rect, border_radius = 12)
        self.SCREEN.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_collision(self): # check va chạm
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def check_click(self): # đổi màu và nhấn xuống
        if self.check_collision() == True:
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]: # left mouse = True
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:  
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'
       

# # Game loop
# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Button")
# clock = pygame.time.Clock()
# gui_font = pygame.font.SysFont("comicsans", 30)


# button1 = Button("click me", 200, 40, (200, 250), 5)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame .quit()
#             # sys.quit()
#     screen.fill("#DCDDD8")
#     button1.draw()

#     pygame.display.update()
#     clock.tick(60)
