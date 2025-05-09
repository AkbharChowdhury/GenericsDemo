from typing import Generic, TypeVar

from fruits import *
from pydantic import ConfigDict

T = TypeVar('T', bound=Fruit)


class Box(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    FRUIT_TYPE: T
    items: list[T] = []

    def add(self, item: T):
        self.model_validate({'FRUIT_TYPE': item})
        self.items.append(item)

    def __str__(self):
        return self.items.__str__()


class BananaBox(Box[Banana]):
    pass

    # self.name_ = name


def main():
    fruit: T = Pear
    fruit_list: list[Pear()] = [
        Pear(),
        # Apple(),
    ]

    box = Box[fruit](FRUIT_TYPE=fruit(), items=fruit_list)
    box.add(Pear())
    print(box)


if __name__ == '__main__':
    main()
    # box = Box[Apple](FRUIT_TYPE=Apple(), items=[])
    # box.add(Apple())
    # print(box.items.index(Apple()))
    # main()
    # b = BananaBox(FRUIT_TYPE=Pear())
    # b.add(Banana())
    # # b.add(Apple())
    # print(b.items)
