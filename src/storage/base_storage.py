from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, item):
        pass
