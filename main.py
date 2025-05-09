from typing import Generic, TypeVar, Any

from pydantic import ConfigDict, Field

from fruits import *

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

    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)


class FruitBoxSpecific(BaseModel, Generic[T]):
    FRUIT_TYPE: T
    items: list[T] = []
    model_config = ConfigDict(arbitrary_types_allowed=True)



    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)


def main():
    apple_box = Box[Apple]()
    print(type(apple_box))
    apple_box.add(Apple())
    apple_box.add(Apple())

    banana_box = BananaBox()
    banana_box.add(Banana())


def any_fruit():
    box = FruitBox(items=[Banana(), Apple()])
    box.add(Pineapple())
    box.add(Pear())
    print(box.items)
    box.remove(Pear())
    box.remove(Apple())
    print(box.items)


def fruit_specific():
    box = FruitBoxSpecific[Pear](FRUIT_TYPE=Pear(), items=[
        Pear(),
    ])
    # Box[Apple]()
    box.add(Apple())
    box.add(Apple())
    box.add(Apple())
    box.add(Apple())
    box.add(Banana())
    box.add(Pear())
    for item in box.items:
        print(item)
    print(len(box.items))


if __name__ == '__main__':
    fruit_specific()
    # any_fruit()
    # main()
