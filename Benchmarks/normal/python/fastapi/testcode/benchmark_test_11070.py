# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel
import json


class UserInput(BaseModel):
    payload: str = ''
_shared_counter_lock = threading.Lock()

async def BenchmarkTest11070(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
