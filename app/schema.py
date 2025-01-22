import datetime
from typing import Optional, Union

from pydantic import BaseModel


class MetaObj(BaseModel):
    trace_id: str = ""
    timestamp: str = ""


def get_meta_obj():
    now = datetime.datetime.now()
    return MetaObj(timestamp=str(now.timestamp()))


class SuccessResponse(BaseModel):
    data: Union[dict, list, str, None] = None
    meta: Optional[MetaObj] = get_meta_obj()
