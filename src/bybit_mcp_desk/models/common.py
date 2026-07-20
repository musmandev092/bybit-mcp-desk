"""Fields shared by every Bybit v5 API response envelope."""

from pydantic import BaseModel


class BaseApiResponse(BaseModel):
    retCode: int
    retMsg: str
