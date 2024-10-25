from sqlalchemy.ext.asyncio import AsyncSession
from models import ORM_OBJECT, ORM_CLS
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


async def add_item(session: AsyncSession, item: ORM_OBJECT)->ORM_OBJECT:
    session.add(item)
    try:
        await session.commit()
    except IntegrityError as e:
        if e.orig.pgcode =='23505':
            raise HTTPException(status_code=409, detail='the field is not unique')
        raise e
    return item

async def get_item(session: AsyncSession, orm_class: ORM_CLS, item_id: int)->ORM_OBJECT:
    orm_obj = await session.get(orm_class, item_id)
    if orm_obj is None:
        raise HTTPException(status_code= 404, detail='item not found')
    return orm_obj

async def delete_item(session: AsyncSession, orm_class: ORM_CLS, item_id: int):
    orm_obj = await session.get(orm_class, item_id)
    await session.delete(orm_obj)
    await session.commit()

