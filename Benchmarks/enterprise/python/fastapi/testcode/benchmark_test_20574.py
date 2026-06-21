# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import urlparse
from starlette.responses import JSONResponse
import json
import socket
from app_runtime import redis_client


async def BenchmarkTest20574(request: Request):
    redis_value = redis_client.get('user_data')
    try:
        data = json.loads(redis_value).get('value', redis_value)
    except (json.JSONDecodeError, AttributeError):
        data = redis_value
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = data
    s = socket.create_connection((str(target_url), 80))
    s.close()
    return {"updated": True}
