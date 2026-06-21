# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest10074(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    eval(str(data))
    return {"updated": True}
