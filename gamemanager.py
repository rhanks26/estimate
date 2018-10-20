import random

class GameManager(object):

    def __init__(self):
        self.quit = False

    def play(self):
        score = 0
        for i in range(3):
            num1 = random.randint(10, 100)
            num2 = random.randint(10, 100)
            user_input = input("{} x {} = ".format(num1,num2))
            ans = num1 * num2
            tenp = ans * .1
            fivep = ans * .05
            estimate = int(user_input)
            if estimate == ans:
                score += 10
                print("+10")
            elif estimate > ans - fivep and estimate < ans + fivep:
                score += 5
                print("+5")
            elif estimate > ans- tenp and estimate < ans + tenp:
                score += 3
                print("+3")

            print(estimate/ans * 100)

        print("Score is {}".format(score))



if __name__ == '__main__':
    game = GameManager()
    game.play()
