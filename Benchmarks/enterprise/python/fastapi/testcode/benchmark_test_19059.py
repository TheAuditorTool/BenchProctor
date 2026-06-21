# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest19059(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    processed = data[:64]
    globals()['counter'] = int(processed)
    return {"updated": True}
