class Player:
    def __init__(self, name: str):
        self.name = name
        self.sips = 0
        self.baks = 0

    def add_sips(self, n: int = 1) -> None:
        self.sips += n
        print("{} moet {} meer slokken (totaal {}).".format(self.name, n, self.sips))

    def add_baks(self, n: int = 1) -> None:
        self.baks += n
        print("{} moet {} meer bakken (totaal {}).".format(self.name, n, self.baks))

    def drink_sips(self, n: int = 1) -> None:
        self.sips -= n
        print("{} trok {} slokken ({} over).".format(self.name, n, self.sips))

    def drink_baks(self, n: int = 1) -> None:
        self.baks -= n
        print("{} trok {} bakken ({} over).".format(self.name, n, self.baks))
