from fastapi import FastAPI
import shema
from lifispan import lifespan
import crud
import models
from models import Session
from dependencies import SessionDependency
from sqlalchemy import select
from constans import STATUS_SUCCESS


app = FastAPI(
    title='Cервис объявлений купли/продажи',
    version='0.0.1',
    lifespan=lifespan
)


@app.get('/v1/advertisement/{advertisement_id}')
async def get_advertisement(advertisement_id:int, session: SessionDependency):
    advertisement_id = await crud.get_item(session,models.Advertisement, advertisement_id)
    return advertisement_id.dict


@app.get('/v1/advertisement', response_model= shema.SearchResult)
async def search_advertisement(title:str, session: SessionDependency):
    advertisement_query = select(models.Advertisement).where(models.Advertisement.title == title)
    advertisements = await session.scalars(advertisement_query)
    return {'result': [advertisement.id_dict for advertisement in advertisements]}



@app.post('/v1/advertisement', response_model=shema.CreateAdvertisementResponse)
async def add_advertisement(advertisement_json: shema.CreateAdvertisementRequest, session: SessionDependency):
    advertisement_item = models.Advertisement(**advertisement_json.model_dump())
    advertisement_item = await crud.add_item(session, advertisement_item)
    return advertisement_item.id_dict

@app.patch('/v1/advertisement/{advertisement_id}', response_model= shema.UpdateAdvertisementResponse)
async def update_advertisement(advertisement_json: shema.UpdateAdvertisementRequest, advertisement_id:int, session: SessionDependency):
    advertisement = await crud.get_item(session,models.Advertisement, advertisement_id)
    for field, value in advertisement_json.model_dump(exclude_unset=True).items():
        setattr(advertisement, field, value)
    advertisement = await crud.add_item(session, advertisement)
    return advertisement.id_dict



@app.delete('/v1/advertisement/{advertisement_id}', response_model= shema.DeleteAdvertisementResponse)
async def delete_advertisement(advertisement_id:int, session: SessionDependency):
    advertisement = await crud.get_item(session, models.Advertisement, advertisement_id)
    if not advertisement:
        return {"status": "error", "message": "Advertisement not found"}
    await crud.delete_item(session, models.Advertisement, advertisement_id)
    return {"status": "success"}






