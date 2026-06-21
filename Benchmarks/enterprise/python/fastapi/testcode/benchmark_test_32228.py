# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest32228(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
