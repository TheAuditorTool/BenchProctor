# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
_shared_counter_lock = threading.Lock()

async def BenchmarkTest43991(request: Request, req: UserInput):
    json_value = req.payload
    with _shared_counter_lock:
        globals()['counter'] = int(json_value)
    return {"updated": True}
