from typing import List, Any, Dict, Optional

from config.cache_conf import get_json_cache, set_cache

CATEGORY_KEY="news:categories"
NEWS_LIST_PREFIX="news_list"

async def get_cached_categories():
    return await get_json_cache(CATEGORY_KEY)

async def set_cache_categories(data:List[Dict[str,Any]],expire:int=7200):
    return await set_cache(CATEGORY_KEY,data,expire)

async def set_cache_news_list(category_id:Optional[int],page:int,page_size:int,data:List[Dict[str,Any]],expire:int=1800):
    key=f"{NEWS_LIST_PREFIX}{category_id}:{page}:{page_size}"
    return await set_cache(key,data,expire)

async def get_cache_news_list(category_id:Optional[int],page:int,page_size:int):
    key = f"{NEWS_LIST_PREFIX}{category_id}:{page}:{page_size}"
    return await get_json_cache(key)