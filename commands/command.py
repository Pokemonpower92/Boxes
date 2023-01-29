from abc import ABC, abstractmethod


class Command(ABC):
    """
    Commands execute some logic.
    """

    @abstractmethod
    def execute(self) -> None:
        pass
