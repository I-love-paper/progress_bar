import time

class ProgressBar:
    def __init__(self, total_steps, bar_length=40, char_fill='█', char_remain='-', prefix='Progress:', suffix='Complete', decimal_places=1):
        self.total_steps = total_steps
        self.bar_length = bar_length
        self.char_fill = char_fill
        self.char_remain = char_remain
        self.prefix = prefix
        self.suffix = suffix
        self.decimal_places = decimal_places

    def update(self, current_step):
        percent = round((current_step / self.total_steps) * 100, self.decimal_places)
        filled_length = int(self.bar_length * current_step // self.total_steps)
        bar = self.char_fill * filled_length + self.char_remain * (self.bar_length - filled_length)

        print(f'\r{self.prefix} [{bar}] {percent}% {self.suffix}', end='', flush=True)

        if current_step == self.total_steps:
            print('\n')
