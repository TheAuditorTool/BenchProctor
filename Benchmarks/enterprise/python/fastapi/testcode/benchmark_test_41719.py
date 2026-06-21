# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest41719(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
