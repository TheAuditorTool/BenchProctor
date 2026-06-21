# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


_shared_counter_lock = threading.Lock()

async def BenchmarkTest30077(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
