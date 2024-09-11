from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class Sells(BaseModel):
  email: EmailStr
  date_time: datetime
  value: PositiveFloat
  quantity: PositiveInt
  product: str