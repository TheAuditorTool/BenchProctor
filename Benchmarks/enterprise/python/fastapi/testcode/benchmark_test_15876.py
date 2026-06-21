# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

async def BenchmarkTest15876(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
