# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest26100(request: Request, req: UserInput):
    json_value = req.payload
    size = min(int(json_value) if str(json_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
