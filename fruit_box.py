from typing import Generic, TypeVar

from pydantic import BaseModel

from fruits import Apple, Pear, Pineapple, Banana

FRUIT = TypeVar('FRUIT')


class Box(BaseModel, Generic[FRUIT]):
    FRUIT_TYPE: FRUIT
    items: list[FRUIT] = list[FRUIT]


box = Box[Apple](FRUIT_TYPE=Apple())
box.items.append(Apple())
print(box.items)
