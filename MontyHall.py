import random

class MontyHallGame:
    def __init__(self):
        self.prize_door = random.randint(0, 2)
        self.initial_choice = random.randint(0, 2)
        self.host_open = self._open_host_door()
        self.switch_choice = self._get_switch_choice()

    def _open_host_door(self):
        remaining_doors = [door for door in range(3) if door != self.initial_choice and door != self.prize_door]
        return random.choice(remaining_doors)

    def _get_switch_choice(self):
        return [door for door in range(3) if door != self.initial_choice and door != self.host_open][0]

    def is_win_stay(self):
        return self.initial_choice == self.prize_door

    def is_win_switch(self):
        return self.switch_choice == self.prize_door

class MontyHallResults:
    def __init__(self):
        self.win_switch = 0
        self.win_stay = 0

    def record_result(self, win_switch, win_stay):
        if win_switch:
            self.win_switch += 1
        if win_stay:
            self.win_stay += 1

    def get_results(self, runs):
        percent_win_switch = (self.win_switch / runs) * 100
        percent_win_stay = (self.win_stay / runs) * 100
        return percent_win_stay, percent_win_switch

class MontyHallSimulator:
    def __init__(self, runs=1000):
        self.runs = runs
        self.results = MontyHallResults()

    def run_simulation(self):
        for _ in range(self.runs):
            game = MontyHallGame()
            self.results.record_result(game.is_win_switch(), game.is_win_stay())

    def get_results(self):
        return self.results.get_results(self.runs)

if __name__ == "__main__":
    runs = 1000
    simulator = MontyHallSimulator(runs)
    simulator.run_simulation()
    percent_win_stay, percent_win_switch = simulator.get_results()
    print(f"Percent chance of winning by not switching: {percent_win_stay:.2f}%")
    print(f"Percent chance of winning by switching: {percent_win_switch:.2f}%")