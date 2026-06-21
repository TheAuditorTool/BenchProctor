# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib


request_state: dict[str, str] = {}

async def BenchmarkTest58125(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
