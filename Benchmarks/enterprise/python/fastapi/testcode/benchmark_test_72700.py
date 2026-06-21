# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from pydantic import BaseModel
import json
from app_runtime import db


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72700(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
