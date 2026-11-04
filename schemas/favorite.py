from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from schems.base import NewsItemBase

class FavoriteCheckResponse(BaseModel):
    is_favorite: bool=Field(...,alias="isFavorite")

class FavoriteAddResponse(BaseModel):
    news_id:int=Field(...,alias="newsId")

class FavoriteNewsItem(NewsItemBase):
    favorite_id: int=Field(...,alias="favoriteId")
    favorite_time:datetime=Field(...,alias="favoriteTime")
    model_config = ConfigDict(populate_by_name=True,)

class FavoriteListResponse(BaseModel):
    list:list[FavoriteNewsItem]
    total:int
    has_more:bool=Field(...,alias="hasMore")