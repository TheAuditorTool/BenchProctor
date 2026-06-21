# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


_shared_counter_lock = threading.Lock()

async def BenchmarkTest17529(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
