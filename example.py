from typing import Generic, TypeVar

from fruits import *
from pydantic import ConfigDict

T = TypeVar('T', bound=Fruit)


class MyBox(BaseModel, Generic[T]):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    FRUIT_TYPE: T
    items: list[T] = []


fruit: T = Pear
fruit_list: list[Pear()] = [
    Pear(),
    # Apple(),
]

box = MyBox[fruit](FRUIT_TYPE=fruit(), items=fruit_list)
box.model_validate({
    'FRUIT_TYPE': Apple()
})
# print(box.items)
