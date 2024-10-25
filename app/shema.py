from pydantic import BaseModel
import datetime
from typing import Literal


class BaseItemId(BaseModel):
    id:int


class BaseSearchResults(BaseModel):
    result: list[BaseItemId]

class BaseStatus(BaseModel):
    status: Literal['success']


class CreateAdvertisementRequest(BaseModel):
    title: str
    description: str
    price: float
    author: str


class CreateAdvertisementResponse(BaseItemId):
    pass


class GetAdvertisementResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    author: str
    date_add: datetime.datetime


class UpdateAdvertisementRequest(BaseModel):
    title: str |None=None
    description: str |None=None
    price: float |None=None
    author: str |None=None


class UpdateAdvertisementResponse(BaseItemId):
    pass

class SearchResult(BaseSearchResults):
    pass

class DeleteAdvertisementResponse(BaseStatus):
    pass