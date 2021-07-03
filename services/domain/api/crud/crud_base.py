from abc import ABC, abstractmethod


class CRUDBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def get(self, **kwargs):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass

    @abstractmethod
    def delete_all(self):
        pass
