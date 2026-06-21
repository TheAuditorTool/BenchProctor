# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest51599(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    os.remove(str(data))
    return {"updated": True}
