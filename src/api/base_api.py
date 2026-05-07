from abc import ABC, abstractmethod


class BaseAPI(ABC):

    @abstractmethod
    def get_coordinates(self, country: str):
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str):
        pass
