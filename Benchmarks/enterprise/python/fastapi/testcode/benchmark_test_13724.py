# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import importlib


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest13724(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    importlib.import_module(str(data))
    return {"updated": True}
