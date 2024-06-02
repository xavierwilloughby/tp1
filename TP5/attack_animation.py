from enum import Enum
import arcade

class AttackType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.5
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type):
        super().__init__()
        self.attack_type = attack_type
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0

        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("assets/rock.png",center_x=100,center_y=100),
                arcade.load_texture("assets/rock_attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("assets/paper.png"),
                arcade.load_texture("assets/paper_attack.png"),
            ]
        else:
            self.textures = [
                arcade.load_texture("assets/scissors.png"),
                arcade.load_texture("assets/scissors_attack.png"),
            ]

        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def update(self, delta_time):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0
