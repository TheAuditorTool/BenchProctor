# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
import json
import pickle


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest31012(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    pickle.loads(data.encode('latin-1'))
    return {"updated": True}
