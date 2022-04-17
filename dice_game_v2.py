import random
from dice_game import Dice

class Dice_dif(Dice):
    """
    допишем режими игры в кости
    type 1: успех1 = совпадение обоих чисел
    type 2: успех2 = совпадение одного числа
    type 3: успех3 = совпадение суммы
    """
    def __init__(self, N, type):
        # super(Dice_dif, self).__init__()
        super().__init__(N)
        self.type_game = type

    def throw_dices(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        self.current_throw += 1
        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили кол-во попыток')

        if self.type_game == 1:
            if {dice_1, dice_2} == {self._hidden_num_1, self._hidden_num_2}:
                return True
            else:
                return False
        elif self.type_game == 2:
            if (dice_1 in {self._hidden_num_1, self._hidden_num_2}) or (dice_2 in {self._hidden_num_1, self._hidden_num_2}):
                print("Attemp:", dice_1, dice_2)
                return True
            else:
                return False
        elif self.type_game == 3:
            if (dice_1+dice_2) == (self._hidden_num_1+self._hidden_num_2):
                return True
            else:
                return False

if __name__ == '__main__':
    dice_game = Dice_dif(19, 3)
    dice_game.set_hidden_numbers()
    print(dice_game._hidden_num_1, dice_game._hidden_num_2)
    for i in range(20):
        try:
            print(dice_game.throw_dices())
        except:
            print('Game OVER')


