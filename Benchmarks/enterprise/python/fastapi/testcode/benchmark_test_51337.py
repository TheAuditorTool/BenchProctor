# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import re
from starlette.responses import JSONResponse
from types import SimpleNamespace
from app_runtime import redis_client


async def BenchmarkTest51337(request: Request):
    redis_value = redis_client.get('user_data')
    ns = SimpleNamespace(payload=redis_value)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    requests.get(str(data))
    return {"updated": True}
