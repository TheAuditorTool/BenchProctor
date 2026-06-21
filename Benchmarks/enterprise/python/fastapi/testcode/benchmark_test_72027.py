# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import json


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72027(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
