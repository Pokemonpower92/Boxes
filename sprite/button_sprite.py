import pygame
from utils import constants, controls


class ButtonSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        width=constants.BUTTON_WIDTH,
        height=constants.BUTTON_HEIGHT,
        color=constants.BUTTON_COLOR,
        center=constants.WINDOW_CENTER,
        **kwargs
    ):
        pygame.sprite.Sprite.__init__(self)

        self._width = width
        self._height = height
        self._color = color
        self._center = center

        for key, value in kwargs.items():
            setattr(self, "_" + key, value)

    def _check_for_press(self):
        mouse_pos = pygame.mouse.get_pos()

        if self._rect.collidepoint(mouse_pos):
            self._mouseover = True
            if pygame.mouse.get_pressed()[0] and self._can_click():
                self._clicked = True
                self._press_button()
        else:
            self._mouseover = False
            self._clicked = False

    def _can_click(self):
        current_time = pygame.time.get_ticks()
        internal_timer = (
            current_time - self._time_since_last_click
        ) > constants.BUTTON_PRESS_COOLDOWN

        if internal_timer and controls.CTRLS().can_press_button():
            self._time_since_last_click = pygame.time.get_ticks()
            return True

        return False

    def _press_button(self):
        self._command.execute()

    def custom_draw(self, surface):
        surface.blit(self._content, self._rect)

    def set_command(self, command):
        self._command = command

    def with_text(self, text: str):
        self._font = pygame.font.SysFont(None, 48)
        self._text = text
        self._content = self._font.render(
            self._text, True, constants.WHITE, self._color
        )
        return self

    def with_icon(self, icon: pygame.image):
        self._icon = icon
        return self

    def build(self):
        self._rect = self._content.get_rect()
        self._rect.width = self._width
        self._rect.height = self._height
        self._rect.center = self._center
        self._time_since_last_click = pygame.time.get_ticks()

        return self

    def update(self):
        self._check_for_press()
