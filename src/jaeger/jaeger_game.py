from player import Player
import random


class JaegerGame:
    def __init__(self, players: list):
        self.players = players
        self.current_player = players[0]

        self.result_dict = {
            [1, 1]: 'bak',
            [2, 1]: 'mex',
            [2, 2]: 'double_prev',
            [3, 1]: 'choose',
            [3, 2]: 0,
            [3, 3]: {1, 'double_next'},
            [4, 1]: 0,
            [4, 2]: 1,
            [4, 3]: 0,
            [4, 4]: 'next',
            [5, 1]: 1,
            [5, 2]: 0,
            [5, 3]: 0,
            [5, 4]: 1,
            [5, 5]: 'prev',
            [6, 1]: 1,
            [6, 2]: 1,
            [6, 3]: 2,
            [6, 4]: 1,
            [6, 5]: 1,
            [6, 6]: 'bak'
        }

    def round(self, player: Player) -> None:
        print("{} is aan de beurt.".format(player.name))

        turn_over = False
        while not turn_over:
            result = self.throw()
            turn_over = self.process_throw(result, player)

    def throw(self) -> list:
        dice = [random.randint(1, 6), random.randint(1, 6)]
        dice.sort(reverse=True)
        return dice

    def process_throw(self, dice: list, player: Player) -> bool:
        turn_over = True
        res = self.result_dict[dice]

        if res != 0:
            if isinstance(res, list):
                if res[0] != 0: player.add_sips(res[0])
                if res[1] != 0: player.add_baks(res[1])

        return turn_over
