# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


_shared_counter_lock = threading.Lock()

async def BenchmarkTest01107(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
