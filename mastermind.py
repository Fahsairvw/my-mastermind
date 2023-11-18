import random


class Answer:
    def __init__(self, x=6, y=4):
        self.color = x
        self.position = y
        self.answer = ''
        self.guess_n = 0
        self.position_n = 0
        self.color_n = 0

    def find_answer(self):
        self.answer = ''
        for i in range(self.position):
            self.answer += str(random.randint(1, self.color))
        print(self.answer)

    def play(self):
        self.find_answer()
        print(f'Playing Mastermind with {self.color} colors and {self.position} positions')
        self.guess_n = 0
        while True:
            self.position_n = 0
            self.color_n = 0
            guess = input('input: ')
            self.guess_n += 1
            if len(guess) != self.position:
                continue
            for i in range(len(self.answer)):
                if guess[i] == self.answer[i]:
                    self.position_n += 1

            set_guess = set(list(guess))
            for i in set_guess:
                n = min(guess.count(i), self.answer.count(i))
                self.color_n += n

            print('*' * self.position_n, 'o' * (self.color_n - self.position_n), '\n', sep='')

            if guess == self.answer:
                print(f'You solve it after {self.guess_n} rounds')
                break

        if input('Start new game:(y/n): ') == 'y':
            self.color = int(input('How many color: '))
            self.position = int(input('How many position: '))
            self.play()


color = int(input('How many color: '))
position = int(input('How many position: '))
game = Answer(color, position)
game.play()







