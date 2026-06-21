# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest56233(request: Request, req: UserInput):
    json_value = req.payload
    data, _sep, _rest = str(json_value).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
