# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import importlib


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04299(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    importlib.import_module(str(data))
    return {"updated": True}
