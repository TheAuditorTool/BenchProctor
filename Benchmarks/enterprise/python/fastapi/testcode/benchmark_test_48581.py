# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest48581(request: Request, req: UserInput):
    json_value = req.payload
    data = default_blank(json_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
