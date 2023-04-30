from abc import ABC, abstractmethod

from App.actors.Actor import Actor


class ActorLive(Actor, ABC):
    def __init__(self):
      super().__init__()
    
    @abstractmethod
    def animate(self):
        ...
    
    @abstractmethod
    def get_input(self):
        ...

    @abstractmethod
    def get_status(self):
        ...

    @abstractmethod
    def jump(self):
        ...

    @abstractmethod
    def update(self):
        ...