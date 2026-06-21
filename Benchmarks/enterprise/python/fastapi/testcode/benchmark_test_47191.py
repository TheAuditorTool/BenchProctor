# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest47191(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    result = 100 / int(str(data))
    return {"updated": True}
