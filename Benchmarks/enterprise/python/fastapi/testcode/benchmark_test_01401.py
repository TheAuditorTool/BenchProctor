# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form
import json


_shared_counter_lock = threading.Lock()

async def BenchmarkTest01401(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
