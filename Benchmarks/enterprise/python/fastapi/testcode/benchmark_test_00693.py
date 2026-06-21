# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest00693(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    os.remove(str(data))
    return {"updated": True}
