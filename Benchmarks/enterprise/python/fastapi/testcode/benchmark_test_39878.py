# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest39878(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
