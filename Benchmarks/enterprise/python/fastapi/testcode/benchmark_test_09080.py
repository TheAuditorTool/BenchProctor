# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import importlib
import sys


request_state: dict[str, str] = {}

async def BenchmarkTest09080(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
