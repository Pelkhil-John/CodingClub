import pygame

class Player(pygame.sprite.Sprite):
    """
    """

    rect: pygame.rect.Rect
    color: pygame.Color
    on_screen: bool
    health: int
    mana: int
    defence: int
    power: int
    experience: int
    level: int
    class_type: str

    def __init__(self, rect, *groups):
        self.rect = rect
        self.color = pygame.color.Color("blue")
        self.on_screen = True
        self.health = 100
        self.mana = 10
        self.defence = 0
        self.power = 1
        self.experience = 0
        self.level = 0
        self.class_type = "none"

    def load(self, save_dict):
        """
        
        TODO: add tryblocks to prevent save corruption
        """
        rect = self.rect_loader(save_dict["rect"])
        color = self.color_loader(save_dict["color"])
        on_screen = save_dict["on_screen"]
        health = save_dict["health"]
        mana = save_dict["mana"]
        defence = save_dict["defence"]
        power = save_dict["power"]
        experience = save_dict["experience"]
        level = save_dict["level"]

    def rect_loader(rect_save):
        """ for loading the converted/ overridden string cast for rect.
        
        :param rect_save: list(left(float),top(float),width(float),height(float))
        """
        return pygame.rect.Rect(rect_save[0], rect_save[1], rect_save[2], rect_save[3])
    
    def color_loader(color_save) -> pygame.color.Color:
        """ for loading the converted/overriden string cast for color
        
        :param color_save: list(r(int), g(int), b(int))
        """
        return pygame.color.Color(color_save[0], color_save[1], color_save[2])
        
    def get(self, variable):
        # pygame.Rect, string cast does not play nice with json so this fixes it
        if (variable == "rect"):
            return [self.rect.left, self.rect.top, self.rect.width, self.rect.height]
        if (variable == "color"):
            return [self.color.r, self.color.g, self.color.b]
        return eval(variable, globals(), self.__dict__)