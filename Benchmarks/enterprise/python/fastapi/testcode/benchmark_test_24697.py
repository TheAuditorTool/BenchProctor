# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
_shared_counter_lock = threading.Lock()

async def BenchmarkTest24697(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
