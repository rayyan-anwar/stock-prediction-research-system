from pydantic import BaseModel,Field
class PriceRow(BaseModel):
    close: float=Field(gt=0)
    volume: float=Field(gt=0)
class ForecastRequest(BaseModel):
    prices: list[PriceRow]=Field(min_length=15)
class ForecastResponse(BaseModel):
    author: str
    next_price_estimate: float
    direction: str
    methodology: str
