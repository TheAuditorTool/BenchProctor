# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest55127(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
