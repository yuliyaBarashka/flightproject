from abc import ABC, abstractmethod


class BaseAPI(ABC):

    @abstractmethod
    def get_coordinate(self, country: str):
        pass

    @abstractmethod
    def get_aeroplane(self, country: str):
        pass
