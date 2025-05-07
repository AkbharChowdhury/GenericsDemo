from typing import Generic, TypeVar, Optional

from pydantic import BaseModel, ConfigDict, Field


class Fruit:
    pass


T = TypeVar('T', bound=Fruit)


class Apple(BaseModel, Fruit):
    name: str = 'Apple'


class Banana(BaseModel, Fruit):
    name: str = 'Banana'


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


class FruitBox(BaseModel, Generic[T]):
    fruit_type: T
    model_config = ConfigDict(arbitrary_types_allowed=True)
    items: list[T] = list[T]
    def add(self, item: T):
        self.items.append(item)

    pass
    # fruit_type: T
    # items: Field(default=list[T])


class BananaBox(Box[Banana]):
    pass


def main():
    apple_box = Box[Apple]()
    apple_box.add(Apple())
    apple_box.add(Apple())

    for item in apple_box.items:
        print(item.name)

    banana_box = BananaBox()
    banana_box.add(Banana())


if __name__ == '__main__':
    # main()
    box = FruitBox(fruit_type=Banana())
    box.add(Banana())
    print(len(box.items))
    # print(box.items)
    # print(type(box.items))
