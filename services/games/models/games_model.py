from pydantic import BaseModel, field_validator
from typing import List, Optional


class GameModel(BaseModel):
    category_uuids: List[str]
    price: int
    title: str
    uuid: str

    @field_validator('price', "title", "uuid")
    def fields_are_not_empty(cls, value):
        if not value:
            raise ValueError("Field is empty")
        return value


class MetaModel(BaseModel):
    total: int


class MainModel(BaseModel):
    games: List[GameModel]
    meta: MetaModel