# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest61001(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
