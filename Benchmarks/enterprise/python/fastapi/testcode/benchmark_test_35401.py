# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def coalesce_blank(value):
    return value or ''

async def BenchmarkTest35401(request: Request, req: UserInput):
    json_value = req.payload
    data = coalesce_blank(json_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
