from dataclasses import dataclass
from typing import Generic, TypeVar, ReadOnly
from pydantic import BaseModel, conint, confloat, field_validator, Field


class Fruit:
    pass
T = TypeVar('T', bound=Fruit)


class Apple(BaseModel, Fruit):
    name: str = 'Apple'


class Banana(BaseModel, Fruit):
    name: str = 'Banana'


# class Box[T]:
#     def __init__(self):
#         self.items: list[T] = list()
#
#     def add(self, item: T) -> None:
#         self.items.append(item)
#
#     def remove(self, item: T) -> None:
#         self.items.remove(item)


class Box[T]:
    def __init__(self):
        self.items: list[T] = list()

    def add(self, item: T) -> None:
        self.items.append(item)

    def remove(self, item: T) -> None:
        self.items.remove(item)

# Generic[T]
class FruitBox(BaseModel, Generic[T] ):
    fruit_type: T
    pass
    # fruit_type: T
    # items: Field(default=list[T])


class BananaBox(Box[Banana]):
    pass


# def main():
#     apple_box = Box[Apple]()
#     apple_box.add(Apple())
#     apple_box.add(Apple())
#     print(len(apple_box.items))
#
#     # banana_box = BananaBox()
#     # banana_box.add(Banana())
#     # print(len(apple_box.items))
#     # print(type(apple_box))
#     # items = apple_box.items
#     # for row in items:
#     #     print(f'{row=}')
#
#     # print(banana_box)


if __name__ == '__main__':
    fruit_box = FruitBox(fruit_type=Apple())
    print(fruit_box.model_dump())
    # a: T = Apple()
    # print(a)
    # main()
    # apple_box = FruitBox(value=Apple())
    # apple_box.items.append(Apple())
    # apple_box.items.append(Apple())
    # print(len(apple_box.items))

    # a = Apple1()
    # print(a)
