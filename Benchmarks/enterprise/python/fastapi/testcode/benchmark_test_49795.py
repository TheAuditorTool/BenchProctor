# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def coalesce_blank(value):
    return value or ''

async def BenchmarkTest49795(request: Request, req: UserInput):
    json_value = req.payload
    data = coalesce_blank(json_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
