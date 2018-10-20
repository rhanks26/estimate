import random

class GameManager(object):

    def __init__(self):
        self.quit = False

    def play(self):
        for i in range(3):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            user_input = input("{} x {} = ".format(num1,num2))
            ans = num1 * num2
            score = int(user_input)/ans * 100
            print(score)



if __name__ == '__main__':
    game = GameManager()
    game.play()
