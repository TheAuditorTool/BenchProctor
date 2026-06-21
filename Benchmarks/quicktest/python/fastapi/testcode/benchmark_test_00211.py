# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import ast


_shared_counter_lock = threading.Lock()

async def BenchmarkTest00211(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return {"updated": True}
