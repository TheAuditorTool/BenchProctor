# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from pydantic import BaseModel
import importlib


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest31948(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    importlib.import_module(str(data))
    return {"updated": True}
