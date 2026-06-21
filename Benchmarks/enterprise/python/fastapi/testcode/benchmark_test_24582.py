# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest24582(request: Request, req: UserInput):
    json_value = req.payload
    requests.get(str(json_value))
    return {"updated": True}
