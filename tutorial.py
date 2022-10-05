import pygame
from pong import Game
import neat
import os
import pickle

# fitness of a genome - similar idea of natural selection - based off how well they perform our task, which will require a function for rating
# in this circumstance we are going to use the amount of times the ai paddle hits the ball
# have multiple generations, where the genomes can breed, taking qualities from multiple genomes to combine them, again testing the fitness of the new offspring
# there is the ability to introduce random mutations through to the offspring of successive generations


class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)
        self.left_paddle = self.game.right_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            game_info = self.game.loop()
            print(game_info.left_score, game_info.right_score)

            self.game.draw(True, False)
            pygame.display.update()


pygame.quit()

# neat training methodologies
#


def eval_genomes(genomes, config):
    pass


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-127")
    # use the above line if instead of starting from the beginning, you want neat to begin from a checkpoint
    # instead of the below code 'p=neat.Population(config)'
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )
    run_neat(config)
