import random
import arcade
from game_state import GameState
from attack_animation import AttackType, AttackAnimation


class RockPaperScissors(arcade.Window):
    def __init__(self, width, height, title):
        #variable list
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.player_rock = arcade.Sprite("assets/rock.png",center_x=100,center_y=100)
        self.player_paper = arcade.Sprite("assets/paper.png",center_x=200,center_y=100)
        self.player_scissors = arcade.Sprite("assets/scissors.png",center_x=300,center_y=100)
        self.facebeard = arcade.Sprite("assets/facebeard.png",center_x=200,center_y=400,)
        self.set_mouse_visible(True)
        self.game_state = GameState.NOT_STARTED
        self.player_attack_type = None
        self.computer_attack_type = None
        self.player_score = 0
        self.computer_score = 0
        self.title="press space to start"
        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)

    def on_draw(self):
         # Draw game elements 
        arcade.start_render()
        self.player_rock.draw()
        self.player_paper.draw()
        self.player_scissors.draw()
        self.facebeard.draw()
        arcade.draw_text(f"Player Score: {self.player_score}", 100, 170, arcade.color.WHITE, 16)
        arcade.draw_text(f"Computer Score: {self.computer_score}", 1200, 170, arcade.color.WHITE, 16)
        arcade.draw_text(self.title, 650, 170, arcade.color.WHITE, 16)


    def on_key_press(self, key, modifiers):
        #start the game
        if key == arcade.key.SPACE:         
            if self.game_state == GameState.NOT_STARTED or self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.title =""
                self.player_score= 0
                self.computer_score= 0
                self.player_attack_selected = False
                self.computer_attack_type = False
            elif self.game_state == GameState.GAME_OVER:
                self.game_state = GameState.ROUND_ACTIVE


    def on_mouse_press(self, x, y, button, modifiers):
        # Handle player attack selection with mouse
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.player_rock.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
                self.player_attack_selected = True
            elif self.player_paper.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
                self.player_attack_selected = True
            elif self.player_scissors.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
                self.player_attack_selected = True
        
        # Determine the winner if both player and computer have made their choices
        if self.player_attack_selected:
            self.computer_attack_type = random.choice([AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS])
            self.determine_winner()

    def determine_winner(self):
        # Determine the winner based on the player's and computer's choices
        if self.player_attack_type == self.computer_attack_type:
            # It's a tie
            self.title="its a tie!"
        elif (self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS) or \
             (self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK) or \
             (self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER):
            # Player wins
            self.title="You win!"
            self.player_score += 1
        else:
            # Computer wins
            self.title="Computer wins!"
            self.computer_score += 1
        if self.computer_score == 3 :
            self.computer_score = 0
            self.player_score = 0
            self.game_state == GameState.ROUND_DONE
            self.title= "you lose the game"
            self.player_attack_selected= False
            self.computer_attack_type= False
        elif self.player_score == 3 :
            self.computer_score = 0
            self.player_score = 0
            self.game_state ==GameState.ROUND_DONE
            self.title= "you win the game"
            self.player_attack_selected= False
            self.computer_attack_type= False







def main():
    window = RockPaperScissors(1500, 600, "Rock Paper Scissors")
    arcade.run()

if __name__ == "__main__":
    main()
