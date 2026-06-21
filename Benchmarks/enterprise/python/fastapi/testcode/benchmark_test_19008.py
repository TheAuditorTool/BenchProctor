# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def normalise_input(value):
    return value.strip()

async def BenchmarkTest19008(request: Request, req: UserInput):
    json_value = req.payload
    data = normalise_input(json_value)
    os.remove(str(data))
    return {"updated": True}
