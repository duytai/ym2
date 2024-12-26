from omegaconf import DictConfig
from typing import Dict
from ym2 import Stat

class Hello:
    def __init__(self, name: str, **kwargs: Dict[str, str]):
        self.name = name
        print(kwargs)

    def main(self, stat: Stat):
        print(f'Hello {self.name}')
