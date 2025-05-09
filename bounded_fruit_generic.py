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

class BananaBox(Box[Banana]):
    
    pass
def main():
    fruit: T = Pear
    fruit_list: list[Pear()] = [
        Pear(),
        # Apple(),
    ]

    box = Box[fruit](FRUIT_TYPE=fruit(), items=fruit_list)
    box.add(Pear())


if __name__ == '__main__':
    # main()
    b = BananaBox(FRUIT_TYPE=Banana())
    b.add(Banana())
    b.add(Apple())
    print(b.items)
