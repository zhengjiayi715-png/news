from fastapi.encoders import jsonable_encoder
from sqlalchemy import select,func,update
from sqlalchemy.ext.asyncio import AsyncSession
from cache.news_cache import get_cached_categories, set_cache_categories, get_cache_news_list, set_cache_news_list
from models.news import Category, News
from schems.base import NewsItemBase


async def get_categories(dp:AsyncSession,skip:int=0,limit:int=100):
    cached_categories=await get_cached_categories()
    if cached_categories:
        return cached_categories
    stmt=select(Category).offset(skip).limit(limit)
    result=await dp.execute(stmt)
    categories=result.scalars().all()
    if categories:
        categories=jsonable_encoder(categories)
        await set_cache_categories(categories)
    return categories

async def get_news_list(dp:AsyncSession,category_id:int,skip:int=0,limit:int=10):
    page=skip//limit+1
    cached_list=await get_cache_news_list(category_id,page,limit)
    if cached_list:
        return [News(**item) for item in cached_list]
    stmt=select(News).where(News.category_id==category_id).offset(skip).limit(limit)
    result = await dp.execute(stmt)
    news_list= result.scalars().all()
    if news_list:
        news_data=[NewsItemBase.model_validate(item).model_dump(mode="json",by_alias=False) for item in news_list]
        await set_cache_news_list(category_id,page,limit,news_data)
    return news_list

async def get_new_count(dp:AsyncSession,category_id:int):
    stmt=select(func.count(News.id)).where(News.category_id==category_id)
    result = await dp.execute(stmt)
    return result.scalar_one()

async def get_news_detail(dp:AsyncSession,news_id:int):
    stmt=select(News).where(News.id==news_id)
    result = await dp.execute(stmt)
    return result.scalar_one_or_none()

async def increase_news_views(dp:AsyncSession,news_id:int):
    stmt=update(News).where(News.id==news_id).values(views=News.views + 1)
    result=await dp.execute(stmt)
    await dp.commit()
    return result.rowcount>0

async def get_related_news(dp:AsyncSession,category_id:int,news_id:int,limit:int=5):
    stmt=select(News).where(
        News.category_id==category_id,
        News.id!=news_id
    ).order_by(
        News.views.desc(),
        News.publish_time.desc()
    ).limit(limit)
    result=await dp.execute(stmt)
    related_news= result.scalars().all()
    return[{
        "id": news_detail.id,
        "title": news_detail.title,
        "content": news_detail.content,
        "image": news_detail.image,
        "author": news_detail.author,
        "publishTime": news_detail.publish_time,
        "categoryId": news_detail.category_id,
        "views": news_detail.views
    }for news_detail in related_news]

