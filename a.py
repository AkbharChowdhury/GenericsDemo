from typing import Generic, TypeVar

from fruits import *
from pydantic import ConfigDict, Field

T = TypeVar('T', bound=Fruit)


class Box(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # FRUIT_TYPE: T
    FRUIT_TYPE: Field(
        exclude=False,
        default=T
    )
    items: list[T] = []

    # val: str = Field(
    #     exclude=False,
    #     default="he"
    # )

    def add(self, item: T):
        self.model_validate({'FRUIT_TYPE': item})
        self.items.append(item)

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
    print(box.items)


if __name__ == '__main__':
    b = BananaBox()
#     box = Box[Pear](FRUIT_TYPE=Pear(), items=[])
#     print(box.val)
#     main()


