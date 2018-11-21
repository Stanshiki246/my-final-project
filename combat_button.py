import pygame
pygame.init()
class Button:
    def __init__(self,screen,rectx,recty,width,height,text):
        """Initialize button attributes."""
        self.screen = screen
        self.rectx = rectx
        self.recty = recty

        # Set the dimensions and properties of the button.
        self.width, self.height = width,height
        self.button_color = (200, 200, 200)
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont("Verdana", 36)

        # Build the button's rect object.
        self.rect = pygame.Rect(self.rectx, self.recty, self.width, self.height)

        # The button message only needs to be prepped once.
        self.show_text(text)

    def show_text(self,text):
        """Turn msg into a rendered image, and center text on the button."""
        self.text_rendering = self.font.render(text, True, self.text_color,
            self.button_color)
        self.text_rendering_rectx = self.rectx+25
        self.text_rendering_recty = self.recty
        self.text_rendering_rect = (self.text_rendering_rectx,self.text_rendering_recty)

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_rendering, self.text_rendering_rect)
