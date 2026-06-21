# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import urlparse
import os
from starlette.responses import JSONResponse


async def BenchmarkTest07659(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parsed = urlparse(env_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JSONResponse({'error': 'forbidden host'}, status_code=403)
    target_url = env_value
    requests.get(str(target_url))
    return {"updated": True}
