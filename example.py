from typing import Generic, TypeVar

from pydantic import BaseModel
from typing import Generic, TypeVar, Any
from pydantic import BaseModel, ValidationError

from pydantic import ConfigDict, Field

from fruits import *

T = TypeVar('T')


class MyBox(BaseModel, Generic[T]):
    FRUIT_TYPE: T
    items: list[T] = []





box = MyBox[Pear](FRUIT_TYPE=Pear(), items=[
    Pear(),
])
box.items.append(Apple())
print(box.items)
