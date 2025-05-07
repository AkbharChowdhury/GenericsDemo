from typing import Generic, TypeVar, Optional, Any

from pydantic import BaseModel, ConfigDict, Field

from fruits import Fruit, Apple, Banana, Pineapple

T = TypeVar('T', bound=Fruit)


class Box[T]:
    def __init__(self):
        self.__items: list[T] = list()

    def add(self, item: T) -> None:
        self.__items.append(item)

    def remove(self, item: T) -> None:
        self.__items.remove(item)

    @property
    def items(self):
        return self.__items


class BananaBox(Box[Banana]):
    pass

class FruitBox(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    items: list[T] = Field(default_factory=list[T])

    def add(self, item: T):
        self.items.append(item)


def main():
    apple_box = Box[Apple]()
    apple_box.add(Apple())
    apple_box.add(Apple())

    for item in apple_box.items:
        print(item.name)

    banana_box = BananaBox()
    banana_box.add(Banana())


def any_fruit():
    box = FruitBox(items=[Banana(), Apple()])
    box.add(Pineapple())
    print(box.items)
    print(len(box.items))


if __name__ == '__main__':
    any_fruit()

