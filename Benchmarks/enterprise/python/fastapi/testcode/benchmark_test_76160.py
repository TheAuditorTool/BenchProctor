# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest76160(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    os.remove(str(data))
    return {"updated": True}
