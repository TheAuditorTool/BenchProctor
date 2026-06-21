# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
request_state: dict[str, str] = {}
_shared_counter_lock = threading.Lock()

async def BenchmarkTest01037(request: Request, req: UserInput):
    json_value = req.payload
    request_state['last_input'] = json_value
    data = request_state['last_input']
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
