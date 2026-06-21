# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def normalise_input(value):
    return value.strip()

async def BenchmarkTest00024(request: Request, req: UserInput):
    json_value = req.payload
    data = normalise_input(json_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
