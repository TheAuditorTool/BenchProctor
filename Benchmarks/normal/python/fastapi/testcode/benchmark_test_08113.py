# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
from starlette.responses import JSONResponse
from app_runtime import redis_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest08113(request: Request):
    redis_value = redis_client.get('user_data')
    reader = make_reader(redis_value)
    data = reader()
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    requests.get(str(target_url))
    return {"updated": True}
