from pydantic import BaseModel


class Fruit:
    pass


class Apple(BaseModel, Fruit):
    name: str = 'Apple'


class Banana(BaseModel, Fruit):
    name: str = 'Banana'


class Pineapple(BaseModel, Fruit):
    name: str = 'Pineapple'
