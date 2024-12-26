from omegaconf import DictConfig
from ym2 import Stat

class Hello:
    def __init__(self, name: str):
        self.name = name

    def main(self, stat: Stat):
        print(f'Hello {self.name}')
