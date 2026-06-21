# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse
import json


async def BenchmarkTest27515(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
