from entity.base_storage import BaseStorage
from exceptions import TooManyOifferentProducts


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyOifferentProducts

        super().add(name, amount)
